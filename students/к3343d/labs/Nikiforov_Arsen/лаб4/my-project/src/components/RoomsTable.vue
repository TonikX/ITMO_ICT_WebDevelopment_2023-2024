<template> 
  <div>
    <h2>Список комнат</h2>

    <!-- Фильтры -->
    <label for="room_type">Тип комнаты:</label>
    <select v-model="filterType">
      <option value="">--Выберите тип--</option>
      <option value="single">Одноместный</option>
      <option value="double">Двухместный</option>
      <option value="suite">Люкс</option>
    </select>

    <label for="room_status">Статус комнаты:</label>
    <select v-model="filterStatus">
      <option value="">--Выберите статус--</option>
      <option value="available">Доступна</option>
      <option value="occupied">Занята</option>
      <option value="cleaning">На уборке</option>
    </select>

    <!-- Выбор даты бронирования -->
    <div class="date-selection">
      Выберите дату:
      <input type="date" v-model="startDate" placeholder="Дата начала">
      <input type="date" v-model="endDate" placeholder="Дата окончания">
    </div>

    <!-- Таблица комнат -->
    <table class="table">
      <thead>
        <tr>
          <th>Тип комнаты</th>
          <th>Номер этажа</th>
          <th>Статус</th>
          <th>Стоимость</th>
          <th>Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="room in filteredRooms" :key="room.id">
          <td>{{ room.room_type }}</td>
          <td>{{ room.floor }}</td>
          <td>{{ room.status }}</td>
          <td>{{ room.cost }}</td>
          <td>
            <button v-if="room.status === 'available'" @click="bookRoom(room.id)">
              Забронировать
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      rooms: [],
      filterType: '',
      filterStatus: '',
      startDate: '',
      endDate: ''
    };
  },
  computed: {
    filteredRooms() {
      return this.rooms.filter(room => {
        return (!this.filterType || room.room_type === this.filterType) &&
               (!this.filterStatus || room.status === this.filterStatus);
      });
    }
  },
  created() {
    this.fetchRooms();
  },
  methods: {
    fetchRooms() {
      axios.get('http://localhost:8000/hotel_api/api/rooms/')
        .then(response => {
          this.rooms = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении данных о комнатах:', error);
        });
    },
    bookRoom(roomId) {
    // Проверка, выбраны ли даты начала и окончания бронирования
    if (!this.startDate || !this.endDate) {
      alert('Введите дату!');
      return;
    }

    const bookingData = {
      start_date: this.startDate,
      end_date: this.endDate
    };

    axios.post(`http://localhost:8000/hotel_api/api/rooms/${roomId}/book_room/`, bookingData, {
      headers: {
        'Authorization': `Bearer ${this.$store.state.user.token}`
      }
    })
    .then(() => {
      alert('Бронирование успешно отправлено на подтверждение');
      this.fetchRooms();
    })
    .catch(error => {
      console.error('Ошибка при бронировании комнаты:', error);
    });
  }

  }
};
</script>




<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.table th,
.table td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.table th {
  background-color: #f2f2f2;
}

.table tbody tr:nth-child(even) {
  background-color: #f5f5f5;
}
</style>
