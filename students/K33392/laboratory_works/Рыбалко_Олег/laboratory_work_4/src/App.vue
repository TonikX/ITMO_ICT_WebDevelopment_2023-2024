<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav class="header">
    <RouterLink to="/posts">Posts</RouterLink>
    <RouterLink to="/profile">Profile</RouterLink>
    <RouterLink to="/auth">Auth</RouterLink>
  </nav>
  <RouterView />
</template>

<style scoped>
.header {
  background-color: #ff6600;
  font-weight: 600;
  padding: 5px;
  display: flex;
  gap: 10px;
}
</style>

