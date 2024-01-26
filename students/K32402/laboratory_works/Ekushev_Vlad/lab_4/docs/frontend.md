# Фронтенд

До выполнения ЛР была выполнена базовая верстка и привязка к mock-данным без запросов к бекенду. С помощью библиотеки RTK Query был реализован стор для запросов к API и авторизации.

### Авторизация

Для авторизации нужно подставлять правильный токен из стора в заголовки запроса. Также, в случае ошибки запроса из-за того, что запрос не прошёл авторизацию (ошибка 401), следует перезапросить токены с помощью refresh токена. Блокируем последующие запросы, чтобы не плодить заведомо ошибочные запросы.

```typescript
// src/api/customFetchBase.ts
...

const mutex = new Mutex()

const baseQuery = fetchBaseQuery({
  baseUrl: API_URL,
  credentials: 'include',
  prepareHeaders: (headers, { getState, endpoint }) => {
    const accessToken = (getState() as RootState).auth.accessToken
    const refreshToken = (getState() as RootState).auth.refreshToken

    if (headers.get('Authorization')) {
      return headers
    }

    if (accessToken && endpoint !== 'refresh') {
      headers.set('Authorization', `Bearer ${accessToken}`)
    }

    if (refreshToken && endpoint === 'refresh') {
      headers.set('Authorization', `Bearer ${refreshToken}`)
    }

    return headers
  },
})

const customFetchBase: BaseQueryFn<
  string | FetchArgs,
  unknown,
  FetchBaseQueryError
> = async (args, api, extraOptions) => {
  await mutex.waitForUnlock()

  let result = await baseQuery(args, api, extraOptions)

  if ((result.error?.data as ApiErrorMessage)?.statusCode === 401) {
    if (!mutex.isLocked()) {
      const release = await mutex.acquire()
      const refreshToken = (api.getState() as RootState).auth.refreshToken

      try {
        const refreshResult = await baseQuery(
          {
            credentials: 'include',
            url: '/auth/refresh',
            headers: {
              Authorization: `Bearer ${refreshToken}`,
            },
          },
          api,
          extraOptions
        )

        if (refreshResult.data && typeof args !== 'string') {
          result = await baseQuery(
            {
              ...args,
              headers: {
                Authorization: `Bearer ${
                  (refreshResult.data as Tokens).accessToken
                }`,
              },
            },
            api,
            extraOptions
          )
        } else {
          api.dispatch(logout())
          window.location.href = getRouteByAlias('login').path
        }
      } finally {
        release()
      }
    } else {
      await mutex.waitForUnlock()
      result = await baseQuery(args, api, extraOptions)
    }
  }

  return result
}

export default customFetchBase
```

### API

