<template>
  <div>
    <h2>Favorites</h2>
    <!-- Display user's favorite books -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name:'FavoRites',
  data() {
    return {
      favoriteBooks: []
    };
  },
  mounted() {
    this.fetchFavoriteBooks();
  },
  methods: {
    fetchFavoriteBooks() {
      axios.get('http://127.0.0.1:8000/favorites/')
          .then(response => {
            this.favoriteBooks = response.data;
          })
          .catch(error => {
            console.error('Error fetching favorite books:', error);
          });
    }
  }
};
</script>

<!-- Стили для компонента Favorites.vue -->
<style scoped>
/* Your styles here */
</style>
