import {
  mdiAccountCircle,
  mdiSquareEditOutline,
  mdiTable,
} from '@mdi/js'

export default [
  {
    to: '/tables',
    label: 'Таблицы',
    icon: mdiTable
  },
  {
    to: '/forms',
    label: 'Форма',
    icon: mdiSquareEditOutline
  },
  {
    to: '/profile',
    label: 'Профиль',
    icon: mdiAccountCircle
  },
]
