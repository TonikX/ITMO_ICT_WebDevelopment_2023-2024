<template>
  <div>
    <h2>Оставить отзыв</h2>
    <form @submit.prevent="submitFeedback">
      <div>
        <label for="room">Комната:</label>
        <select v-model="feedback.room">
          <option v-for="room in rooms" :value="room.id" :key="room.id">{{ room.name }}</option>
        </select>
      </div>
      <div>
        <label for="text">Текст отзыва:</label>
        <textarea v-model="feedback.text"></textarea>
      </div>
      <button type="submit">Отправить</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      feedback: {
        room: '',
        text: ''
      },
      rooms: [] // Массив для хранения списка комнат
    };
  },
  methods: {
    submitFeedback() {
      axios.post('http://localhost:8000/hotel_api/api/reviews/', this.feedback, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('userToken')}`
        }
      })
      .then(() => {
        alert('Отзыв отправлен');
        this.feedback.room = '';
        this.feedback.text = '';
      })
      .catch(error => {
        console.error('Ошибка:', error);
      });
    },
    fetchRooms() {
      axios.get('http://localhost:8000/hotel_api/api/rooms/', {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('userToken')}`
        }
      })
      .then(response => {
        this.rooms = response.data;
      })
      .catch(error => {
        console.error('Ошибка при загрузке комнат:', error);
      });
    }
  },
  created() {
    this.fetchRooms();
  }
};
</script>

<style>
/*  стили */
</style>
