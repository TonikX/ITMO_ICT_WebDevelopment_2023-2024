<template>
    <div>
      <h2>Таблица сотрудников</h2>
      <table>
        <thead>
          <tr>
            <th>Имя</th>
            <th>Фамилия</th>
            <th>Должность</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="employee in employees" :key="employee.id">
            <td>{{ employee.firstName }}</td>
            <td>{{ employee.lastName }}</td>
            <td>{{ employee.position }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        employees: [
          { id: 1, firstName: "Анна", lastName: "Смирнова", position: "Менеджер" },
          { id: 2, firstName: "Петр", lastName: "Иванов", position: "Рецепционист" },
        ]
      };
    }
  };
  </script>
  
  <style scoped>
  </style>
  