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
      <input type="date" v-model="startDate" placeholder="Дата начала">
      <input type="date" v-model="endDate" placeholder="Дата окончания">
    </div>

    <!-- Таблица комнат -->
    <table>
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
      startDate: '', // Для хранения даты начала бронирования
      endDate: ''   // Для хранения даты окончания бронирования
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
  methods: {
    fetchRooms() {
      axios.get('http://localhost:8000/hotel_api/api/rooms/')
        .then(response => {
          this.rooms = response.data;
        })
        .catch(error => {
          console.error('Ошибка загрузки комнат:', error);
        });
    },
    applyFilter() {
      this.fetchRooms();
    },
    bookRoom(roomId) {
      if (!this.startDate || !this.endDate) {
        alert('Необходимо указать даты начала и окончания бронирования');
        return;
      }

      const token = localStorage.getItem('userToken');
      axios.post(`http://localhost:8000/hotel_api/api/book_room/${roomId}/`, {
        start_date: this.startDate,
        end_date: this.endDate
      }, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      .then(response => {
        if (response.data.status === 'success') {
          alert('Комната успешно забронирована');
          this.fetchRooms(); // Обновление списка комнат
        } else {
          console.error('Ответ об ошибке:', response.data);
          alert('Ошибка бронирования: ' + response.data.message);
        }
      })
      .catch(error => {
        console.error('Ошибка бронирования комнаты:', error);
        alert('Ошибка бронирования: ' + error.message);
      });
    }
  },
  created() {
    this.fetchRooms();
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

td {
  background-color: #fff;
}

tr:hover {
  background-color: #f5f5f5;
}

.date-selection {
  margin: 10px 0;
}

.date-selection input {
  margin-right: 10px;
}
</style>
