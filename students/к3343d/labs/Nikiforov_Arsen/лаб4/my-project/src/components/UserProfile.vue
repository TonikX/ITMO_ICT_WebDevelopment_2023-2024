<template>
  <div>
    <h2>Профиль пользователя</h2>
    <div v-if="user">
      <p><strong>Имя пользователя:</strong> {{ user.username }}</p>
      <!-- Другие данные пользователя -->
      <p>Welcome to the Hotel Management System</p>
    <button @click="logout">Logout</button>
    </div>
  </div>
</template>

<script>
import { state } from '@/store';

export default {
  computed: {
    user() {
      return state.user;
    },
  },
};
</script>
