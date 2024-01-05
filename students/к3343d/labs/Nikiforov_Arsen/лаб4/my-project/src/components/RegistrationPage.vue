<template>
  <div class="app-container">
    <img alt="Vue logo" src="@/assets/logo.png" class="logo">
    <div class="menu" v-if="showButtons">
      <h1>Добро пожаловать в наш отель!</h1>
      <button @click="showComponent = 'login'">Вход</button>
      <button @click="showComponent = 'registration'">Регистрация</button>
    </div>
    <LoginPage v-if="showComponent === 'login'" @show-user-profile="showUserProfile" />
    <RegistrationPage v-if="showComponent === 'registration'" />
    <UserProfile v-if="showComponent === 'userProfile'" @go-back="showMainButtons" />
  </div>
</template>

<script>
import RegistrationPage from '@/components/RegistrationPage.vue';
import LoginPage from '@/components/LoginPage.vue';
import UserProfile from '@/components/UserProfile.vue';

export default {
  name: 'App',
  components: {
    RegistrationPage,
    LoginPage,
    UserProfile
  },
  data() {
    return {
      showComponent: null,
      showButtons: true,
    };
  },
  methods: {
    showUserProfile() {
      this.showComponent = 'userProfile';
      this.showButtons = false;
    },
    showMainButtons() {
      this.showComponent = null;
      this.showButtons = true;
    }
  }
};
</script>

<style scoped>
.app-container {
  text-align: center;
  background: linear-gradient(to right, #b4ffb0, #b19dff); 
  min-height: 100vh;
}

.logo {
  max-width: 150px;
  margin: 20px auto;
}

.menu h1 {
  color: #fff;
  text-shadow: 2px 2px 4px #000;
}

.menu {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
  margin-bottom: 20px;
}

button {
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0056b3;
}
</style>