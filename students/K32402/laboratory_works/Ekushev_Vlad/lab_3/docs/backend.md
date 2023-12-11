# Реализация бекенда

### Схема БД Prisma

```python
# packages/shared/prisma/schema.prisma

model User {
  id             BigInt  @id
  canCreateEvent Boolean
  avatarUrl      String?

  names           UserNames[]
  moderatedEvents AdminOnEvent[]
  bookings        Booking[]
}

model UserNames {
  user   User   @relation(fields: [userId], references: [id])
  userId BigInt

  name String

  @@id([userId, name])
}

model Booking {
  id            Int           @id @default(autoincrement())
  code          Int           @unique
  guestsCount   Int
  ticketPrice   Int
  isActive      Boolean
  isPaid        Boolean
  paymentMethod PaymentMethod
  createdAt     DateTime      @default(now())

  event   Event  @relation(fields: [eventId], references: [id])
  eventId Int
  user    User   @relation(fields: [userId], references: [id])
  userId  BigInt
}

model AdminOnEvent {
  user   User   @relation(fields: [userId], references: [id])
  userId BigInt

  event   Event @relation(fields: [eventId], references: [id])
  eventId Int

  @@id([userId, eventId])
}

model Event {
  id               Int      @id @default(autoincrement())
  price            Int
  title            String
  description      String
  place            String
  placeUrl         String
  date             DateTime
  totalTickets     Int
  availableTickets Int
  createdAt        DateTime @default(now())

  admins      AdminOnEvent[]
  bookings    Booking[]
  actionChips ActionChip[]
  covers      EventCover[]
}

model ActionChip {
  id          Int     @id @default(autoincrement())
  title       String
  description String
  icon        String
  action      String?

  event   Event @relation(fields: [eventId], references: [id])
  eventId Int
}

model EventCover {
  id    Int    @id @default(autoincrement())
  index Int?
  url   String

  event   Event? @relation(fields: [eventId], references: [id])
  eventId Int?
}
```

Генерация типов и создание миграций производится командой `prisma migrate dev`. Prism автоматически создаёт внутри node_modules `.d.ts` файлы для моделей, описанных в `schema.prisma`. После выполнения миграций, к базе данных можно подключиться через PgAdmin.

### Визуализация связей в БД

<img src="/assets/schema.png" />

### Валидация токена от Telegram

```typescript
const TOKEN_EXPIRY_DATE = 86400

export function validate(
  sp: string | URLSearchParams,
  token: string
): void {
  const searchParams = typeof sp === 'string' ? new URLSearchParams(sp) : sp
  const params: string[] = []
  let authDate = new Date(0)
  let hash = ''

  searchParams.forEach((value, key) => {
    if (key === 'hash') {
      hash = value
      return
    }

    if (key === 'auth_date') {
      const authDateNum = parseInt(value, 10)

      if (Number.isNaN(authDateNum)) {
        throw new TypeError('"auth_date" should present integer')
      }
      authDate = new Date(authDateNum * 1000)
    }

    params.push(`${key}=${value}`)
  })

  if (authDate.getTime() + TOKEN_EXPIRY_DATE * 1000 < new Date().getTime()) {
    throw new Error('Init data expired')
  }

  params.sort()

  const computedHash = createHmac(
    'sha256',
    createHmac('sha256', 'WebAppData').update(token).digest()
  )
    .update(params.join('\n'))
    .digest()
    .toString('hex')

  if (computedHash !== hash) {
    throw new Error('Signature is invalid')
  }
}
```

### Middleware для валидации токена и создания пользователя

Создаём пользователя, если он в первый раз заходит в приложение. Записывать данные об аватарке и данные об именах пользователя необходимо для того, чтобы в админке можно было добавлять пользователей как проверяющих билетов, а также чтобы при покупке билета отображались данные пользователя. Из API Telegram, к сожалению, эти данные получить нельзя (что довольно странно, но оправдывается молодым возрастом компании).

