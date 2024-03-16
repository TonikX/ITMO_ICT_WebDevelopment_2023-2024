<template>
  <div class="container-fluid justify-content-center row d-flex vw-100">
    <navigation-menu v-if="showHeader"/>
    <RouterView/>
  </div>
</template>

<script setup>
import NavigationMenu from "@/components/NavigationMenu.vue";
import {useRoute} from "vue-router";
import {computed} from "vue";

const route = useRoute();

const showHeader = computed(() => {
  return route.path !== '/login' && route.path !== '/register';
});
</script>

<style scoped>
nav {
  background: #3bbc55;
}
</style>