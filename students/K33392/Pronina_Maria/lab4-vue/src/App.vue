<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import NavBar from '@/components/NavBar.vue';
</script>

<template>
  <NavBar />
  <main>
    <RouterView />
  </main>
</template>


<style scoped>
  main {
    margin-left: 375px;
    width: calc(100vw - 375px);
  }
</style>