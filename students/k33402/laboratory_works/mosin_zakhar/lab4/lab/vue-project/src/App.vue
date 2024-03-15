<template>
  <div id="app" class="web-1-0">
    <Navbar />
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>

<style>
#app {
  background-color: #001b68;
  min-height: 768px;
  margin: 0 auto;
  padding: 2rem;
  font-weight: normal;
}
.web-1-0 {
  background-color: #001b68; /* Bright yellow */
  font-family: Comic Sans MS, cursive, sans-serif;
  color: #00ffcc; /* Bright red */
}
</style>
