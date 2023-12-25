<template>
  <div>
    <h2>{{ book.title }}</h2>
    <p>by {{ book.author }}</p>
    <p>{{ book.description }}</p>

    <div>
      <button class="styled-button" @click="markAsRead">Read</button>
      <button class="styled-button" @click="markAsWantToRead">Want to Read</button>
    </div>

<!---    <div>
      <label for="rating">Rating:</label>
      <input type="number" v-model="rating" min="1" max="5">
    </div>

    <div>
      <label for="review">Review:</label>
      <textarea v-model="review"></textarea>
    </div>

    <button class="styled-button" @click="submitReview">Submit Review</button>
-->
  </div>

</template>

<style scoped>
.styled-button {
  background-color: #FFFFFF;
  color: #000000;
  padding: 10px 20px;
  border: 1px solid #ddd;
  cursor: pointer;
  border-radius: 7px;
  transition: transform 0.3s;
}
.styled-button:hover {
  transform: scale(1.1);
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      book: {},
      rating: null,
      review: '',
    };
  },
  mounted() {
    this.fetchBookDetails();
  },
  methods: {
    fetchBookDetails() {
      const bookId = this.$route.params.id;
      axios.get(`http://localhost:8000/api/books/${bookId}/`)
        .then(response => {
          this.book = response.data;
        })
        .catch(error => {
          console.error('Error fetching book details:', error);
        });
    },
    updateBookStatus(action) {
        const bookId = this.$route.params.id;
        axios.post(`http://localhost:8000/api/books/${bookId}/update_status/`, {
            action,
            rating: this.rating,
            review: this.review,
        })
            .then(response => {
                this.book = response.data;
            })
            .catch(error => {
                console.error('Error updating book status:', error);
            });
    },
    markAsRead() {
      this.updateBookStatus('mark_as_read');
    },
    markAsWantToRead() {
      this.updateBookStatus('mark_as_want_to_read');
    },
    submitReview() {
      // Implement logic to submit the review
      // You can use this.review and this.rating here
    },
  },
};
</script>

