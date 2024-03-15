<template>
  <v-btn v-if="auth" @click="home()" text><span class="mr-2">Домашняя страница</span></v-btn>
  <v-spacer></v-spacer>
  <v-btn v-if="auth" @click="navigateToAccount()" text> Личный кабинет</v-btn>
  <v-btn v-if="auth" @click="logout()" text><span class="mr-2">Выйти</span></v-btn>
</template>

<script>
export default {
  name: 'AllBooks',
  computed: {
    auth() {
      let auth;
      if (localStorage.auth_token) {
        auth = true
      }
      return auth
    }
  },
  methods: {
    logout() {
      this.$router.push({name: 'Login'})
    },
    home() {
      this.$router.push({name: 'Home'})
    },
    navigateToAccount() {
      this.$router.push({name: 'Manager'})
    }
  }
}
</script>
