# Бекенд

### Авторизация

Реализована авторизация через JWT токен. Для этого требуется создать 4 роута: регистрация, логин, обновление токенов, выход из аккаунта. Ниже представлен контроллер для модуля `Auth`:

```typescript
// src/auth/auth.controller.ts
export interface RequestWithUser extends Request {
  user: {
    userId: string
    email: string
  }
}

@ApiTags('auth')
@Controller('auth')
export class AuthController {
  constructor(private authService: AuthService) {}

  @UseGuards(LocalAuthGuard)
  @Post('login')
  async login(@Request() req: RequestWithUser): Promise<UserLoginRes> {
    return await this.authService.login(req.user.userId, req.user.email)
  }

  @UseGuards(JwtAuthGuard)
  @Get('logout')
  async logout(@Request() req: RequestWithUser) {
    return await this.authService.logout(req.user.userId)
  }

  @Post('register')
  async register(
    @Body() { email, fullname, password, avatarUrl }: RegisterDto
  ): Promise<UserRegisterRes> {
    return await this.authService.register({
      email,
      fullname,
      password,
      avatarUrl,
    })
  }

  @UseGuards(JwtRefreshTokenAuthGuard)
  @Get('refresh')
  async refreshTokens(@Req() req: RequestWithJwtPayload) {
    const userId = req.user.sub
    const refreshToken = req.user.refreshToken
    return await this.authService.refreshTokens(userId, refreshToken)
  }
}
```

Реализация генерации токенов и авторизации:

```typescript
// src/auth/auth.service.ts
...
export interface JwtPayload {
  email: string
  sub: string
}

@Injectable()
export class AuthService {
  constructor(
    private jwtService: JwtService,
    private userService: UserService,
    private configService: ConfigService
  ) {}

  serializeUserDocument(user: UserDocument): ApiUser {
    return {
      email: user.email,
      fullname: user.fullname,
      id: user.id,
      avatarUrl: user.avatarUrl,
    }
  }

  async updateRefreshToken(userId: string, refreshToken: string) {
    const hashedRefreshToken = await this.userService.hash(refreshToken)
    await this.userService.update(userId, {
      refreshToken: hashedRefreshToken,
    })
  }

  async removeRefreshToken(userId: string) {
    await this.userService.update(userId, {
      refreshToken: null,
    })
  }

  async refreshTokens(userId: string, refreshToken: string) {
    const user = await this.userService.findById(userId)

    if (!user || !user.refreshToken) {
      throw new ForbiddenException('Access denied')
    }

    const refreshTokenMatches = await compare(refreshToken, user.refreshToken)
    if (!refreshTokenMatches) throw new ForbiddenException('Access denied')

    const tokens = await this.getTokens(user.id, user.email)
    await this.updateRefreshToken(user.id, tokens.refreshToken)

    return tokens
  }

  async validateUser(
    email: string,
    password: string
  ): Promise<RequestWithUser['user']> {
    const user = await this.userService.login(email, password)

    return {
      userId: user.id,
      email: user.email,
    }
  }

  async login(userId: string, email: string): Promise<UserLoginRes> {
    const user = await this.userService.findById(userId)
    if (!user) {
      throw new NotFoundException('User not found')
    }

    const tokens = await this.getTokens(userId, email)
    this.updateRefreshToken(userId, tokens.refreshToken)

    return { user: this.serializeUserDocument(user), tokens }
  }

  async logout(userId: string) {
    this.removeRefreshToken(userId)
    return { ok: true }
  }

  async getTokens(id: string, email: string) {
    const [accessToken, refreshToken] = await Promise.all([
      this.jwtService.signAsync(
        {
          sub: id,
          email,
        },
        {
          secret: this.configService.JWT_KEY,
          expiresIn: this.configService.JWT_ACCESS_TOKEN_TTL,
        }
      ),
      this.jwtService.signAsync(
        {
          sub: id,
          email,
        },
        {
          secret: this.configService.JWT_KEY,
          expiresIn: this.configService.JWT_REFRESH_TOKEN_TTL,
        }
      ),
    ])

    return {
      accessToken,
      refreshToken,
    }
  }

  async register(userData: Omit<User, 'devices' | 'refreshToken'>) {
    const user = await this.userService.register(userData)
    const tokens = await this.getTokens(user.id, user.email)
    this.updateRefreshToken(user.id, tokens.refreshToken)

    return { user: this.serializeUserDocument(user), tokens }
  }
}
```

