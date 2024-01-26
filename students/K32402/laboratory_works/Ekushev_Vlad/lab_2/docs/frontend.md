# Реализация фронтенда

Реализуем страницу с помощью React.JS для рендеринга и RTK Query для получения данных.

### Описание API

```typescript
import {
  EventCoverUploadReq,
  EventCoverUploadRes,
  EventsCreateReq,
  EventsCreateRes,
  EventsDeleteReq,
  EventsDeleteRes,
  EventsEditReq,
  EventsEditRes,
  EventsGetByIdReq,
  EventsGetByIdRes,
  EventsGetReq,
  EventsGetRes,
} from '@outcy/shared'
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { API_URL } from 'config/constants'

const baseQuery = fetchBaseQuery({
  baseUrl: API_URL,
  prepareHeaders: (headers) => {
    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
    //@ts-ignore
    const token = window.Telegram.WebApp.initData

    if (token) {
      headers.set('authorization', `Bearer ${token}`)
    }

    return headers
  },
})

export const apiSlice = createApi({
  baseQuery,
  tagTypes: ['Event', 'User', 'Admin', 'Booking'],
  endpoints: (builder) => ({
    getEvents: builder.query<EventsGetRes, EventsGetReq>({
      query: (body) => ({
        url: 'events.get',
        method: 'POST',
        body,
      }),
      providesTags: (result = { events: [] }) => [
        'Event',
        ...result.events.map((event) => ({
          type: 'Event' as const,
          id: event.id,
        })),
      ],
    }),
    getEvent: builder.query<EventsGetByIdRes, EventsGetByIdReq>({
      query: (body) => ({
        url: 'events.getById',
        method: 'POST',
        body,
      }),
      providesTags: (result) => [{ type: 'Event', id: result?.event.id }],
    }),
    uploadCover: builder.mutation<EventCoverUploadRes, EventCoverUploadReq>({
      query: (body) => ({
        url: 'covers.upload',
        method: 'POST',
        body,
      }),
    }),
    createEvent: builder.mutation<EventsCreateRes, EventsCreateReq>({
      query: (body) => ({
        url: 'events.create',
        method: 'POST',
        body,
      }),
      invalidatesTags: ['Event'],
    }),
    editEvent: builder.mutation<EventsEditRes, EventsEditReq>({
      query: (body) => ({
        url: 'events.edit',
        method: 'POST',
        body,
      }),
      invalidatesTags: (_result, _error, arg) => [
        { type: 'Event', id: arg.eventId },
      ],
    }),
    deleteEvent: builder.mutation<EventsDeleteRes, EventsDeleteReq>({
      query: (body) => ({
        url: 'events.delete',
        method: 'POST',
        body,
      }),
      invalidatesTags: (_result, _error, arg) => [
        { type: 'Event', id: arg.id },
      ],
    }),
    // ...
  }),
})

export const {
  useGetEventsQuery,
  useUploadCoverMutation,
  useCreateEventMutation,
  useEditEventMutation,
  useDeleteEventMutation,
  useGetEventQuery,
  // ...
} = apiSlice
```

### Реализация страницы

