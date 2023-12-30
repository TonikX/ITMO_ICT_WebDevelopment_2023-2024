<template>
  <div>
    <h2>Статистика по комнатам</h2>
    <table>
      <thead>
        <tr>
          <th>Тип комнаты</th>
          <th>Общее количество</th>
          <th>Средняя стоимость</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="stat in roomStats" :key="stat.room_type">
          <td>{{ stat.room_type }}</td>
          <td>{{ stat.total }}</td>
          <td>{{ stat.average_cost }}</td>
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
      roomStats: []
    };
  },
  created() {
    this.fetchRoomStatistics();
  },
  methods: {
    fetchRoomStatistics() {
      axios.get('http://localhost:8000/hotel_api/api/room-statistics/') 
        .then(response => {
          this.roomStats = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении статистики комнат:', error);
        });
    }
  }
};
</script>

<style>
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
</style>
