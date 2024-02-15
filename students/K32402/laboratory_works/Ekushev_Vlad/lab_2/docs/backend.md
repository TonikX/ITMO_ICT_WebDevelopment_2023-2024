# Реализация бекенда

### Схема модели Event для Prisma

```python
# packages/shared/prisma/schema.prisma

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
```

### Получение по ID

```typescript
const eventsGetByIdValidator = z.object({
  id: z.number().gt(0),
})
eventRouter.post<
  '/events.getById',
  core.RouteParameters<'/events.getById'>,
  EventsGetByIdRes,
  EventsGetByIdReq
>(
  '/events.getById',
  asyncHandler(async (req, res) => {
    const validated = eventsGetByIdValidator.safeParse(req.body)
    if (!validated.success) {
      throw new InvalidParamsError()
    }

    const event =
      (await prisma.event.findFirst({
        where: {
          id: req.body.id,
        },
        include: {
          covers: true,
          actionChips: true,
          admins: {
            include: {
              user: {
                include: {
                  names: true,
                },
              },
            },
          },
          bookings: {
            where: {
              userId: req[tgUserDataSymbol].id,
            },
          },
        },
      })) ?? undefined

    if (!event) {
      throw new NotFoundError()
    }

    const admins = event.admins.map((admin) => ({
      id: admin.userId,
      canCreateEvent: admin.user.canCreateEvent,
      avatarUrl: admin.user.avatarUrl,
      names: admin.user.names,
    }))

    const booking = event?.bookings[0]
    // Need to filter these fields out to not to create another object in memory
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    delete event?.bookings
    // Need to filter these fields out to not to create another object in memory
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    delete event?.admins

    res.json({
      event: {
        ...event,
        admins,
        booking,
      },
    })
  })
)
```

### Получение всех объектов

```typescript
const eventsGetValidator = z.object({
  id: z.number().gt(0).optional(),
  offset: z.number().gt(0).lte(MAX_EVENTS_OFFSET).optional(),
  count: z.number().gt(0).lte(MAX_EVENTS_COUNT).optional(),
})
eventRouter.post<
  '/events.get',
  core.RouteParameters<'/events.get'>,
  EventsGetRes,
  EventsGetReq
>(
  '/events.get',
  asyncHandler(async (req, res) => {
    const validated = eventsGetValidator.safeParse(req.body)
    if (!validated.success) {
      throw new InvalidParamsError()
    }

    const events = await prisma.event.findMany({
      orderBy: {
        createdAt: 'desc',
      },
      where: {
        id: req.body.id || undefined,
      },
      skip: req.body.offset || 0,
      take: req.body.count || MAX_EVENTS_COUNT,
      include: {
        covers: true,
        actionChips: true,
        admins: {
          include: {
            user: {
              include: {
                names: true,
              },
            },
          },
        },
        bookings: {
          where: {
            userId: req[tgUserDataSymbol].id,
          },
        },
      },
    })

    res.json({
      events: events.map(({ admins, bookings, ...event }) => {
        const booking = bookings[0]
        const parsedAdmins = admins.map((admin) => ({
          id: admin.userId,
          canCreateEvent: admin.user.canCreateEvent,
          avatarUrl: admin.user.avatarUrl,
          names: admin.user.names,
        }))

        return {
          ...event,
          booking,
          admins: parsedAdmins,
        }
      }),
    })
  })
)
```

### Создание

```typescript
const eventsCreateActionChipValidator = z.object({
  title: z.string().nonempty(),
  description: z.string().nonempty(),
  action: z.string(),
  icon: z.string().nonempty(),
})
const eventsCreateValidator = z.object({
  title: z.string().nonempty(),
  description: z.string().nonempty(),
  place: z.string().nonempty(),
  price: z.number().gt(0),
  totalTickets: z.number().gt(0),
  date: z.string().nonempty(),
  actionChips: z.array(eventsCreateActionChipValidator),
  admins: z.array(z.string().nonempty()),
  covers: z.array(z.number()),
})
eventRouter.post<
  '/events.create',
  core.RouteParameters<'/events.create'>,
  EventsCreateRes,
  EventsCreateReq
>(
  '/events.create',
  asyncHandler(async (req, res) => {
    const validated = eventsCreateValidator.safeParse(req.body)
    if (!validated.success) {
      throw new InvalidParamsError()
    }

    if (!req[tgUserDataSymbol].canCreateEvent) {
      throw new AccessDeniedError()
    }

    const {
      actionChips: rawActionChips,
      covers: coverIds,
      admins,
      date,
      ...restBody
    } = req.body

    const event = await prisma.event.create({
      data: {
        ...restBody,
        date: new Date(date),
        availableTickets: restBody.totalTickets,
        actionChips: {
          createMany: {
            data: rawActionChips,
          },
        },
        admins: {
          createMany: {
            data: admins.map((userId) => ({ userId })),
          },
        },
      },
      include: {
        actionChips: true,
      },
    })
    const covers = await prisma.$transaction(
      coverIds.map((coverId, coverIndex) =>
        prisma.eventCover.update({
          where: {
            id: coverId,
          },
          data: {
            eventId: event.id,
            index: coverIndex,
          },
        })
      )
    )

    const actionChips = event.actionChips
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-expect-error
    delete event.actionChips

    res.json({
      event,
      actionChips,
      covers,
      admins: [],
    })
  })
)
```

