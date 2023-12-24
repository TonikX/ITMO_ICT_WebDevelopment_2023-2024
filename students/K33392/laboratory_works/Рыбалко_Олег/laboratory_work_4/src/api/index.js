import axios from 'axios'
const instance = axios.create({
  baseURL: 'http://localhost:8080',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  },
})
instance.interceptors.request.use(function (cfg) {
  cfg.headers.Authorization = `Token ${localStorage.getItem("auth_token")}`
  return cfg
}, function (error) {
  return Promise.reject(error)
})
export default instance