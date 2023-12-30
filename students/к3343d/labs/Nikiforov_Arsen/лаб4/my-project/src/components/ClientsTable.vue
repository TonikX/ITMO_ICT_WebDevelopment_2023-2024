<template>
  <div>
    <h2>Список клиентов</h2>
    <table>
      <thead>
        <tr>
          <th>ID клиента</th>
          <th>Имя</th>
          <th>Фамилия</th>
          <th>Номер комнаты</th>
          <!-- Дополнительные столбцы по необходимости -->
        </tr>
      </thead>
      <tbody>
        <tr v-for="client in clients" :key="client.id">
          <td>{{ client.id }}</td>
          <td>{{ client.first_name }}</td>
          <td>{{ client.last_name }}</td>
          <td>{{ client.room_number }}</td>
          <!-- Дополнительные данные по необходимости -->
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
      clients: []
    };
  },
  created() {
    this.fetchClients();
  },
  methods: {
    fetchClients() {
      axios.get('http://localhost:8000/hotel_api/api//clients') // API URL
        .then(response => {
          this.clients = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении данных о клиентах:', error);
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
