<template>
  <v-app-bar>
    <MenuComponent />
    <v-spacer></v-spacer>
    <v-btn v-if="!isLoggedIn" @click="$goTo('/login')">Вход</v-btn>
    <v-btn v-if="!isLoggedIn" @click="$goTo('/register')" class="ml-2">Регистрация</v-btn>
    <v-btn v-if="isLoggedIn" @click="$goTo('/profile')">Профиль</v-btn>
    <v-btn v-if="isLoggedIn" @click="logout" class="ml-2">Выйти</v-btn>
  </v-app-bar>
</template>

<script>
import axios from 'axios';
import MenuComponent from './MenuComponent.vue';

export default {
  components: {
    MenuComponent,
  },
  methods: {
    logout() {
      const token = localStorage.getItem('token');
      if (token) {
        const headers = { Authorization: `Token ${token}` };
        axios.post(this.$websiteURL + '/auth/token/logout/', null, { headers })
          .then(() => {
            localStorage.removeItem('token');
            window.location.reload();
          })
          .catch(error => {
            console.error('Logout error:', error);
          });
      } else {
        console.warn('No token found. User might not be authenticated.');
      }
    },
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('token');
    },
  },
};
</script>
