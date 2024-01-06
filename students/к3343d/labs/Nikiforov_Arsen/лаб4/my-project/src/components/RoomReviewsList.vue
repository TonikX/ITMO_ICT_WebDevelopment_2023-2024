<template>
  <div>
    <h2>Отзывы о комнате {{ roomId }}</h2>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        {{ review.text }} - {{ review.author }}
      </li>
    </ul>
    <router-link :to="`/room/${roomId}/add-review`">Добавить отзыв</router-link>
  </div>
</template>

<script>
import axios from 'axios';

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
      axios.get(`http://localhost:8000/hotel_api/api/rooms/${this.roomId}/reviews`, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('userToken')}` //  метод авторизации
        }
      })
        .then(response => {
          this.reviews = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении отзывов:', error);
        });
    }
  },
  created() {
    this.fetchReviews();
  }
};
</script>