```typescript
// src/api/index.ts
...

export const apiSlice = createApi({
  baseQuery,
  tagTypes: ['Device', 'User'],
  endpoints: (builder) => ({
    register: builder.mutation<UserRegisterRes, UserRegisterReq>({
      query: (body) => ({
        url: '/auth/register',
        method: 'POST',
        body,
      }),
      async onQueryStarted(_args, { dispatch, queryFulfilled }) {
        const { data } = await queryFulfilled
        dispatch(setAccessToken(data.tokens.accessToken))
        dispatch(setRefreshToken(data.tokens.refreshToken))
      },
      invalidatesTags: (result, _error, _arg) => [
        { type: 'User', id: result?.user.id },
      ],
    }),
    login: builder.mutation<UserLoginRes, UserLoginReq>({
      query: (body) => ({
        url: '/auth/login',
        method: 'POST',
        body,
      }),
      async onQueryStarted(_args, { dispatch, queryFulfilled }) {
        const { data } = await queryFulfilled
        dispatch(setAccessToken(data.tokens.accessToken))
        dispatch(setRefreshToken(data.tokens.refreshToken))
      },
      invalidatesTags: (result, _error, _arg) => [
        { type: 'User', id: result?.user.id },
      ],
    }),
    logout: builder.mutation<void, void>({
      query: () => ({
        url: '/auth/logout',
      }),
    }),
    getDevices: builder.query<DevicesGetRes, DevicesGetReq>({
      query: () => ({
        url: '/devices',
        method: 'GET',
      }),
      providesTags: (result = { devices: [] }) => [
        'Device',
        ...result.devices.map((device) => ({
          type: 'Device' as const,
          id: device.id,
        })),
      ],
    }),
    getFavoritesDevices: builder.query<DevicesGetRes, DevicesGetReq>({
      query: () => ({
        url: '/devices/favorites',
        method: 'GET',
      }),
      providesTags: (result = { devices: [] }) => [
        'Device',
        ...result.devices.map((device) => ({
          type: 'Device' as const,
          id: device.id,
        })),
      ],
    }),
    toggleFavoriteDevice: builder.mutation<
      FavoriteDeviceRes,
      FavoriteDeviceReq
    >({
      query: ({ id }) => ({
        url: `/devices/${id}/favorite`,
        method: 'GET',
      }),
      invalidatesTags: (_result, _error, arg) => [
        { type: 'Device', id: arg.id },
      ],
    }),
    toggleDeviceOnOff: builder.mutation<
      ToggleDeviceOnOffRes,
      ToggleDeviceOnOffReq
    >({
      query: ({ id }) => ({
        url: `/devices/${id}/onOff/toggle`,
        method: 'GET',
      }),
      invalidatesTags: (_result, _error, arg) => [
        { type: 'Device', id: arg.id },
      ],
    }),
    deleteDevice: builder.mutation<DeviceDeleteRes, DeviceDeleteReq>({
      query: ({ id }) => ({
        url: `/devices/${id}/delete`,
        method: 'GET',
      }),
      invalidatesTags: ['Device'],
    }),
    addDevice: builder.mutation<AddDeviceRes, AddDeviceReq>({
      query: (body) => ({
        url: '/devices/add',
        method: 'POST',
        body,
      }),
      invalidatesTags: ['Device'],
    }),
    uploadUserAvatar: builder.mutation<
      UserUploadAvatarRes,
      UserUploadAvatarReq
    >({
      query: (body) => ({
        url: '/user/uploadAvatar',
        method: 'POST',
        body,
      }),
      async onQueryStarted(_args, { dispatch, queryFulfilled }) {
        const { data } = await queryFulfilled
        dispatch(setUserAvatar(data.avatarUrl))
      },
      invalidatesTags: ['User'],
    }),
    updateUser: builder.mutation<UserUpdateRes, UserUpdateReq>({
      query: (body) => ({
        url: '/user/update',
        method: 'POST',
        body,
      }),
      invalidatesTags: ['User'],
    }),
  }),
})

export const {
  useLoginMutation,
  useGetDevicesQuery,
  useGetFavoritesDevicesQuery,
  useToggleFavoriteDeviceMutation,
  useLogoutMutation,
  useRegisterMutation,
  useAddDeviceMutation,
  useToggleDeviceOnOffMutation,
  useDeleteDeviceMutation,
  useUpdateUserMutation,
  useUploadUserAvatarMutation,
} = apiSlice
```

### Обновление данных пользователя

Реализовано на странице настроек. Доступно изменение имени пользователя и загрузки аватарки.

