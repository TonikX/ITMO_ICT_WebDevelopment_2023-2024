<template>
  <v-app>
    <v-app-bar app color="primary">
      <v-toolbar-title>Книжный магазин</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn v-if="isAuthenticated" @click="logout">Выход</v-btn>
      <v-btn v-else to="/auth/token/login/">Войти</v-btn>
    </v-app-bar>

    <v-main>
      <!-- Ваш основной контент здесь -->
      <router-view></router-view>
    </v-main>

    <v-footer app color="primary">
      <!-- Нижний колонтитул, если необходим -->
    </v-footer>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      isAuthenticated: false
    };
  },
  methods: {
    logout() {
      axios.post('http://127.0.0.1:8000/auth/logout/') // Маршрут для выхода из системы
          .then(() => {
            console.log('Вы успешно вышли из системы');
            this.isAuthenticated = false; // Установка значения аутентификации как false после выхода
          })
          .catch(error => {
            console.error('Ошибка при выходе из системы', error);
          });
    }
    // Другие методы для работы с вашим API (регистрация, вход в систему и т.д.)
  }
  // Вам также потребуется добавить логику для аутентификации и маршрутов
}
</script>

<style>
/* Добавьте свои стили здесь */
</style>