```typescript
// packages/backend/src/middlewares/tgAuth.ts
...

/** Поле с данными пользователя от Telegram из WebAppInit */
export const tgUserDataSymbol: unique symbol = Symbol('tgAuth')

export const tgAuthMiddleware = asyncHandler(
  async (req: Request, _: Response, next: NextFunction) => {
    const authorizationHeader = req.headers.authorization

    if (!authorizationHeader) {
      throw new AuthenticationError('Authorization header is not defined')
    }

    if (!authorizationHeader.startsWith('Bearer ')) {
      throw new AuthenticationError('Authorization header is invalid')
    }

    const tgWebAppInitData = authorizationHeader.slice('Bearer '.length)

    try {
      validate(tgWebAppInitData, BOT_SECRET_KEY)
    } catch (e) {
      throw new AuthenticationError('Invalid TG signature')
    }

    const parsedInitData = initData.parse(tgWebAppInitData)
    if (!parsedInitData.user) {
      throw new AuthenticationError('User not found')
    }

    // eslint-disable-next-line @typescript-eslint/no-non-null-assertion
    req[tgUserDataSymbol] = (await prisma.$transaction(async (tx) => {
      if (!parsedInitData.user) {
        return
      }
      const userId = BigInt(parsedInitData.user.id)

      let user = await tx.user.findFirst({
        where: {
          id: userId,
        },
        include: {
          names: {
            select: {
              name: true,
            },
          },
        },
      })
      const names = Array.from(
        new Set(
          [
            ...(user?.names || []),
            ...(parsedInitData.user.username
              ? [{ name: parsedInitData.user.username }]
              : []),
          ].map(({ name }) => name)
        ).values()
      )

      // Добавляем пользователя, если его не существует
      if (!user) {
        const userPhotos = await bot.telegram.getUserProfilePhotos(
          Number(userId)
        )
        const fileId = userPhotos.photos[0]?.[0]?.file_id || ''
        const avatarUrl = fileId
          ? await bot.telegram.getFileLink(fileId)
          : undefined
        const avatarBuffer =
          avatarUrl && (await downloadUserAvatar(avatarUrl.href))
        const loadPath = avatarBuffer && (await saveFileToUploads(avatarBuffer))

        user = await tx.user.create({
          data: {
            id: userId,
            canCreateEvent: false,
            avatarUrl: loadPath,
          },
          include: {
            names: {
              select: {
                name: true,
              },
            },
          },
        })
      }

      // Добавляем юзернеймы пользователя
      await tx.userNames.createMany({
        skipDuplicates: true,
        data: names.map((name) => ({
          userId,
          name,
        })),
      })

      // eslint-disable-next-line @typescript-eslint/ban-ts-comment
      // @ts-ignore
      delete user.names

      return {
        ...user,
        names,
      }
    }))

    next()
  }
)

const downloadUserAvatar = async (url: string) => {
  const response = await axios.get(url, { responseType: 'arraybuffer' })
  return Buffer.from(response.data, 'utf-8')
}

declare module 'express-serve-static-core' {
  export interface Request {
    [tgUserDataSymbol]: User & { names: string[] }
  }
}
```

### Получение объекта пользователя по данным от WebAppInit

```typescript
// packages/backend/src/routes/user.ts
...

userRouter.get<
  '/users.getSelf',
  core.RouteParameters<'/users.getSelf'>,
  UserGetSelfRes,
  UsersGetSelfReq
>(
  '/users.getSelf',
  asyncHandler(async (req, res) => {
    const user = await prisma.user.findFirst({
      where: {
        id: req[tgUserDataSymbol].id,
      },
    })

    if (!user) {
      throw new AuthenticationError()
    }

    res.json({
      user,
    })
  })
)
```

### Получение объекта пользователя по юзернейму

```typescript
// packages/backend/src/routes/user.ts
...

const usersGetByNameValidator = z.object({
  username: z.string().nonempty(),
})
userRouter.post<
  '/users.getByName',
  core.RouteParameters<'/users.getByName'>,
  UsersGetByNameRes,
  UsersGetByNameReq
>(
  '/users.getByName',
  asyncHandler(async (req, res) => {
    const validated = usersGetByNameValidator.safeParse(req.body)
    if (!validated.success) {
      throw new InvalidParamsError()
    }

    if (!req[tgUserDataSymbol].canCreateEvent) {
      throw new AccessDeniedError()
    }

    const user = await prisma.user.findFirst({
      where: {
        names: {
          some: {
            name: {
              equals: req.body.username,
            },
          },
        },
      },
      include: {
        names: true,
        moderatedEvents: true,
      },
    })

    if (!user) {
      throw new NotFoundError('User not found')
    }

    res.json({
      user,
    })
  })
)
```