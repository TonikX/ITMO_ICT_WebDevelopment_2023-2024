<template>
  <div class="container">
    <h2>Войти</h2>
    <form @submit.prevent="loginUser">
      <label for="username">Имя пользователя:</label>
      <input type="text" id="username" v-model="username" required />

      <label for="password">Пароль:</label>
      <input type="password" id="password" v-model="password" required />

      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await axios.post('http://localhost:8000/auth/token/login/', {
          username: this.username,
          password: this.password,
        });

        const accessToken = response.data.auth_token;

        localStorage.setItem('access_token', accessToken);

        console.log('Login successful. Token:', accessToken);

        // Set isAuthenticated to true in the root Vue instance
        this.$root.isAuthenticated = true;

        // Redirect the user to the profile page or another page
        this.$router.push('/profile');

        console.log('Login successful. Token:', accessToken);
      } catch (error) {
        console.error('Login failed:', error.response.data);
      }
    },
  },
};
</script>