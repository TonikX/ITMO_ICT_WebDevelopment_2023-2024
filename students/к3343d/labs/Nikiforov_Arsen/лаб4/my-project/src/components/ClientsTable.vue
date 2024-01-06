<template>
  <div>
    <h2>Список клиентов</h2>
    <table class="table">
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
