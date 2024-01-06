<template>
  <div>
    <h2>Добавить общий отзыв</h2>
    <form @submit.prevent="submitReview">
      <label for="reviewText">Отзыв:</label>
      <textarea id="reviewText" v-model="reviewText" placeholder="Введите ваш отзыв"></textarea>
      
      <button type="submit">Отправить</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      reviewText: ''
    };
  },
  computed: {
    username() {
      // Получение имени пользователя из состояния Vuex
      return this.$store.state.user ? this.$store.state.user.username : 'Аноним';
    }
  },
  methods: {
    submitReview() {
      const reviewData = {
        author: this.username, // Использование имени пользователя из Vuex
        text: this.reviewText
      };

      axios.post('http://localhost:8000/hotel_api/api/reviews/', reviewData, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('userToken')}`
        }
      })
      .then(() => {
        alert('Отзыв успешно добавлен!');
        this.reviewText = ''; // Очистка поля ввода после отправки отзыва
      })
      .catch(error => {
        console.error('Ошибка при добавлении отзыва:', error);
      });
    }
  }
};
</script>
