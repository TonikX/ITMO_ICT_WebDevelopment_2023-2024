<template>
  <div>
    <input type="text" v-model="username" placeholder="Username">
    <input type="password" v-model="password" placeholder="Password">
    <button @click="login">Login</button>
    <p v-if="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios'; // Убедитесь, что axios установлен

export default {
  data() {
    return {
      username: '',
      password: '',
      error: false,
      errorMessage: ''
    };
  },
  methods: {
    login() {
      // Отправляем запрос на сервер для аутентификации
      axios.post('http://localhost:3000/api/auth/login', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        // Предполагаем, что сервер возвращает объект с токеном
        // Токен можно сохранить в localStorage или другом месте
        localStorage.setItem("auth_token", response.data.token);
        localStorage.setItem("username", this.username);
        
        // Перенаправление на страницу профиля
        this.$router.push('/user-profile');
      })
      .catch(error => {
        // Обработка ошибок аутентификации
        this.error = true;
        this.errorMessage = 'Ошибка входа: ' + error.message;
      });
    }
  }
};
</script>
