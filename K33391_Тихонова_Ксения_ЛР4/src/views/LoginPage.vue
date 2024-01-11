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
      const response = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
        username: this.username,
        password: this.password,
      });

      const accessToken = response.data.auth_token;
      
      localStorage.setItem('access_token', accessToken);
      
      console.log('Login successful. Token:', accessToken);
     
      window.location.reload(); 
      window.location.href = '/';
      
      console.log('Login successful. Token:', accessToken);
    } catch (error) {
      console.error('Login failed:', error.response.data);
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
  