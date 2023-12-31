<template>
  <div>
    <h2>Комплексная информация о комнатах</h2>
    <table>
      <thead>
        <tr>
          <th>ID комнаты</th>
          <th>Тип комнаты</th>
          <th>Статус</th>
          <th>Стоимость</th>
      
        </tr>
      </thead>
      <tbody>
        <tr v-for="room in complexRooms" :key="room.id">
          <td>{{ room.id }}</td>
          <td>{{ room.room_type }}</td>
          <td>{{ room.status }}</td>
          <td>{{ room.cost }}</td>
      
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
      complexRooms: []
    };
  },
  created() {
    this.fetchComplexRooms();
  },
  methods: {
    fetchComplexRooms() {
      axios.get('http://localhost:8000/hotel_api/complex_rooms/') 
        .then(response => {
          this.complexRooms = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении комплексной информации о комнатах:', error);
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
  