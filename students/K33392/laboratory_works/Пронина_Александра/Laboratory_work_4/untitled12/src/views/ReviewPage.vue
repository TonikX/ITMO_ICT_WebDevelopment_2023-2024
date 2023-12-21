<template>
  <div>
    <h2>Review Form</h2>
    <div v-if="reviews.length > 0">
      <h3>Reviews:</h3>
      <ul>
        <li v-for="(review, index) in reviews" :key="index">{{ review.text }}</li>
      </ul>
    </div>
    <form @submit.prevent="submitReview">
      <textarea v-model="newReview" rows="4" cols="50" placeholder="Enter your review"></textarea>
      <button type="submit">Submit Review</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "ReviewForm",
  data() {
    return {
      reviews: [],
      newReview: ''
    };
  },
  mounted() {
    // Выполнение запроса к бэкэнду при загрузке компонента
    this.fetchReviews();
  },
  methods: {
    fetchReviews() {
      // Запрос к бэкэнду для получения списка отзывов
      axios.get('/reviews/') // Замените на ваш эндпоинт для получения списка отзывов
          .then(response => {
            this.reviews = response.data;
          })
          .catch(error => {
            console.error('Error fetching reviews:', error);
          });
    },
    submitReview() {
      // Отправка нового отзыва на бэкэнд
      axios.post('/reviews/', { text: this.newReview }) // Замените на ваш эндпоинт для создания отзыва
          .then(() => {
            // Обновление списка отзывов после успешной отправки
            this.fetchReviews();
            this.newReview = ''; // Очистка поля ввода
          })
          .catch(error => {
            console.error('Error submitting review:', error);
          });
    }
  }
};
</script>

<style scoped>
/* Здесь можете добавить стили по своему усмотрению */
</style>
