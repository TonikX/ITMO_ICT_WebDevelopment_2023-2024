
<template>
  <body>
  <div id="app">
    <Header :isLoggedIn="isLoggedIn" @logout="logout" />
    <router-view></router-view>
  </div>
</body>
</template>

<script>
import Header from '@/components/HeaderComponent.vue';

export default {
  data() {
    return {
      isLoggedIn: false,
    };
  },
  created() {
    this.isLoggedIn = localStorage.getItem('access_token') !== null;
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      this.isLoggedIn = false;
      window.location.reload(); 
      window.location.href = '/';
    },
  },
  components: {
    Header,
  },
};
</script>

<style>

#app {
  font-family: 'Raleway', sans-serif;
  text-align: center;
  color: #000000;
}

body { 
  margin: 0;
  padding: 0;
  height: 100vh;  background: linear-gradient(to left, #d0ffbc, #96ac9a);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
}

</style>
