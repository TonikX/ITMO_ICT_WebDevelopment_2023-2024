<template>
  <div>
    <h2>Favorites</h2>
    <!-- Display user's favorite books -->
    <ul>
      <li v-for="book in favoriteBooks" :key="book.id">
        {{ book.title }} by {{ book.author }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name:'FavoritePage',
  data() {

    return {
      favoriteBooks: []
    };
  },
  mounted() {
    this.fetchFavoriteBooks(); // Вызываем метод для получения избранных книг при монтировании компонента
  },
  methods: {
    fetchFavoriteBooks() {
      // Здесь нужно изменить URL запроса на ваш эндпоинт для получения избранных книг
      axios.get('http://127.0.0.1:8000/favorites/')
          .then(response => {
            this.favoriteBooks = response.data; // Обновляем список избранных книг
          })
          .catch(error => {
            console.error('Ошибка при получении избранных книг:', error);
          });
    }
  }
};
</script>

<style>
/* Стили для компонента Favorites.vue */
</style>
