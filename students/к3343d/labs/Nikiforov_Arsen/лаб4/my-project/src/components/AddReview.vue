<template>
    <div>
      <h2>Добавить отзыв</h2>
      <form @submit.prevent="submitReview">
        <textarea v-model="reviewText" placeholder="Ваш отзыв"></textarea>
        <button type="submit">Отправить</button>
      </form>
    </div>
  </template>
  
  <script>
  import ReviewService from '@/reviewService'; 
  
  export default {
    props: {
      roomId: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        reviewText: ''
      };
    },
    methods: {
      submitReview() {
        const reviewData = {
          text: this.reviewText,
          room: this.roomId
        };
        ReviewService.createReview(reviewData)
          .then(() => {
            alert('Отзыв добавлен');
            this.reviewText = '';
            this.$emit('review-added'); // Отправка события родительскому компоненту
          })
          .catch(error => {
            console.error('Ошибка при добавлении отзыва:', error);
          });
      }
    }
  };
  </script>
  