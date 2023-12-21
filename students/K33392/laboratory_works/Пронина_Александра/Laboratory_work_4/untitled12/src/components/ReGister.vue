<template>
  <v-container>
    <h2>Регистрация нового пользователя</h2>
    <v-form @submit.prevent="registerUser">
      <v-text-field v-model="username" label="Имя пользователя" required></v-text-field>
      <v-text-field v-model="password" label="Пароль" type="password" required></v-text-field>
      <v-text-field v-model="email" label="Email" required></v-text-field>
      <v-text-field v-model="name" label="Имя" required></v-text-field>
      <v-btn type="submit" color="primary">Зарегистрироваться</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ReGister',
  data() {
    return {
      username: '',
      password: '',
      email: '',
      name: ''
    };
  },
  methods: {
    registerUser() {
      const userData = {
        username: this.username,
        password: this.password,
        email: this.email,
        name: this.name
      };

      // Отправляем запрос на регистрацию пользователя на бэкэнд
      axios.post('http://127.0.0.1:8000/register/', userData) // Замените URL на ваш роут для регистрации пользователя
          .then(response => {
            console.log('Пользователь успешно зарегистрирован:', response.data);

            this.$router.push({ name: 'CatalogPage' });
          })
          .catch(error => {
            console.error('Ошибка при регистрации пользователя:', error);
            // Логика при ошибке регистрации
            this.$router.push({ name: 'CatalogPage' });
          });
    }
  }
};
</script>

<style scoped>
/* Стили для компонента ReGister.vue */
</style>
