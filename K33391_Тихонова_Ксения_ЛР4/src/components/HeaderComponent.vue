<template>
  <header>
    <h1 class="logo">WEBZoo</h1>
    <nav>
      <router-link to="/" class="nav-link" :class="{ 'active': $route.path === '/' }">Главная страница</router-link>
      <router-link v-if="!isLoggedIn" to="/login" class="nav-link" :class="{ 'active': $route.path === '/login' }">Войти</router-link>
      <router-link v-if="!isLoggedIn" to="/register" class="nav-link" :class="{ 'active': $route.path === '/register' }">Зарегистрироваться</router-link>
      <router-link v-if="isLoggedIn" to="/profile" class="nav-link" :class="{ 'active': $route.path === '/profile' }">Профиль</router-link>
      <router-link v-if="isLoggedIn" to="/animals" class="nav-link" :class="{ 'active': $route.path === '/animals' }">Животные</router-link>
      <router-link v-if="isLoggedIn" to="/locations" class="nav-link" :class="{ 'active': $route.path === '/locations' }">Места</router-link>
      <router-link v-if="isLoggedIn" to="/shop" class="nav-link" :class="{ 'active': $route.path === '/shop' }">Магазин</router-link>
      <router-link v-if="isLoggedIn" to="/other-zoos" class="nav-link" :class="{ 'active': $route.path === '/other-zoos' }">Другие зоопарки</router-link>
      <button v-if="isLoggedIn" @click="logout" class="logout-button">Выйти</button>
    </nav>
  </header>
</template>

<script>
export default {
  props: {
    isLoggedIn: Boolean,
  },
  methods: {
    logout() {
      this.$emit('logout');
    },
  },
  
};

</script>

<style scoped>


header {
  background-color: #3bbc55;
  color: #f8fa87;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  margin: 0;
}

nav {
  display: flex;
}

.nav-link {
  text-decoration: none;
  color: #000000;
  font-size: 1.2em;
  padding: 10px;
  border: none;
  cursor: pointer;
  font-size: 1.2em;
  border-radius: 4px;
  margin-left: 10px;
  transition: color 0.3s;
}

.nav-link:hover,
.active {
  text-decoration: underline;
  color: #f8fa87;
}

.logout-button {
  background-color: #3bbc55;
  color: #000000;
  padding: 10px;
  border: none;
  cursor: pointer;
  font-size: 1.2em;
  border-radius: 4px;
  margin-left: 10px;
  transition: color 0.3s;

}

.logout-button:hover {
  color: #f8fa87;
  text-decoration: underline;

}
</style>
