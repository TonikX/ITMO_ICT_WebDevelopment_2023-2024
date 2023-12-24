<script>
import api from '@/api'
import router from '@/router'
import { useAuthStore } from '@/store/auth'
export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login() {
      const authStore = useAuthStore()
      api
        .post('auth/token/login', {
          username: this.username,
          password: this.password,
        })
        .then((resp) => resp.data)
        .then((data) => {
          authStore.login(this.username, this.password, data.auth_token)
          router.push({ path: '/profile' })
        })
    },
  },
}
</script>

<template>
  <h2>Login</h2>
  <label for="username">Username</label>
  <input type="text" name="username" v-model="username" />
  <br />
  <br />
  <label for="password">Password</label>
  <input type="password" name="password" v-model="password" />
  <br />
  <br />
  <button v-on:click="login">Login</button>
</template>

<style></style>

