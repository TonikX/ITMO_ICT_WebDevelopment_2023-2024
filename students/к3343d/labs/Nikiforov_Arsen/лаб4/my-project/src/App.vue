<template>
  <div class="app-container">
    <img alt="Vue logo" src="./assets/logo.png" class="logo">
    <div class="menu">
      <h1>Добро пожаловать в наш отель!</h1>
      <button @click="showComponent = 'login'">Вход</button>
      <button @click="showComponent = 'registration'">Регистрация</button>
    </div>
    <component v-if="showComponent" :is="currentComponent"></component>
  </div>
</template>

<script>
import RegistrationPage from './components/RegistrationPage.vue';
import LoginPage from './components/LoginPage.vue';

export default {
  name: 'App',
  data() {
    return {
      showComponent: null
    };
  },
  computed: {
    currentComponent() {
      switch (this.showComponent) {
        case 'login': return LoginPage;
        case 'registration': return RegistrationPage;
        default: return null;
      }
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
  max-width: 220px;
  margin: 20px auto;
  height: auto;
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
