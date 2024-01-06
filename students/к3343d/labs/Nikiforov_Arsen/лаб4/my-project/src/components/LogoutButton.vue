<template>
    <button @click="logout">Выход</button>
  </template>
  
  <script>
  import { useStore } from 'vuex';
  import { useRouter } from 'vue-router';
  
  export default {
    setup() {
      const store = useStore();
      const router = useRouter();
  
      const logout = () => {
        store.commit('clearUser'); // Очищаем данные пользователя из Vuex
        router.push('/login'); // Перенаправляем на страницу входа
      };
  
      return { logout };
    }
  };
  </script>
  
  <style scoped>
  button {
    margin: 0 10px;
    text-decoration: none;
    color: #333;
    font-weight: bold;
    cursor: pointer;
  }
  button:hover {
    color: #007bff;
    text-decoration: underline;
  }
  </style>
  