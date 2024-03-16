<template>
  <main class="container-fluid w-auto align-items-center row vh-100">
    <div>
      <h1>Добро пожаловать!</h1>
      <div v-if="loggedOut" class="align-content-center">
        <router-link to="/login" class="navbar-brand">Войти</router-link>
        |
        <router-link to="/register" class="navbar-brand">Зарегистрироваться</router-link>
      </div>
    </div>
  </main>
</template>

<script setup>
import {computed} from "vue";

const loggedOut = computed(() => {
  return localStorage.getItem('access_token') === '';
});
</script>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>

</style>