<template>
  <div>
    <h2>Book Catalog</h2>
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
  name: 'CatalogPage',
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
      axios.get('http://localhost:8080/db.json') // Путь к вашему db.json относительно корня проекта
          .then(response => {
            this.books = response.data.books; // Предполагая, что массив книг находится в свойстве books файла db.json
          })
          .catch(error => {
            console.error('Ошибка при получении списка книг:', error);
          });
    }
  }
};
</script>

<style scoped>
/* Ваши стили здесь */
</style>
