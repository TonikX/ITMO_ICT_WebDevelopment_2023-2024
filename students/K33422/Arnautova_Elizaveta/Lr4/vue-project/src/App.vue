<template>
  <header>
    <div>
      <a v-if="!auth" href="/">Home </a>
      <a v-else href="/userpage">Home </a>

      <RouterLink to="/alp/climbers"> Сlimbers </RouterLink>
      <RouterLink to="/alp/mountains"> Mountains </RouterLink>
      <RouterLink to="/alp/ascensions"> Ascensions </RouterLink>
      <RouterLink to="/alp/clubs"> Clubs </RouterLink>
      <RouterLink to="/alp/groups"> Groups </RouterLink>

      <a class="black" v-if="!auth" @click="goLogin"> Login</a>
      <a class="black" v-else @click="logout"> Logout</a>

      <RouterView />
    </div>

  </header>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<script>
import VSpoiler from 'v-spoiler';
import 'v-spoiler/dist/v-spoiler.css';
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("token")) {
        return true
      }
    }
  },
  methods: {
    goLogin() {
      this.$router.push({name: "Login"})
    },
    logout() {
      sessionStorage.removeItem("token")
      window.location = '/home'
    }
  },
  components: {
    VSpoiler
  }
}
</script>
<style scoped>
header {
  line-height: 1.5;
  max-height: 150vh;
  text-align: center;
}
a {
  font-size: 30px;
  background-color: white;
}

a:hover {
  font-size: 30px;
  background-color: #04AA6D;
  color: white;
}

.black
{
  font-size: 30px;
  color: #23684f;
}
</style>