<template>
  <v-app-bar app color="indigo" dark>
    <v-toolbar-title>Alpinists</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-text-field
        solo-inverted
        flat
        hide-details
        append-icon="mdi-magnify"
        label="Search Routes"
    />
    <v-btn text to="/routes">Routes</v-btn>
    <v-btn text to="/clubs">Clubs</v-btn>
    <v-menu offset-y>
      <template v-slot:activator="{ props }">
        <v-btn text v-bind="props">Account</v-btn>
      </template>
      <v-list>
        <v-list-item v-if="!isAuthenticated" @click="openLoginModal">Login</v-list-item>
        <v-list-item v-if="!isAuthenticated" link to="/register">Register</v-list-item>
        <v-list-item v-if="isAuthenticated" link to="/profile">Profile</v-list-item>
        <v-list-item v-if="isAuthenticated" link to="/ascents">My Ascents</v-list-item>
        <v-list-item v-if="isAuthenticated" @click="logout">Logout</v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>

  <login-modal ref="loginModal"></login-modal>
</template>

<script>
import LoginModal from './LoginModal.vue';

export default {
  name: 'SiteNavbar',
  components: {
    LoginModal,
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
    logout() {
      this.$store.dispatch('logout');
    }
  }
};
</script>
