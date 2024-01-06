<template>
  <div>
    <h2>Список сотрудников</h2>
    <table class="employee-table">
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

<style scoped>
.employee-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.employee-table th,
.employee-table td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.employee-table th {
  background-color: #f2f2f2;
}

.employee-table tbody tr:nth-child(even) {
  background-color: #f5f5f5;
}
</style>
