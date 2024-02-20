<template>
    <div class="container">
      <h2>Зарегистрироваться</h2>
      <form @submit.prevent="registerUser">
        <label for="username">Имя пользователя:</label>
        <input type="text" v-model="username" required />
  
        <label for="email">Электронная почта:</label>
        <input type="email" v-model="email" required />
  
        <label for="password">Пароль:</label>
        <input type="password" v-model="password" required />
  
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
      };
    },
    methods: {
      async registerUser() {
        try {
          const response = await axios.post('http://localhost:8000/auth/users/', {
            username: this.username,
            email: this.email,
            password: this.password,
          });
  
          console.log('User registered successfully:', response.data);
          this.$router.push('/login');
        } catch (error) {
          console.error('Registration failed:', error.response.data);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
  }
  
  h2 {
    color: #333;
    font-size: 2em;
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  label {
    margin-bottom: 5px;
  }
  
  input {
    margin-bottom: 10px;
    padding: 10px;
    font-size: 1em;
  }
  
  button {
    background-color: #3bbc55;
    color: #ffffff;
    padding: 10px;
    border: none;
    cursor: pointer;
    font-size: 1em;
    border-radius: 4px;
  }
  </style>
  