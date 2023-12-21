<template>
  <div>
    <h2>Список книг</h2>
    <ul>
      <li v-for="book in books" :key="book.id">
        <router-link :to="'/book/' + book.id">
          {{ book.title }} - {{ book.author }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: []
    };
  },
  mounted() {
    this.fetchBooks();
  },
  methods: {
    fetchBooks() {
      axios.get('http://127.0.0.1:8000/books/')
          .then(response => {
            this.books = response.data;
          })
          .catch(error => {
            console.error('Ошибка получения списка книг:', error);
          });
    }
  }
};
</script>

<style scoped>
/* Ваши стили здесь */
</style>
