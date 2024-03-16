<template>
  <div class="brokers-table">
    <h1>Brokers Page</h1>

    <!-- Sorting options -->
    <label>Sort By:</label>
    <select v-model="sortBy" @change="sortBrokers">
      <option value="name">Name</option>
      <option value="income">Income</option>
    </select>

    <!-- Search input -->
    <label>Search:</label>
    <input v-model="searchTerm" @input="filterBrokers" />

    <!-- Table of brokers -->
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Income</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="broker in filteredBrokers" :key="broker.id">
          <td>{{ broker.name }}</td>
          <td>{{ broker.income }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Brokers',
  data() {
    return {
      brokers: [],
      sortBy: 'name',
      searchTerm: '',
    };
  },
  computed: {
    sortedBrokers() {
      return this.brokers.slice().sort((a, b) => {
        if (this.sortBy === 'name') {
          return a.name.localeCompare(b.name);
        } else if (this.sortBy === 'income') {
          return b.income - a.income;
        }
        return 0;
      });
    },
    filteredBrokers() {
      const search = this.searchTerm.toLowerCase();
      return this.sortedBrokers.filter(
        broker => broker.name.toLowerCase().includes(search)
      );
    },
  },
  methods: {
    async fetchBrokers() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/main/brokers/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('access_token')}`,
          },
        });
        this.brokers = response.data;
      } catch (error) {
        console.error('Error fetching broker data:', error);
      }
    },
    sortBrokers() {
      // Triggered when sorting option changes
    },
    filterBrokers() {
      // Triggered when search term changes
    },
  },
  created() {
    this.fetchBrokers();
  },
};
</script>

<style scoped>

body{
    min-height: 500px;
    background-color: #001b68;
}

.brokers-table {
  margin: 0 auto; /* Центрирует элемент по горизонтали */
  max-width: 600px; /* Максимальная ширина таблицы */
}

table {
  width: 100%;
  border-collapse: collapse; /* Сводит границы ячеек вместе */
}

th, td {
  border: 1px solid #ddd; /* Границы для ячеек */
  padding: 8px;
  text-align: left;
}

th {
  background-color: #b80098; /* Цвет фона для заголовков */
}
</style>