```jsx
import { BackButton, useShowPopup } from '@vkruglikov/react-telegram-web-app'
import Paper from 'components/Paper/Paper'
import React, { useEffect, useMemo, useRef, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import PaperHeader from 'components/PaperHeader/PaperHeader'
import Input from 'components/Input/Input'
import {
  Icon20Attach,
  Icon20CalendarOutline,
  Icon20EuroOutline,
  Icon20Users3Outline,
} from '@vkontakte/icons'
import TextArea from 'components/TextArea/TextArea'
import {
  LocaleProvider,
  DateInput,
  IconButton,
  List,
  Cell,
  Image,
  Spinner,
  Avatar,
} from '@vkontakte/vkui'
import { useForm, SubmitHandler, Controller } from 'react-hook-form'
import Button from 'components/Button/Button'
import './CreateEvent.css'
import './UploadButton.css'
import {
  ACCEPTED_IMAGE_FILE_TYPES,
  EMOJI_STYLE,
  MAX_INT_32,
} from 'config/constants'
import { EventCover } from '@prisma/client'
import {
  useCreateEventMutation,
  useDeleteEventMutation,
  useEditEventMutation,
  useGetEventQuery,
  useLazyGetUserByNameQuery,
  useUploadCoverMutation,
} from '../../api'
import Modals from './Modals'
import {
  EventsCreateReq,
  EventsCreateReqActionChip,
  RichEventAdmin,
  UsersGetByNameRes,
} from '@outcy/shared'
import getImageURL from 'utils/getImageURL'
import { Emoji } from 'emoji-picker-react'
import { skipToken } from '@reduxjs/toolkit/query'
import makeReadOnlyActionChips from 'utils/makeReadOnlyChips'
import FullScreenSpinner from 'components/FullScreenSpinner/FullScreenSpinner'
import SelectEmoji from './SelectEmoji'

type FieldValues = {
  date: Date
  title: string
  description: string
  price?: number
  totalTickets?: number
  place: string
  placeUrl: string
  adminUsername: string
}

type ReorderListFunction = <T>(
  change: {
    from: number
    to: number
  },
  updateList: React.Dispatch<React.SetStateAction<T[]>>
) => void

type RemoveItemFromListFunction = <T>(
  index: number,
  updateList: React.Dispatch<React.SetStateAction<T[]>>
) => void

type ActionChipCellProps =
  | {
      editable: true
      actionChip: EventsCreateReqActionChip
      index: number
      removeItemFromList: RemoveItemFromListFunction
      reorderList: ReorderListFunction
      setActionChips: React.Dispatch<
        React.SetStateAction<EventsCreateReqActionChip[]>
      >
    }
  | {
      editable?: false
      actionChip: EventsCreateReqActionChip
      index: number
      removeItemFromList: undefined
      reorderList: undefined
      setActionChips: undefined
    }

const ActionChipCell: React.FC<ActionChipCellProps> = ({
  editable,
  index,
  actionChip,
  removeItemFromList,
  reorderList,
  setActionChips,
}) => {
  return (
    <Cell
      {...(editable && { mode: 'removable' })}
      draggable={editable}
      hasActive={false}
      hasHover={false}
      before={
        <Paper className="CreateEvent__actionChipIcon" elevation={0}>
          <Emoji emojiStyle={EMOJI_STYLE} unified={actionChip.icon} size={28} />
        </Paper>
      }
      onRemove={() => {
        editable && removeItemFromList(index, setActionChips)
      }}
      onDragFinish={({ from, to }) => {
        editable &&
          reorderList<EventsCreateReqActionChip>({ from, to }, setActionChips)
      }}
    >
      <h1 className="CreateEvent__actionChipTitle">{actionChip.title}</h1>
      <p className="CreateEvent__actionChipDescription">
        {actionChip.description}
      </p>
    </Cell>
  )
}

type ActionChipsProps = {
  readOnlyActionChips: EventsCreateReqActionChip[]
  actionChips: EventsCreateReqActionChip[]
  removeItemFromList: RemoveItemFromListFunction
  reorderList: ReorderListFunction
  setActionChips: React.Dispatch<
    React.SetStateAction<EventsCreateReqActionChip[]>
  >
}

const ActionChips: React.FC<ActionChipsProps> = ({
  readOnlyActionChips,
  actionChips,
  removeItemFromList,
  reorderList,
  setActionChips,
}) => {
  return (
    <>
      <List>
        {readOnlyActionChips.map((actionChip, index) => (
          <ActionChipCell
            editable={false}
            actionChip={actionChip}
            index={index}
            key={index}
            removeItemFromList={undefined}
            reorderList={undefined}
            setActionChips={undefined}
          />
        ))}
      </List>
      <List>
        {actionChips.map((actionChip, index) => (
          <ActionChipCell
            actionChip={actionChip}
            index={index}
            key={index}
            removeItemFromList={removeItemFromList}
            setActionChips={setActionChips}
            reorderList={reorderList}
            editable
          />
        ))}
      </List>
    </>
  )
}

type UploadButtonProps = {
  uploadFile: (file: File) => void
}

const UploadButton: React.FC<UploadButtonProps> = ({ uploadFile }) => {
  const $fileInput = useRef<HTMLInputElement>(null)

  const handleChange: React.ChangeEventHandler<HTMLInputElement> = (e) => {
    if (!$fileInput.current) return

    const uploadedFile = e.target.files?.[0]

    if (!uploadedFile) return
    if (!ACCEPTED_IMAGE_FILE_TYPES.some((e) => e === uploadedFile.type)) return

    uploadFile(uploadedFile)
    $fileInput.current.value = ''
  }

  const handleClick = () => {
    $fileInput.current?.click()
  }

  return (
    <Paper className="UploadButton" button elevation={0} onClick={handleClick}>
      <input
        placeholder="Выбрать файл"
        type="file"
        name="cover"
        multiple={false}
        onChange={handleChange}
        style={{ display: 'none' }}
        ref={$fileInput}
      />
      <div className="UploadButton__before">
        <Icon20Attach />
      </div>
      Выбрать файл
    </Paper>
  )
}

const CreateEvent: React.FC<{ edit?: boolean; selectEmoji?: boolean }> = ({
  edit,
  selectEmoji,
}) => {
  const { id } = useParams<{ id: string }>()
  const { data, isSuccess, isError } = useGetEventQuery(
    id ? { id: Number(id) } : skipToken
  )

  const now = useMemo(() => {
    const date = new Date()
    date.setSeconds(0)
    return date
  }, [])

  const {
    register,
    handleSubmit,
    control,
    watch,
    setValue,
    formState: { errors },
  } = useForm<FieldValues>({
    defaultValues: {
      date: data ? new Date(data.event.date) : now,
      title: data?.event.title || '',
      description: data?.event.description || '',
      price: data?.event.price,
      totalTickets: data?.event.totalTickets,
      place: data?.event.place || '',
      placeUrl: data?.event.placeUrl || '',
      adminUsername: '',
    },
  })
  const [uploadingCoverFile, setUploadingCoverFile] = useState<File | null>(
    null
  )
  const uploadingCoverURL = useMemo(
    () =>
      uploadingCoverFile ? URL.createObjectURL(uploadingCoverFile) : undefined,
    [uploadingCoverFile]
  )
  const showPopup = useShowPopup()
  const [selectedEmoji, setSelectedEmoji] = useState<string | null>(null)
  const [getUserByName, { isLoading: getUserByNameIsLoading }] =
    useLazyGetUserByNameQuery()
  const [uploadCover] = useUploadCoverMutation()
  const [createEvent, { isLoading: createEventIsLoading }] =
    useCreateEventMutation()
  const [editEvent, { isLoading: editEventIsLoading }] = useEditEventMutation()
  const [deleteEvent, { isLoading: deleteEventIsLoading }] =
    useDeleteEventMutation()
  const [covers, setCovers] = useState<EventCover[]>([])
  const [admins, setAdmins] = useState<RichEventAdmin[]>([])
  const [actionChips, setActionChips] = useState<EventsCreateReqActionChip[]>(
    []
  )
  const adminUsernameInputValue = watch('adminUsername')
  const readOnlyActionChipsValues = watch(['price', 'place', 'placeUrl'])
  const readOnlyActionChips = useMemo(
    () => makeReadOnlyActionChips(...readOnlyActionChipsValues),
    [readOnlyActionChipsValues]
  )
  const navigate = useNavigate()

  const handleBack = () => {
    if (edit) {
      navigate(`/events/${id}`)
    } else {
      navigate('/')
    }
  }

  const openAddActionChipModal = () => {
    setSelectedEmoji(null)

    if (edit) {
      navigate(`/events/${id}/edit?modal=addActionChip`)
    } else {
      navigate('/events/create?modal=addActionChip')
    }
  }

  const reorderList: ReorderListFunction = ({ from, to }, updateList) => {
    updateList((prev) => {
      const newList = [...prev]
      const [item] = newList.splice(from, 1)
      item && newList.splice(to, 0, item)
      return newList
    })
  }

  const removeItemFromList: RemoveItemFromListFunction = (
    index,
    updateList
  ) => {
    updateList((prev) => {
      const newList = prev.slice()
      newList.splice(index, 1)
      return newList
    })
  }

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  const isNumberValid = (num: any) => {
    return num && !Number.isNaN(num) && Number(num) > 0
  }

  const handleCoverUpload = (file: File) => {
    setUploadingCoverFile(file)
    const newCover = new FormData()
    newCover.append('cover', file)
    newCover.append('type', file.type)
    newCover.append('title', file.name)
    uploadCover(newCover)
      .unwrap()
      .then((data) => {
        setUploadingCoverFile(null)
        setCovers((prev) => [
          ...prev,
          {
            id: data.cover.id,
            url: data.cover.url,
            eventId: null,
            index: null,
          },
        ])
      })
      .catch(() => {
        setUploadingCoverFile(null)
        showPopup({ message: 'Не удалось загрузить изображение.' })
      })
  }

  const addActionChip = (data: EventsCreateReqActionChip) => {
    setActionChips((prev) => [...prev, data])
  }

  const onSubmit: SubmitHandler<FieldValues> = (form) => {
    if (
      !form.price ||
      !form.totalTickets ||
      covers.length === 0 ||
      createEventIsLoading
    )
      return

    const data: EventsCreateReq = {
      admins: admins.map((admin) => admin.id),
      actionChips,
      covers: covers.map((data) => data.id),
      date: form.date.toString(),
      description: form.description,
      place: form.place,
      placeUrl: form.placeUrl,
      price: form.price,
      title: form.title,
      totalTickets: form.totalTickets,
    }

    const onSuccess = () => {
      navigate('/')
    }

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const onError = (e: any) => {
      showPopup({
        message: e.data.message,
      })
    }

    if (edit) {
      editEvent({ ...data, eventId: Number(id) })
        .unwrap()
        .then(onSuccess)
        .catch(onError)
    } else {
      createEvent(data).unwrap().then(onSuccess).catch(onError)
    }
  }

  const handleDeleteEvent = () => {
    if (deleteEventIsLoading) return

    const onSuccess = () => {
      navigate('/')
    }

    const onError = () => {
      showPopup({
        message: 'Не удалось удалить событие',
      })
    }

    showPopup({
      buttons: [
        { type: 'destructive', text: 'Удалить', id: 'delete' },
        { type: 'cancel', text: 'Отмена', id: 'cancel' },
      ],
      message: `Вы уверены, что хотите удалить событие "${data?.event.title}"?`,
    }).then((data) => {
      if (data === 'cancel') return

      deleteEvent({ id: Number(id) })
        .unwrap()
        .then(onSuccess)
        .catch(onError)
    })
  }

  const handleAddAdmin = () => {
    const formattedValue = adminUsernameInputValue.trim().replace('@', '')

    if (
      admins.some((admin) =>
        admin.names.some((name) => name.name === formattedValue)
      )
    ) {
      showPopup({ message: 'Такой пользователь уже записан как проверяющий' })
      return
    }

    const onSuccess = ({ user }: UsersGetByNameRes) => {
      const newAdmin = {
        id: user.id,
        canCreateEvent: user.canCreateEvent,
        avatarUrl: user.avatarUrl,
        names: user.names,
      }

      setAdmins((prev) => [...prev, newAdmin])
    }

    const onError = () => {
      showPopup({
        message:
          'Пользователь с таким именем не найден.\n\nУбедитесь, что этот человек хотя бы раз зашёл в приложение.',
      })
    }

    getUserByName({ username: formattedValue })
      .unwrap()
      .then(onSuccess)
      .catch(onError)
  }

  const handleRemoveAdmin = (admin: RichEventAdmin) => {
    setAdmins((prev) => prev.filter((e) => e.id !== admin.id))
  }

  const handleSelectEmojiSubmit = (emoji: string) => {
    setSelectedEmoji(emoji)
  }

  useEffect(() => {
    if (!id && edit) {
      navigate('/')
    }
  }, [edit, id, navigate])

  useEffect(() => {
    if (isSuccess) {
      setValue('date', new Date(data.event.date))
      setValue('title', data.event.title)
      setValue('price', data.event.price)
      setValue('totalTickets', data.event.totalTickets)
      setValue('place', data.event.place)
      setValue('placeUrl', data.event.placeUrl || '')
      setActionChips(data.event.actionChips)
      setCovers(data.event.covers)
      setAdmins(data.event.admins || [])
    } else if (edit && isError) {
      navigate('/')
    }
  }, [
    data?.event.actionChips,
    data?.event.date,
    data?.event.place,
    data?.event.placeUrl,
    data?.event.price,
    data?.event.title,
    data?.event.totalTickets,
    data?.event.covers,
    data?.event.admins,
    isSuccess,
    isError,
    edit,
    navigate,
    setValue,
  ])

  if (edit && id && !isSuccess) {
    return <FullScreenSpinner />
  }

  if (selectEmoji) {
    return <SelectEmoji onSubmit={handleSelectEmojiSubmit} />
  }

  return (
    <>
      <div className="CreateEvent">
        <Paper sqare className="CreateEvent__paper">
          <PaperHeader>Информация о событии</PaperHeader>
          <div className="CreateEvent__inputContainer">
            <Input
              state={errors.title ? 'error' : 'default'}
              placeholder="Название события"
              {...register('title', { required: true })}
            />
            <TextArea
              state={errors.description ? 'error' : 'default'}
              minRows={4}
              placeholder="Описание события"
              {...register('description', { required: true })}
            />
          </div>
          <PaperHeader>Билеты</PaperHeader>
          <div className="CreateEvent__inputContainer">
            <Input
              before={<Icon20EuroOutline />}
              placeholder="Стоимость билета"
              type="number"
              autoComplete="off"
              state={errors.price ? 'error' : 'default'}
              min={1}
              max={MAX_INT_32}
              {...register('price', {
                valueAsNumber: true,
                required: true,
                validate: isNumberValid,
              })}
            />
            <Input
              before={<Icon20Users3Outline />}
              placeholder="Количество билетов"
              type="number"
              autoComplete="off"
              state={errors.totalTickets ? 'error' : 'default'}
              min={1}
              max={MAX_INT_32}
              {...register('totalTickets', {
                valueAsNumber: true,
                required: true,
                validate: isNumberValid,
              })}
            />
          </div>
          <PaperHeader>Место проведения</PaperHeader>
          <div className="CreateEvent__inputContainer">
            <Input
              placeholder="Место проведения"
              state={errors.place ? 'error' : 'default'}
              {...register('place', { required: true })}
            />
            <Input
              placeholder="Ссылка на Google Maps"
              type="url"
              state={errors.placeUrl ? 'error' : 'default'}
              {...register('placeUrl', { required: true })}
            />
          </div>
          <PaperHeader>Дата проведения</PaperHeader>
          <div className="CreateEvent__inputContainer">
            <LocaleProvider value={'ru'}>
              <Controller
                name="date"
                control={control}
                rules={{
                  value: new Date(),
                  required: true,
                }}
                render={({ field: { ref, ...fieldProps } }) => (
                  <DateInput
                    className="CreateEvent__vkuiInput"
                    enableTime
                    mode="plain"
                    status={errors.date ? 'error' : 'default'}
                    getRootRef={ref}
                    after={
                      <IconButton aria-label="Calendar">
                        <Icon20CalendarOutline />
                      </IconButton>
                    }
                    {...fieldProps}
                  />
                )}
              />
            </LocaleProvider>
          </div>
        </Paper>

        <Paper sqare className="CreateEvent__paper">
          <PaperHeader>Обложки</PaperHeader>
          <List>
            {covers.map((cover, i) => (
              <Cell
                draggable
                key={cover.id}
                mode="removable"
                before={
                  <Image
                    src={getImageURL(cover.url)}
                    alt="Event cover"
                    size={48}
                  />
                }
                onDragFinish={({ from, to }) =>
                  reorderList<EventCover>({ from, to }, setCovers)
                }
                onRemove={() => removeItemFromList(i, setCovers)}
              >
                ID: {cover.id}
              </Cell>
            ))}
            {uploadingCoverFile && (
              <Cell
                disabled
                before={
                  <Image src={uploadingCoverURL} alt="Event cover" size={48} />
                }
                after={<Spinner />}
                style={{ opacity: 0.4 }}
              >
                {uploadingCoverFile.name}
              </Cell>
            )}
            {covers.length === 0 && !uploadingCoverFile && (
              <p className="CreateEvent__hint">Не загружено ни одной обложки</p>
            )}
          </List>
          <div className="CreateEvent__inputContainer">
            <UploadButton uploadFile={handleCoverUpload} />
          </div>
        </Paper>

        <Paper sqare className="CreateEvent__paper">
          <PaperHeader>Карточки события</PaperHeader>
          <ActionChips
            actionChips={actionChips}
            readOnlyActionChips={readOnlyActionChips}
            removeItemFromList={removeItemFromList}
            reorderList={reorderList}
            setActionChips={setActionChips}
          />
          <div className="CreateEvent__inputContainer">
            <Button type="button" onClick={openAddActionChipModal}>
              Добавить карточку
            </Button>
          </div>
        </Paper>

        <Paper sqare className="CreateEvent__paper">
          <PaperHeader>Проверяющие билетов</PaperHeader>
          <p className="CreateEvent__hint">
            Пользователь обязательно должен хотя бы раз зайти в приложение
          </p>
          <div className="CreateEvent__inputContainer">
            <Input
              {...register('adminUsername')}
              placeholder="Введите юзернейм из TG (например, @admin или admin)"
            />
            <Button
              onClick={handleAddAdmin}
              loading={getUserByNameIsLoading}
              disabled={getUserByNameIsLoading}
            >
              Добавить проверяющего
            </Button>
            {admins.length > 0 && (
              <List className="CreateEvent__adminsList">
                {admins.map((admin) => (
                  <Cell
                    mode="removable"
                    key={admin.id.toString()}
                    onRemove={handleRemoveAdmin.bind(null, admin)}
                    before={
                      <Avatar
                        src={getImageURL(admin.avatarUrl || '')}
                        initials={admin.names[0]?.name.slice(0, 1)}
                        size={44}
                      />
                    }
                  >
                    @{admin.names[0]?.name}
                  </Cell>
                ))}
              </List>
            )}
          </div>
        </Paper>

        <div className="CreateEvent__inputContainer">
          <Button
            onClick={handleSubmit(onSubmit)}
            loading={createEventIsLoading || editEventIsLoading}
            disabled={createEventIsLoading || editEventIsLoading}
          >
            {edit ? 'Сохранить' : 'Создать'}
          </Button>
          {edit && (
            <Button
              loading={deleteEventIsLoading}
              disabled={deleteEventIsLoading}
              onClick={handleDeleteEvent}
              variant="destructive"
            >
              Удалить
            </Button>
          )}
        </div>
      </div>

      <Modals selectedEmoji={selectedEmoji} addActionChip={addActionChip} />
      <BackButton onClick={handleBack} />
    </>
  )
}

export default React.memo(CreateEvent)
```