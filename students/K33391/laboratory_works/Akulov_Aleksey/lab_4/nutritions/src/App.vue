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
  return route.path !== '/login' && route.path !== '/register';
});
</script>

<style scoped>
.main-container {
  display: flex;
  justify-content: space-between; /* Adjust as needed */
  padding: 20px;
}

.recipe-container, .form-container {
  flex: 1;
  padding: 10px;
}
</style>
