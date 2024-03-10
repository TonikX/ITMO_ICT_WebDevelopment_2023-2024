<template>
    <div>
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
  
      <!-- List of brokers -->
      <ul>
        <li v-for="broker in filteredBrokers" :key="broker.id">
          {{ broker.name }} - Income: {{ broker.income }}
        </li>
      </ul>
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
  /* Add your styles here */
  </style>
  