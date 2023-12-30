<template>
  <div>
    <h2>Список сотрудников</h2>
    <table>
      <thead>
        <tr>
          <th>ID сотрудника</th>
          <th>Имя</th>
          <th>Фамилия</th>
     
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td>{{ employee.id }}</td>
          <td>{{ employee.first_name }}</td>
          <td>{{ employee.last_name }}</td>
     
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
      employees: []
    };
  },
  created() {
    this.fetchEmployees();
  },
  methods: {
    fetchEmployees() {
      axios.get('http://localhost:8000/hotel_api/api/employees') 
        .then(response => {
          this.employees = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении данных о сотрудниках:', error);
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
