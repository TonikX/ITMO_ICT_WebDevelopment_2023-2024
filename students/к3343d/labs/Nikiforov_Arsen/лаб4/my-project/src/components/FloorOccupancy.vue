<template>
  <div>
    <h2>Заполненность этажей</h2>
    <table>
      <thead>
        <tr>
          <th>Этаж</th>
          <th>Занятые комнаты</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="floor in floors" :key="floor.number">
          <td>{{ floor.number }}</td>
          <td>{{ floor.occupied_rooms_count }}</td>
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
      floors: []
    };
  },
  created() {
    axios.get('http://localhost:8000/hotel_api/floor_occupancy/')
      .then(response => {
        this.floors = response.data;
      })
      .catch(error => {
        console.error('Ошибка:', error);
      });
  }
};
</script>
