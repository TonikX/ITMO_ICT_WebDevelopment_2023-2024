<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required>

      <label for="password">Password:</label>
      <input type="password" v-model="password" required>

      <button class="styled-button" type="submit">Register</button>
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
      password: ''
    }
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://localhost:8000/api/register/', {
          username: this.username,
          password: this.password
        })

        // Сохраняем токен в Vuex, localStorage или в состояние компонента
        const token = response.data.access;
        localStorage.setItem('token', token);

        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }
  }
}
</script>


