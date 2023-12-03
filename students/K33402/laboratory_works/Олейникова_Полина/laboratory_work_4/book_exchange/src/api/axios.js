import axios from 'axios'
import { useUserStore } from '../stores/user'
import { errorHandler } from '../helpers/errorHandler'

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers: {
        'Content-type': 'application/json',
        'X-CSRFToken': 'oOdoOuaBF1xkIfVsP5PdGomSFnguDuybCWrtyJmYV3lHsGAnHtkTynEhwDRfDM3Z'
    }
})

api.interceptors.request.use(
    config => {
        const userStore = useUserStore()
        const { token } = userStore
        if (token) {
            config.headers['Authorization'] = `Token ${token}`
        }
        return config
    }
)

api.interceptors.response.use(
    response => response,
    error => {
        errorHandler(error)
        return Promise.reject(error)
    }
)

export { api }