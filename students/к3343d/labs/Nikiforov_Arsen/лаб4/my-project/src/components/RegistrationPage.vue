<!-- src/components/RegistrationForm.vue -->

<template>
    <div>
      <h2>Регистрация</h2>
      <form @submit.prevent="register">
        <label for="username">Имя пользователя:</label>
        <input type="text" id="username" v-model="userData.username" required>
  
        <label for="email">Электронная почта:</label>
        <input type="email" id="email" v-model="userData.email" required>
  
        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="userData.password" required>
  
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </template>
  
  <script>
  import { registerUser } from '@/api/auth.js';
  
  export default {
    data() {
      return {
        userData: {
          username: '',
          email: '',
          password: '',
        },
      };
    },
    methods: {
      async register() {
        try {
          const response = await registerUser(this.userData);
          console.log('Успешно зарегистрирован:', response.data);
          
        } catch (error) {
          console.error('Ошибка регистрации:', error);
          
        }
      },
    },
  };
  </script>
  