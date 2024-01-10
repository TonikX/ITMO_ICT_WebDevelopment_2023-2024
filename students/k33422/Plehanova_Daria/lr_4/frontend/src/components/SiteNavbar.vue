<template>
  <v-app-bar app color="indigo" dark>
    <v-toolbar-title>
      <router-link style="text-decoration: none; color: inherit;" to="/">Alpinists</router-link>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn text to="/routes">Routes</v-btn>
    <v-btn text to="/clubs">Clubs</v-btn>
    <v-menu offset-y>
      <template v-slot:activator="{ props }">
        <v-btn text v-bind="props">Account</v-btn>
      </template>
      <v-list>
        <v-list-item v-if="!isAuthenticated" @click="openLoginModal">Login</v-list-item>
        <v-list-item v-if="!isAuthenticated" @click="openRegisterModal">Register</v-list-item>
        <v-list-item v-if="isAuthenticated" @click="logout">Logout</v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>

  <login-modal ref="loginModal"></login-modal>
  <register-modal ref="registerModal"></register-modal>
</template>

<script>
import LoginModal from './LoginModal.vue';
import RegisterModal from "@/components/RegisterModal.vue";

export default {
  name: 'SiteNavbar',
  components: {
    LoginModal,
    RegisterModal
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    openLoginModal() {
      this.$refs.loginModal.dialog = true;
    },
    openRegisterModal() {
      this.$refs.registerModal.dialog = true;
    },
    logout() {
      this.$store.dispatch('logout');
    }
  }
};
</script>
