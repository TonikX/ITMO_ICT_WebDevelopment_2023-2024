<template>
  <div>
    <img alt="Vue logo" src="./assets/logo.png">
    <nav class="navigation-links">
      <router-link to="/registration">Регистрация</router-link>
      <router-link to="/login">Вход</router-link>
      <router-link to="/user-profile">Профиль пользователя</router-link>
    </nav>
    <router-view></router-view>
    <RegistrationPage />
  </div>
</template>

<script>
import RegistrationPage from './components/RegistrationPage.vue';

export default {
  name: 'App',
  components: {
    RegistrationPage,
  },
};
</script>

<style scoped>
.navigation-links {
  /* Стили для контейнера навигационных ссылок */
  text-align: center;
  margin-bottom: 20px;
}

.navigation-links a {
  /* Стили для самих ссылок */
  margin: 0 10px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.navigation-links a:hover {
  /* Стили для ссылок при наведении */
  color: #007bff;
  text-decoration: underline;
}
</style>