Функция для проверки пароля в сервисе пользователя:

```typescript
// src/user/user.service.ts
...
class UserService {
  ...
  async login(email: string, password: string): Promise<UserDocument> {
    const user = await this.findByEmail(email)

    if (!user) {
      throw new Error('User not found')
    }

    const passwordMatch = await compare(password, user.password)

    if (!passwordMatch) {
      throw new Error('Invalid credentials')
    }

    return user
  }
  ...
}
...
```

### Роуты пользователя

```typescript
// src/user/user.controller.ts
...

@ApiTags('user')
@Controller('user')
export class UserController {
  constructor(
    private readonly userService: UserService,
    private readonly configService: ConfigService
  ) {}

  @UseGuards(JwtAuthGuard)
  @Get()
  @ApiBearerAuth()
  async getSelf(@Request() req: RequestWithUser): Promise<UserGetSelfRes> {
    return await this.userService.getSelf(req.user.userId)
  }

  @UseGuards(JwtAuthGuard)
  @Post('update')
  @ApiBearerAuth()
  async updateInfo(
    @Request() req: RequestWithUser,
    @Body() update: UserUpdateReq
  ): Promise<UserUpdateRes> {
    return await this.userService.updateInfo(req.user.userId, update)
  }

  @UseGuards(JwtAuthGuard)
  @Post('uploadAvatar')
  @UseInterceptors(FileInterceptor('file'))
  @ApiBearerAuth()
  @ApiConsumes('multipart/form-data')
  @ApiBody({
    description: 'Avatar file in "file" field',
    type: AvatarUploadDto,
  })
  async uploadAvatar(
    @Request() req: RequestWithUser,
    @UploadedFile(
      new ParseFilePipe({
        validators: [
          /** 1 MB max size */
          new MaxFileSizeValidator({ maxSize: 100000 }),
          new FileTypeValidator({
            fileType: '.(png|jpeg|jpg|webp)',
          }),
        ],
      })
    )
    file: Express.Multer.File
  ): Promise<UserUploadAvatarRes> {
    return await this.userService.updateAvatar(req.user.userId, file)
  }
}
```

### Роуты девайсов

```typescript
// src/devices/devices.controller.ts
...

@ApiTags('devices')
@Controller('devices')
export class DevicesController {
  constructor(private readonly devicesService: DevicesService) {}

  @UseGuards(JwtAuthGuard)
  @Get()
  async getDevices(@Request() req: RequestWithUser): Promise<DevicesGetRes> {
    const devices = await this.devicesService.getDevices(req.user.userId)
    return { devices }
  }

  @UseGuards(JwtAuthGuard)
  @Get('favorites')
  async getFavoriteDevices(
    @Request() req: RequestWithUser
  ): Promise<DevicesGetRes> {
    const devices = await this.devicesService.getFavoriteDevices(
      req.user.userId
    )
    return { devices }
  }

  @UseGuards(JwtAuthGuard)
  @Get(':id/favorite')
  async toggleFavorite(
    @Request() req: RequestWithUser,
    @Param('id') id: string
  ): Promise<FavoriteDeviceRes> {
    const state = await this.devicesService.toggleFavorite(req.user.userId, id)
    return { state }
  }

  @UseGuards(JwtAuthGuard)
  @Get(':id/onOff/toggle')
  async toggleOnOff(
    @Request() req: RequestWithUser,
    @Param('id') id: string
  ): Promise<ToggleDeviceOnOffRes> {
    const state = await this.devicesService.toggleOnOff(req.user.userId, id)
    return { state }
  }

  @UseGuards(JwtAuthGuard)
  @Get(':id/delete')
  async delete(
    @Request() req: RequestWithUser,
    @Param('id') id: string
  ): Promise<DeviceDeleteRes> {
    const state = await this.devicesService.delete(req.user.userId, id)
    return { ok: state }
  }

  @UseGuards(JwtAuthGuard)
  @Post('add')
  async addDevice(
    @Request() req: RequestWithUser,
    @Body() newDevice: AddDeviceReq
  ): Promise<AddDeviceRes> {
    const device = await this.devicesService.addDevice(
      req.user.userId,
      newDevice
    )
    return { device }
  }
}
```
