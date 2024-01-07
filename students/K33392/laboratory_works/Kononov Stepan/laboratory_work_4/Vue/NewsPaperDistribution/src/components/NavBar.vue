<template>
  <nav class="navbar navbar-expand-lg">
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav mx-auto">
        <li class="nav-item">
          <router-link to="/profile" class="nav-link">Профиль</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/newspapers" class="nav-link">Газеты</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/printing_house" class="nav-link">Типографии</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/post_offices" class="nav-link">Почтовые отделения</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/print_runs" class="nav-link">Тиражи</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/post_arrivals" class="nav-link">Поступления</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
</style>
<script setup>
</script>