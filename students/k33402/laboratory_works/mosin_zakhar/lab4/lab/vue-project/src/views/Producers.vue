<template>
  <div class="producers-table">
    <h1>Producers Companies Page</h1>

    <!-- Search input -->
    <label>Search by Name:</label>
    <input v-model="searchTerm" @input="filterProducers" />

    <!-- Table of producers -->
    <table>
      <thead>
        <tr>
          <th>Name</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="producer in filteredProducers" :key="producer.id">
          <td>{{ producer.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Producers',
  data() {
    return {
      producers: [],
      searchTerm: '',
    };
  },
  computed: {
    filteredProducers() {
      const search = this.searchTerm.toLowerCase();
      return this.producers.filter(
        producer => producer.name.toLowerCase().includes(search)
      );
    },
  },
  methods: {
    async fetchProducers() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/main/companies/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('access_token')}`,
          },
        });
        this.producers = response.data;
      } catch (error) {
        console.error('Error fetching producer data:', error);
      }
    },
    filterProducers() {
      // Triggered when search term changes
    },
  },
  created() {
    this.fetchProducers();
  },
};
</script>

<style scoped>
.producers-table {
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
  background-color: #b80000; /* Цвет фона для заголовков */
}
</style>
