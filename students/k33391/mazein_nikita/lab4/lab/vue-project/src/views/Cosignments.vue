<template>
    <div>
      <h1>Consignments Page</h1>
  
      <label>Sort By:</label>
      <select v-model="sortBy" @change="sortConsignments">
        <option value="date_sold">Date Sold</option>
        <option value="cost">Cost</option>
      </select>
  
      <label>Search:</label>
      <input v-model="searchTerm" @input="filterConsignments" />
  
      <ul>
        <li v-for="consignment in filteredConsignments" :key="consignment.id">
          Date Sold: {{ consignment.date_sold }} - Cost: {{ consignment.cost }}
        </li>
      </ul>
  
      <div>
        <h2>Add New Consignment</h2>
        <form @submit.prevent="addConsignment">
          <label for="dateSold">Date Sold:</label>
          <input type="date" v-model="newConsignment.date_sold" required />
  
          <label for="num">Number:</label>
          <input type="text" v-model="newConsignment.num" required />
  
          <label for="cost">Cost:</label>
          <input type="number" v-model="newConsignment.cost" required />
  
          <label for="prepayment">Prepayment:</label>
          <input type="checkbox" v-model="newConsignment.prepayment" />
  
          <label for="broker">Broker ID:</label>
          <input type="number" v-model="newConsignment.broker" required />
  
          <button type="submit">Add Consignment</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Consignments',
    data() {
      return {
        consignments: [],
        sortBy: 'date_sold',
        searchTerm: '',
        newConsignment: {
          date_sold: '',
          num: '',
          cost: 0,
          prepayment: false,
          broker: 0,
        },
      };
    },
    computed: {
      sortedConsignments() {
        return this.consignments.slice().sort((a, b) => {
          if (this.sortBy === 'date_sold') {
            return new Date(b.date_sold) - new Date(a.date_sold);
          } else if (this.sortBy === 'cost') {
            return b.cost - a.cost;
          }
          return 0;
        });
      },
      filteredConsignments() {
        const search = this.searchTerm.toLowerCase();
        return this.sortedConsignments.filter(
          consignment => consignment.date_sold.toLowerCase().includes(search)
        );
      },
    },
    methods: {
      async fetchConsignments() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/main/consignments/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.consignments = response.data;
        } catch (error) {
          console.error('Error fetching consignment data:', error);
        }
      },
      sortConsignments() {
      },
      filterConsignments() {
      },
      async addConsignment() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/main/consignments/', this.newConsignment, {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          console.log('Consignment added successfully:', response.data);
        } catch (error) {
          console.error('Error adding consignment:', error.response.data);
        }
      },
    },
    created() {
      this.fetchConsignments();
    },
  };
  </script>
  
  <style scoped>
  </style>  