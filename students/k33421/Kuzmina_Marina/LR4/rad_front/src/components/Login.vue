<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required>

      <label for="password">Password:</label>
      <input type="password" v-model="password" required>

      <button class="styled-button" type="submit">Login</button>
    </form>
  </div>
</template>

<style scoped>
.styled-button {
  background-color: #FFFFFF;
  color: #000000;
  padding: 10px 20px;
  border: 1px solid #ddd;
  cursor: pointer;
  border-radius: 7px;
  transition: transform 0.3s;
}
.styled-button:hover {
  transform: scale(1.1);
}
</style>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login() {
      axios.post('http://localhost:8000/api/login/', {
        username: this.username,
        password: this.password,
      })
        .then(response => {
          console.log(response.data.access);
          const token = response.data.access;
          localStorage.setItem('token', token);
          this.$router.push('/');
        })
        .catch(error => {
            //
            // const errorMessage = Object.entries(error.response.data)
            //   .map(([key, value]) => `${key}: ${value}`)
            //   .join('\n');
            // alert(errorMessage);
            console.error('Login error:', error);
          }
        );
    }
    },
}
</script>