```jsx
// src/pages/Settings.tsx
...

export const ACCEPTED_IMAGE_FILE_TYPES = [
  'image/jpeg',
  'image/png',
  'image/webp',
]

const Content = styled('div')(({ theme }) => ({
  padding: theme.spacing(2),
  display: 'flex',
  flexDirection: 'column',
  gap: theme.spacing(2),
  alignItems: 'center',
}))

const SectionTitle = styled('h3')(({ theme }) => ({
  margin: 0,
  fontWeight: 600,
  fontSize: 15,
  color: theme.palette.text.secondary,
  width: '100%',
  maxWidth: `calc(${BUTTON_MAX_WIDTH}px - ${theme.spacing(2)})`,
}))

const Section = styled('div')(({ theme }) => ({
  display: 'flex',
  flexDirection: 'column',
  gap: theme.spacing(1),
  alignItems: 'center',
  alignSelf: 'stretch',
}))

const OnOffButton = styled('label')(({ theme }) => ({
  padding: theme.spacing(1.25, 2),
  paddingRight: theme.spacing(1.25),
  borderRadius: 100,
  boxShadow: '0 0 0 2px inset ' + alpha(theme.palette.text.primary, 0.12),
  fontFamily: theme.typography.fontFamily,
  fontSize: 15,
  fontWeight: 500,
  lineHeight: '20px',
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'center',
  justifyContent: 'space-between',
  width: '100%',
  ...theme.mixins.button,
  '&:active': {
    transform: 'none',
  },
}))

const UploadButtonRoot = styled('button')(({ theme }) => ({
  ...theme.mixins.button,
  width: '100%',
  boxShadow: '0 0 0 2px inset ' + theme.palette.background.default,
  background: 'transparent',
  borderRadius: '100px',
  display: 'flex',
  flexDirection: 'row',
  alignItems: 'center',
  gap: theme.spacing(1),
  height: 52,
  fontFamily: theme.typography.fontFamily,
  fontSize: 15,
  fontWeight: 500,
  padding: theme.spacing(1.25, 2),
  paddingRight: theme.spacing(1.25),
  color: theme.palette.text.primary,
}))

const UploadAvatar: React.FC = () => {
  const $fileInput = useRef<HTMLInputElement>(null)
  const user = useAppSelector((store) => store.auth.user)
  const [avatarUrl, setAvatarUrl] = useState(user?.avatarUrl || '')
  const [uploadUserAvatar, { isLoading }] = useUploadUserAvatarMutation()

  const handleChange: React.ChangeEventHandler<HTMLInputElement> = (e) => {
    if (!$fileInput.current) return

    const uploadedFile = e.target.files?.[0]

    if (!uploadedFile) return
    if (!ACCEPTED_IMAGE_FILE_TYPES.some((e) => e === uploadedFile.type)) return

    const newAvatar = new FormData()
    newAvatar.append('file', uploadedFile)
    newAvatar.append('type', uploadedFile.type)
    newAvatar.append('title', uploadedFile.name)
    uploadUserAvatar(newAvatar)
      .unwrap()
      .then((data) => {
        setAvatarUrl(data.avatarUrl)
      })

    $fileInput.current.value = ''
  }

  const handleClick = () => {
    $fileInput.current?.click()
  }

  return (
    <UploadButtonRoot onClick={handleClick}>
      <input
        placeholder="Выбрать файл"
        type="file"
        name="avatar"
        multiple={false}
        onChange={handleChange}
        style={{ display: 'none' }}
        ref={$fileInput}
      />
      {!isLoading && (
        <UserAvatar avatarUrl={avatarUrl} fullname={user?.fullname} />
      )}
      {isLoading && <CircularProgress color="inherit" size={32} />}
      <AttachFileOutlined />
      Загрузить аватарку
    </UploadButtonRoot>
  )
}

const Settings: React.FC = () => {
  const theme = useAppSelector((store) => store.app.theme)
  const user = useAppSelector((store) => store.auth.user)
  const dispatch = useAppDispatch()
  const [fullname, setFullname] = useState(user?.fullname || '')
  const [updateUser, { isLoading }] = useUpdateUserMutation()

  const handleDarkThemeSwitchChange = () => {
    dispatch(setTheme(theme === Theme.LIGHT ? Theme.DARK : Theme.LIGHT))
  }

  const handleUpdateUserClick = () => {
    updateUser({ fullname })
      .unwrap()
      .then((data) => {
        dispatch(setUser(data.user))
      })
  }

  return (
    <>
      <AppBar fixed header="Настройки" />
      <Content>
        <OnOffButton>
          Тёмная тема
          <Switch
            onChange={handleDarkThemeSwitchChange}
            checked={theme === Theme.DARK}
            id="dark-theme-switch"
          />
        </OnOffButton>
        <Section>
          <SectionTitle>Аккаунт</SectionTitle>
          <UploadAvatar />
          <Input
            fullWidth
            disableUnderline
            value={fullname}
            type="fullname"
            placeholder="Имя пользователя"
            onChange={(e) => setFullname(e.target.value)}
          />
          <Button
            disabled={isLoading}
            sx={{ gap: 1 }}
            onClick={handleUpdateUserClick}
          >
            {isLoading && <CircularProgress color="inherit" size={16} />}
            Сохранить
          </Button>
        </Section>
      </Content>
    </>
  )
}

export default Settings
```

По той же структуре реализованы функции у девайсов.
