<template>
  <nav class="navbar container-fluid p-2 m-auto flex-row vw-100">
      <router-link to="/" class="navbar-brand">Главная</router-link>
      <router-link to="/ingredients" class="navbar-brand">Ингридиенты</router-link>
      <router-link to="/recipes" class="navbar-brand">Рецепты</router-link>
      <router-link  to="/login"  class="navbar-brand" @click="logout">Выйти</router-link>
  </nav>
</template>

<script>
import router from "@/router/index.js";

export default {
  name: 'NavigationMenu',
  methods: {
    logout() {
      console.log('Token before logout:', localStorage.getItem('access_token'));
      localStorage.removeItem('access_token');
      console.log('Token after logout:', localStorage.getItem('access_token'));
      router.push('/login');
    }
  }
}
</script>
