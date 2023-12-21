<template>
  <div>
    <h2>Book Detail</h2>
    <h3>{{ book.title }}</h3>
    <p>Author: {{ book.author }}</p>
    <p>Price: {{ book.price }}</p>
    <!-- Other book details -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      book: {}
    };
  },
  mounted() {
    this.fetchBookDetails();
  },
  methods: {
    fetchBookDetails() {
      const bookId = this.$route.params.id;
      axios.get(`http://127.0.0.1:8000/books/${bookId}/`)
          .then(response => {
            this.book = response.data;
          })
          .catch(error => {
            console.error('Error fetching book details:', error);
          });
    }
  }
};
</script>

<!-- Стили для компонента BookDetail.vue -->
<style scoped>
/* Your styles here */
</style>
