<template>
  <div id="app">
    <header v-if="showHeader">
      <NavigationMenu />
    </header>

    <RouterView />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import NavigationMenu from "@/components/NavigationMenu.vue";

const route = useRoute();

const showHeader = computed(() => {
  return route.path !== '/login' && route.path !== '/register' && route.path !== '/some-other-path';
});
</script>

<style scoped>
/* Здесь вы можете добавить стили для header или другие глобальные стили */
</style>
