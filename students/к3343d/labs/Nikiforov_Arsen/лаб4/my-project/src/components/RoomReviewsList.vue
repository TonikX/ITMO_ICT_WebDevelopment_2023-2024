<template>
    <div>
      <h2>Отзывы о комнате {{ roomId }}</h2>
      <ul>
        <li v-for="review in reviews" :key="review.id">
          {{ review.text }} - {{ review.author }}
          <button @click="deleteReview(review.id)">Удалить</button>
        </li>
      </ul>
      <router-link :to="`/room/${roomId}/add-review`">Добавить отзыв</router-link>
    </div>
  </template>
  
  <script>
  import ReviewService from '@/reviewService.js'; // Убедитесь, что путь к файлу reviewService.js верный
  
  export default {
    props: {
      roomId: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        reviews: []
      };
    },
    methods: {
      fetchReviews() {
        ReviewService.getAllReviews()
          .then(response => {
            this.reviews = response.data;
          })
          .catch(error => {
            console.error('Ошибка при получении отзывов:', error);
          });
      },
      deleteReview(reviewId) {
        ReviewService.deleteReview(reviewId)
          .then(() => {
            alert('Отзыв удален');
            this.fetchReviews(); // Обновление списка отзывов после удаления
          })
          .catch(error => {
            console.error('Ошибка при удалении отзыва:', error);
          });
      }
    },
    created() {
      this.fetchReviews();
    }
  };
  </script>
  