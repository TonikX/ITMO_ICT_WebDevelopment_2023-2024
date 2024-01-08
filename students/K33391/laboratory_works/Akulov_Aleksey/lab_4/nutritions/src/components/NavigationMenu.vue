<template>
  <nav>
    <ul>
      //<li><router-link to="/">Главная</router-link></li>
      <li><router-link to="/ingredients">Ингридиенты</router-link></li>
      <li><button @click="logout">Выйти</button></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'NavigationMenu',
  methods: {
    logout() {
      localStorage.removeItem('authToken');
      this.$router.push('/login');
    }
  }
}
</script>

<style scoped>
nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 10px;
}
</style>
