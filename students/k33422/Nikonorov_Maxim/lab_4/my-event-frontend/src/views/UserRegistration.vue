<template>
    <div>
      <h1>Регистрация</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">Логин:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div>
          <label for="FirstName">FirstName</label>
          <input type="text" id="FirstName" v-model="FirstName" required>
        </div>
        <div>
          <label for="LastName">LastName</label>
          <input type="text" id="LastName" v-model="LastName" required>
        </div>
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div>
          <label for="password">Пароль:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </template>
  
  <script>
import axios from 'axios';

export default {
  name: 'UserRegistration',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      LastName: '',
      FirstName: '',
    };
  },
  methods: {
    register() {
      axios.post('http://localhost:8000/auth/users/create/', {
        username: this.username,
        email: this.email,
        password: this.password,
        LastName: this.LastName,
        FirstName: this.FirstName,

      })
      .then(response => {
        console.log('Успешная регистрация:', response.data);
        
        this.$router.push({ name: 'EventHome' });
      })
      .catch(error => {
        console.error('Ошибка регистрации:', error.response.data);
        
      });
    },
  },
};
</script>
