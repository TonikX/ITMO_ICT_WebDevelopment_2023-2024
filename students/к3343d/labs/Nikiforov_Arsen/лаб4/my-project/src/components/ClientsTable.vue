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
        </tr>
      </thead>
      <tbody>
        <tr v-for="client in clients" :key="client.id">
          <td>{{ client.id }}</td>
          <td>{{ client.client_info.first_name }}</td>
          <td>{{ client.client_info.last_name }}</td>
          <td>{{ client.room }}</td>
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
    axios.get('http://localhost:8000/hotel_api/api/clients') 
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
