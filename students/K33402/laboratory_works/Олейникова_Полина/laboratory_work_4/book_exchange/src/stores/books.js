import { defineStore } from 'pinia'
import { api } from '../api/axios'
import { Notify } from 'quasar'

export const useBooksStore = defineStore('books', {
  state: () => ({
    isLoading: false,
    books: {},
    myBooks: {},
    book: null,
    dates: []
  }),

  actions: {
    async getBooks(payload) {
      this.isLoading = true
      try {
        const response = await api.get('/api/books/', {
          params: payload
        })
        if (response.status === 200) {
          this.books = response.data
        }
      } catch (_) {
        this.books = []
      } finally {
        this.isLoading = false
      }
    },

    async getMyBooks(payload) {
      this.isLoading = true
      try {
        const response = await api.get('/api/books/own/', {
          params: payload
        })
        if (response.status === 200) {
          this.myBooks = response.data
        }
      } catch (_) {
        this.myBooks = []
      } finally {
        this.isLoading = false
      }
    },

    async getBook(payload) {
      this.isLoading = true
      try {
        console.log(payload)
        const response = await api.get(`/api/books/${payload}/`)
        if (response.status === 200) {
          this.book = response.data
          return true
        }
      } catch (_) {
        this.book = null
      } finally {
        this.isLoading = false
      }
    },

    async addBook(payload) {
      this.isLoading = true
      try {
        const response = await api.post('/api/books/create/', payload)
        if (response.status === 200) {
          Notify.create({
            color: 'green',
            textColor: 'white',
            icon: 'error',
            message: 'Success',
            caption: 'Book added',
            position: 'bottom-right'
          })
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    },

    async updateBook(payload) {
      this.isLoading = true
      try {
        const response = await api.put(`/api/books/${payload.id}/update/`, payload)
        if (response.status === 200) {
          Notify.create({
            color: 'green',
            textColor: 'white',
            icon: 'error',
            message: 'Success',
            caption: 'Book updated',
            position: 'bottom-right'
          })
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    },

    async removeBook(payload) {
      this.isLoading = true
      try {
        const response = await api.delete(`/api/books/${payload}/delete/`)
        if (response.status === 200) {
          Notify.create({
            color: 'green',
            textColor: 'white',
            icon: 'error',
            message: 'Success',
            caption: 'Book deleted',
            position: 'bottom-right'
          })
          return true
        }
      } catch (_) {
      } finally {
        this.isLoading = false
      }
    },

    async getAvailableDates(payload) {
      try {
        const response = await api.get(`/api/books/${payload.id}/dates/`, { params: payload })
        if (response.status === 200) {
          this.dates = response.data
          return true
        }
      } catch (_) {
        this.dates = []
      }
    }
  }
})
