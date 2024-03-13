<template>
  <v-app-bar app color="deep-orange darken-1" dark>
    <v-toolbar-title>
      <router-link to="/" style="text-decoration: none; color: white;">
        Клубы Восхождения
      </router-link>
    </v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn text to="/routes" class="text-capitalize white--text">
      Маршруты
    </v-btn>
    <v-btn text to="/clubs" class="text-capitalize white--text">
      Клубы
    </v-btn>
    <v-menu offset-y>
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props">Аккаунт</v-btn>
      </template>
      <v-list>
        <v-list-item v-if="!isAuthenticated" @click="openLoginModal">Login</v-list-item>
        <v-list-item v-if="!isAuthenticated" @click="openRegisterModal">Register</v-list-item>
        <v-list-item v-if="isAuthenticated" @click="logout">Logout</v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>

  <!-- Модальные окна для входа и регистрации -->
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

<style>
.v-app-bar {
  background-color: #D84315 !important;
}

.v-btn {
  margin-right: 10px;
}

.router-link-active {
  font-weight: bold;
  color: #FFCCBC !important;
}
</style>