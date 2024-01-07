<template>
    <div>
      <h1>User Information</h1>
      <div v-if="user">
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>ID:</strong> {{ user.id }}</p>
        <p><strong>Username:</strong> {{ user.username }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
  
      <!-- Добавим кнопку для перехода на главную страницу -->
      <router-link to="/MainPage" class="back-button">
        Back to Main Page
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        user: null,
      };
    },
    mounted() {
      // Проверяем наличие токена перед загрузкой информации о пользователе
      const accessToken = localStorage.getItem('access_token');
      if (!accessToken) {
        // Если токен отсутствует, перенаправляем на страницу авторизации
        this.$router.push({ name: 'Auth' });
        return;
      }
  
      // Отправляем GET-запрос для получения информации о пользователе
      axios.get('http://127.0.0.1:8000/auth/users/me', {
        headers: {
          Authorization: `Token ${accessToken}`,
        },
      })
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          console.error('Error fetching user information:', error);
        });
    },
  };
  </script>
  
  <style scoped>
  /* Твои стили компоненты, если нужны */
  </style>
  