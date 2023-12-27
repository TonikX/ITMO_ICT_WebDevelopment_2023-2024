<template>
    <div>
      <h2>Список комнат</h2>
      <table>
        <thead>
          <tr>
            <th>Тип комнаты</th>
            <th>Этаж</th>
            <th>Статус</th>
            <th>Стоимость</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="room in rooms" :key="room.id">
            <td>{{ room.room_type }}</td>
            <td>{{ room.floorNumber }}</td>
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
        rooms: []
      };
    },
    created() {
      this.fetchRooms();
    },
    methods: {
      fetchRooms() {
        axios.get('http://localhost:8000/hotel_api/api/rooms/')
          .then(response => {
            this.rooms = response.data.map(room => ({
              ...room,
              floorNumber: room.floor ? room.floor.number : 'Неизвестно'
            }));
            console.log('Комнаты загружены:', this.rooms);
          })
          .catch(error => {
            console.error('Ошибка при загрузке данных о комнатах:', error);
          });
      }
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
  </style>
  