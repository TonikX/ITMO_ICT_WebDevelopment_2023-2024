<template>
    <div class="registration-container">
      <h2>Registration</h2>
      <form @submit.prevent="register">
        <label for="newUsername">New Username:</label>
        <input v-model="newUsername" type="text" id="newUsername" required />
  
        <label for="newPassword">New Password:</label>
        <input v-model="newPassword" type="password" id="newPassword" required />
  
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Registration',
    data() {
      return {
        newUsername: '',
        newPassword: '',
      };
    },
    methods: {
      async register() {
        try {
          // Отправляем запрос на регистрацию
          const response = await axios.post('http://127.0.0.1:8000/auth/users/', {
            username: this.newUsername,
            password: this.newPassword,
          }, {
            headers: {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
            },
          });
  
          // При успешной регистрации выводим сообщение (можно изменить)
          alert('Registration successful!');
  
          // Перенаправляем на страницу авторизации
          this.$router.push({ name: 'Auth' }).catch(() => {}); // Обрабатываем возможные ошибки
        } catch (error) {
          // Выводим сообщение об ошибке (можно изменить)
          alert('Registration failed. Please try again.');
          console.error(error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .registration-container {
    width: 200%;
    max-width: 400px;
    margin: 0 auto;
    text-align: center;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .registration-container h2 {
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  label {
    margin-bottom: 5px;
  }
  
  input {
    margin-bottom: 10px;
    padding: 10px;
    box-sizing: border-box;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  button {
    cursor: pointer;
    background-color: #3498db;
    color: #fff;
    border: none;
    padding: 20px;
    border-radius: 30px;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #1e6ea9;
  }
  </style>
  