<template>
  <div>
    <img alt="Vue logo" src="./assets/logo.png">
    <router-link to="/registration">Регистрация</router-link>
    <router-link to="/login">Вход</router-link>
    <router-link to="/user-profile">Профиль пользователя</router-link>
    <router-view></router-view>
    
    <!-- Добавляем использование RegistrationPage -->
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
