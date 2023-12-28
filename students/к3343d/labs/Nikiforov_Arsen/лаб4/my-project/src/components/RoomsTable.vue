<template>
  <div class="rooms-container">
    <h2>Список номеров</h2>
    <div class="room" v-for="room in rooms" :key="room.id">
      <h3>Номер: {{ room.id }}</h3>
      <p>Тип: {{ room.room_type }}</p>
      <p>Этаж: {{ room.floor }}</p>
      <p>Стоимость: {{ room.cost }}</p>
      <button v-if="room.is_available" @click="bookRoom(room.id)">Забронировать</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rooms: [] // Предполагается, что это массив комнат
    };
  },
  methods: {
    async bookRoom(roomId) {
      try {
        const response = await this.$axios.post(`http://localhost:8000/book_room/${roomId}`);
        if (response.data.status === 'booked') {
          // Обновление состояния комнаты после успешного бронирования
          this.updateRoomStatus(roomId, false);
        }
      } catch (error) {
        console.error('Ошибка при бронировании: ', error);
      }
    },
    updateRoomStatus(roomId, isAvailable) {
      const room = this.rooms.find(r => r.id === roomId);
      if (room) {
        room.is_available = isAvailable;
      }
    }
  },
  // Методы загрузки данных комнат и т.д.
}
</script>

<style>
.rooms-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.room {
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}

.room h3 {
  margin: 0;
  font-size: 1.2em;
}

.room p {
  margin: 5px 0;
}

button {
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #45a049;
}
</style>