### Редактирование

```typescript
eventRouter.post<
  '/events.edit',
  core.RouteParameters<'/events.edit'>,
  EventsEditRes,
  EventsEditReq
>(
  '/events.edit',
  asyncHandler(async (req, res) => {
    const validated = eventsCreateValidator.safeParse(req.body)
    if (!validated.success) {
      throw new InvalidParamsError()
    }

    if (!req.body.eventId) {
      throw new InvalidParamsError('No `eventId` field')
    }

    if (!req[tgUserDataSymbol].canCreateEvent) {
      throw new AccessDeniedError()
    }

    const {
      actionChips: rawActionChips,
      covers: coverIds,
      admins,
      date,
      eventId,
      ...restBody
    } = req.body

    const newCoverIdsSet = new Set(coverIds)
    const originalEvent = await prisma.event.findFirst({
      where: {
        id: eventId,
      },
      include: {
        covers: true,
        actionChips: true,
      },
    })

    if (!originalEvent) {
      throw new InvalidParamsError(`Event not found with ID "${eventId}"`)
    }

    const bookings = await prisma.booking.findMany({
      where: {
        eventId,
      },
    })

    const alreadyBookedCount = bookings.reduce(
      (acc, booking) => acc + booking.guestsCount,
      0
    )
    if (alreadyBookedCount > restBody.totalTickets) {
      throw new InvalidParamsError(
        `Event already has more bokings than ${restBody.totalTickets}`
      )
    }
    const newAvailableTickets = restBody.totalTickets - alreadyBookedCount

    // Удаляем все карточки от события, чтобы потом создать новые
    await prisma.actionChip.deleteMany({
      where: {
        id: {
          in: originalEvent.actionChips.map((e) => e.id),
        },
      },
    })

    // Удаляем все обложки от события, чтобы потом создать новые
    await prisma.eventCover.deleteMany({
      where: {
        id: {
          in: originalEvent.covers
            .map((e) => e.id)
            .filter((e) => !newCoverIdsSet.has(e)),
        },
      },
    })

    // Удаляем всех админов события, чтобы потом перезаписать их
    await prisma.adminOnEvent.deleteMany({
      where: {
        eventId,
      },
    })

    // Добавляем заново все карточки
    const actionChipsCreated = await prisma.$transaction(
      rawActionChips.map(({ action, description, icon, title }) =>
        prisma.actionChip.create({
          data: { action, description, icon, title, eventId: eventId },
        })
      )
    )

    const coversUpdated = await prisma.$transaction(
      coverIds.map((coverId, coverIndex) =>
        prisma.eventCover.update({
          where: {
            id: coverId,
          },
          data: {
            eventId,
            index: coverIndex,
          },
        })
      )
    )

    const event = await prisma.event.update({
      where: {
        id: eventId,
      },
      data: {
        ...restBody,
        date: new Date(date),
        availableTickets: newAvailableTickets,
        actionChips: {
          set: actionChipsCreated,
        },
        covers: {
          set: coversUpdated,
        },
        admins: {
          createMany: {
            data: admins.map((userId) => ({ userId })),
          },
        },
      },
      include: {
        actionChips: true,
      },
    })

    const actionChips = event.actionChips
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    // @ts-ignore
    delete event.actionChips

    res.json({
      event,
      actionChips,
      covers: coversUpdated,
      admins: [],
    })
  })
)
```

### Удаление

```typescript
eventRouter.post<
  '/events.delete',
  core.RouteParameters<'/events.delete'>,
  EventsDeleteRes,
  EventsDeleteReq
>(
  '/events.delete',
  asyncHandler(async (req, res) => {
    const validated = eventsGetByIdValidator.safeParse(req.body)
    if (!validated.success) {
      throw new InvalidParamsError()
    }

    if (!req[tgUserDataSymbol].canCreateEvent) {
      throw new AccessDeniedError()
    }

    const { id } = validated.data

    await prisma.actionChip.deleteMany({
      where: {
        eventId: id,
      },
    })

    await prisma.eventCover.deleteMany({
      where: {
        eventId: id,
      },
    })

    await prisma.adminOnEvent.deleteMany({
      where: {
        eventId: id,
      },
    })

    await prisma.booking.deleteMany({
      where: {
        eventId: id,
      },
    })

    await prisma.event.delete({
      where: {
        id,
      },
    })

    res.json({ ok: true })
  })
)
```