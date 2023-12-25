<template>
    <div>
      <h2>Вход</h2>
      <form @submit.prevent="login">
        <label for="email">Электронная почта:</label>
        <input type="email" id="email" v-model="userData.email" required>
  
        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="userData.password" required>
  
        <button type="submit">Войти</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userData: {
          email: '',
          password: '',
        },
      };
    },
    methods: {
      async login() {
        // Логика входа пользователя
        try {

          
          console.log('Успешный вход:', this.userData.email);
        } catch (error) {
          // Обработка ошибок входа
          console.error('Ошибка входа:', error);
        }
      },
    },
  };
  </script>
  