<template>
  <v-container>
    <h2>Вход в систему</h2>
    <v-form @submit.prevent="loginUser">
      <v-text-field v-model="username" label="Имя пользователя" required></v-text-field>
      <v-text-field v-model="password" label="Пароль" type="password" required></v-text-field>
      <router-link :to="{ name: 'CatalogPage' }">
        <v-btn type="submit" color="primary">Войти</v-btn>
      </router-link>
    </v-form>
  </v-container>
</template>
<script>
import axios from 'axios';

export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    loginUser() {
      const userData = {
        username: this.username,
        password: this.password
      };

      axios.post('http://127.0.0.1:8000/auth/token/login/', userData)
          .then(response => {
            console.log('Успешный вход:', response.data);

            // Делаем что-то после успешного входа, например, сохраняем токен в localStorage
            localStorage.setItem('token', response.data.auth_token);

            // Перенаправляем пользователя на страницу после входа
            this.$router.push({ name: 'CatalogPage' });
          })
          .catch(error => {
            console.error('Ошибка входа:', error);
          });
    }
  }
};
</script>