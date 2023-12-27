<template>
  <div>
    <h2>Добро пожаловать в систему управления отелем, {{ userName }}</h2>
    <div class="navigation-links">
      <router-link to="/rooms">Комнаты</router-link>
      <router-link to="/clients">Клиенты</router-link>
      <router-link to="/employees">Сотрудники</router-link>
      <button @click="logout">Выйти</button>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    userName() {
      // Здесь мы предполагаем, что у вас есть данные пользователя в состоянии Vuex
      return this.$store.state.user ? this.$store.state.user.username : 'Guest';
    }
  },
  methods: {
    logout() {
      this.$store.commit('clearUser'); // Очищаем данные пользователя в хранилище
      this.$router.push('/login'); // Перенаправляем на страницу входа
    }
  }
};
</script>

<style scoped>
.navigation-links {
  text-align: center;
  margin-bottom: 20px;
}

.navigation-links a {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.navigation-links a:hover {
  color: #007bff;
  text-decoration: underline;
}
</style>
