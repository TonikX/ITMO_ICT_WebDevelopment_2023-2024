import { defineStore } from 'pinia'
import { api } from '../api/axios'
import { Notify } from 'quasar'

export const useUserStore = defineStore('user', {
  state: () => ({
    isLoading: false,
    user: null,
    token: null
  }),

  actions: {
    async login(payload) {
      this.isLoading = true
      try {
        const response = await api.post('/auth/token/login/', payload)
        if (response.status === 200) {
          this.token = response.data.auth_token
          localStorage.setItem('Token', response.data.auth_token)
          await this.getProfile()
          return true
        }
      } catch (_) {
        this.token = null
        localStorage.removeItem('Token')
      } finally {
        this.isLoading = false
      }
    },

    async register(payload) {
      this.isLoading = true
      try {
        const response = await api.post('/auth/users/', payload)
        if (response.status === 201) {
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    },

    async logout() {
      this.isLoading = true
      try {
        const response = await api.post('/auth/token/logout/')
        if (response.status === 204) {
          this.token = null
          this.user = null
          localStorage.removeItem('Token')
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    },

    async getProfile() {
      this.isLoading = true
      try {
        const response = await api.get('/auth/users/me/')
        if (response.status === 200) {
          this.user = response.data
          return true
        }
      } catch (_) {
        this.user = null
        localStorage.removeItem('Token')
      } finally {
        this.isLoading = false
      }
    },

    async updateProfile(payload) {
      this.isLoading = true
      try {
        const response = await api.put('/auth/users/me/', payload)
        if (response.status === 200) {
          this.user = { ...this.user, ...response.data }
          Notify.create({
            color: 'green',
            textColor: 'white',
            icon: 'error',
            message: 'Success',
            caption: 'Profile updated',
            position: 'bottom-right'
          })
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    },

    async updatePassword(payload) {
      this.isLoading = true
      try {
        const response = await api.post('/auth/users/set_password/', payload)
        if (response.status === 200) {
          Notify.create({
            color: 'green',
            textColor: 'white',
            icon: 'error',
            message: 'Success',
            caption: 'Password updated',
            position: 'bottom-right'
          })
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    }
  }
})
