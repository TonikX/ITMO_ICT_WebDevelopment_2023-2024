<template>
    <div>
      <h1>Вход</h1>
      <form @submit.prevent="login">
        <div>
          <label for="username">Логин:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div>
          <label for="password">Пароль:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Войти</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UserLogin',
    data() {
      return {
        username: '',
        password: '',
      };
    },
    methods: {
      login() {
        axios.post('http://127.0.0.1:8000/auth/token/login/', {
          username: this.username,
          password: this.password,
        })
        .then(response => {
          console.log('Успешный вход:', response.data);

          this.$router.push({ name: 'EventHome' });
        })
        .catch(error => {
          
          console.error('Ошибка входа:', error.response.data);
          // Здесь можете обработать ошибку входа
        });
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
  