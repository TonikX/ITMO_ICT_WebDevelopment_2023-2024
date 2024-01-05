import { defineStore } from 'pinia'
import router from "../router";
import http from "../services/httpClient";

const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
  }),
  getters: {
    isAuthenticated() {
      return this.user !== null
    },
  },
  actions: {
    setUser(user) {
      this.user = user
    },
    register(user) {
      http.post(
        'register',
        {...user},
        ).then(res => {
          router.push({name: 'login'})
      }).catch(e => {
        //
      })
    },
    login(user) {
      http.post(
        'login',
        {...user}
      ).then(res => {
        router.push({name: 'home'})
      }).catch(err => {
        //
      })
    },
    logout() {
      http.post(
        'logout',
      ).then(res => {
        this.$reset()
        router.push({name: 'login'})
      })
    },
    async getUser() {
      if (!this.user) {
        let user
        try {
          user = (await http.get('me')).data
        } catch (e) {
          user = null
        }

        this.user = user
      }

      return this.user
    },
  },
  persist: true,
})

export default useAuthStore