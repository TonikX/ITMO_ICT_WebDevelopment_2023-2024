import { Notify } from 'quasar'


export const errorHandler = error => {
  let message = 'Error'
  let caption = error.message
  if (error.response?.data && typeof error.response?.data === 'object') {
    message = Object.keys(error.response.data).join(', ')
    caption = Object.values(error.response.data).join(', ')
  }
  Notify.create({
    color: 'red',
    textColor: 'white',
    icon: 'error',
    message: message,
    caption: caption,
    position: 'bottom-right'
  })
}
