import { defineStore } from 'pinia'
import { api } from '../api/axios'
import { Notify } from 'quasar'

export const useRequestsStore = defineStore('requests', {
  state: () => ({
    isLoading: false,
    requestsFrom: [],
    requestsTo: [],
    request: null
  }),

  actions: {
    async getRequestsFrom() {
      this.isLoading = true
      try {
        const response = await api.get('/api/requests/from/')
        if (response.status === 200) {
          this.requestsFrom = response.data
        }
      } catch (_) {
        this.requestsFrom = []
      } finally {
        this.isLoading = false
      }
    },

    async getRequestsTo() {
      this.isLoading = true
      try {
        const response = await api.get('/api/requests/to/')
        if (response.status === 200) {
          this.requestsTo = response.data
        }
      } catch (_) {
        this.requestsTo = []
      } finally {
        this.isLoading = false
      }
    },

    async getRequest(payload) {
      this.isLoading = true
      try {
        const response = await api.get(`/api/requests/${payload}/`)
        if (response.status === 200) {
          this.request = response.data
          return true
        }
      } catch (_) {
        this.request = null
      } finally {
        this.isLoading = false
      }
    },

    async addRequest(payload) {
      this.isLoading = true
      try {
        const response = await api.post('/api/requests/create/', payload)
        if (response.status === 200) {
          Notify.create({
            color: 'green',
            textColor: 'white',
            icon: 'error',
            message: 'Success',
            caption: 'Request added',
            position: 'bottom-right'
          })
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    },

    async updateRequest(payload) {
      this.isLoading = true
      try {
        const response = await api.put(`/api/requests/${payload.id}/update/`, payload)
        if (response.status === 200) {
          Notify.create({
            color: 'green',
            textColor: 'white',
            icon: 'error',
            message: 'Success',
            caption: 'Request updated',
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
