<template>
  <div>
    <input v-model="username" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/>
    <button @click="setLogin">Войти</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    async setLogin() {
      try {
        const response = await axios.post('http://localhost:8000/auth/token/login',
          {username: this.username, password: this.password})
        sessionStorage.setItem('token', response.data.auth_token)
        sessionStorage.setItem('username', this.username)
        sessionStorage.setItem('password', this.password)
        await this.$router.push({name: "UserPage"})
        // this.mountains = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },

}
</script>

<style scoped>

</style>
