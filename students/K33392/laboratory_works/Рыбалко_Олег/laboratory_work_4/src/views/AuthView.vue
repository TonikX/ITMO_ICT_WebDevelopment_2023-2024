<script>
import api from '@/api'
import router from '@/router'
import { useAuthStore } from '@/store/auth'
export default {
  data() {
    this.authStore = useAuthStore()
    return {
      signupData: {
        email: '',
        username: '',
        password: '',
      },
      loginData: {
        email: '',
        username: '',
        password: '',
      },
    }
  },
  methods: {
    login() {
      api
        .post('auth/token/login', {
          username: this.loginData.username,
          password: this.loginData.password,
        })
        .then((resp) => resp.data)
        .then((data) => {
          this.authStore.login(
            this.loginData.username,
            this.loginData.password,
            data.auth_token
          )
          router.push({ path: '/profile' })
        })
    },
    signup() {
      api
        .post('api/users/', {
          email: this.signupData.email,
          username: this.signupData.username,
          password: this.signupData.password,
        })
        .then((resp) => resp.data)
        .then((data) => {
          this.authStore.login(
            this.signupData.username,
            this.signupData.password,
            data.auth_token
          )
          router.push({ path: '/profile' })
        })
    },
  },
}
</script>

<template>
  <div class="login">
    <h3>Login</h3>
    <label for="username">Username</label>
    <input type="text" name="username" v-model="loginData.username" />
    <br />
    <br />
    <label for="password">Password</label>
    <input type="password" name="password" v-model="loginData.password" />
    <br />
    <br />
    <button v-on:click="login">Login</button>
  </div>
  <div class="signup">
    <h3>Sign Up</h3>
    <label for="email">Email</label>
    <input type="text" name="email" v-model="signupData.email" />
    <br />
    <br />
    <label for="username">Username</label>
    <input type="text" name="username" v-model="signupData.username" />
    <br />
    <br />
    <label for="password">Password</label>
    <input type="password" name="password" v-model="signupData.password" />
    <br />
    <br />
    <button v-on:click="signup">Sign Up</button>
  </div>
</template>

