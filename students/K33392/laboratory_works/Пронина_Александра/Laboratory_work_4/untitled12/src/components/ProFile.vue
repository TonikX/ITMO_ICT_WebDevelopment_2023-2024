<template>
  <v-container>
    <h2>Профиль пользователя</h2>
    <v-form @submit.prevent="updateProfile">
      <!-- Поля для изменения данных пользователя -->
      <v-text-field v-model="username" label="Имя пользователя" required></v-text-field>
      <v-text-field v-model="email" label="Email" required></v-text-field>
      <v-text-field v-model="name" label="Имя" required></v-text-field>
      <v-btn type="submit" color="primary">Сохранить изменения</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ProFile',
  data() {
    return {
      username: '',
      email: '',
      name: ''
    };
  },
  methods: {
    updateProfile() {
      const userData = {
        username: this.username,
        email: this.email,
        name: this.name
      };

      // Отправка запроса на изменение данных пользователя на бэкэнд
      axios.patch('/api/profile/', userData) // Замените на ваш URL для изменения профиля
          .then(response => {
            console.log('Данные пользователя обновлены:', response.data);
            // Логика при успешном обновлении профиля
          })
          .catch(error => {
            console.error('Ошибка при обновлении профиля:', error);
            // Логика при ошибке обновления профиля
          });
    },
    getUserData() {
      // Получение данных пользователя с бэкэнда
      axios.get('http://127.0.0.1:8000/profile/') // Замените на ваш URL для получения профиля
          .then(response => {
            const userData = response.data;
            this.username = userData.username;
            this.email = userData.email;
            this.name = userData.name;
          })
          .catch(error => {
            console.error('Ошибка при получении данных пользователя:', error);
          });
    }
  },
  created() {
    // При создании компонента получаем данные пользователя
    this.getUserData();
  }
};
</script>
