## example of store books

```
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
```