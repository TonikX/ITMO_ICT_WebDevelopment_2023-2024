<template>
  <div>
    <br>
    <input v-model="username" type="text" placeholder="Username"/>
    <br><br>
    <input v-model="password" type="password" placeholder="Password"/>
    <br><br>
    <button class="button button" @click="setLogin">Login</button>
  </div>
  <div>
    <h3> Don't have the account? Not a problem! You can <a href="/registration">register</a> here </h3>
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
      } catch (error) {
        console.log(error);
      }
    },
  },
}
</script>
<style scoped>
</style>