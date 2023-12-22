<script setup>
import { computed } from 'vue'; 
import { useRoute } from 'vue-router';
import Header from "@/components/Header.vue";

const route = useRoute();

const showHeader = computed(() => route.path !== '/registerpatient' && route.path !== '/enterpatient' && route.path !== '/home');
</script>

<template>
  <header v-if="showHeader"> 
    <Header />
  </header>

  <RouterView />
</template>

<style scoped>
</style>