<template>
    <div class="container">
      <h1>Другие зоопарки</h1>
      <p> Обязательно посетите другие зоопарки! </p>
  
      <table class="other-zoos-table">
        <thead>
          <tr>
            <th>Название зоопарка</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="zooItem in zooItems" :key="zooItem.id">
            <td>{{ zooItem.name }}</td>
            
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
        zooItems: [],
      };
    },
    methods: {
      async fetchZooData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/system/other-zoos/',  { 
            headers: {
              'Authorization': `Token ${localStorage.getItem('access_token')}`,
            },
    }
      ,);
          this.zooItems = response.data;
        } catch (error) {
          console.error('Error fetching other zoos data:', error);
        }
      },
    },
    created() {
      this.fetchZooData();
    },
  };
  </script>
  
  <style scoped>
  
  .other-zoos-table {
    border-collapse: collapse;
    margin: 0 auto;
  }

  .other-zoos-table th, .other-zoos-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    background-color: #f2f2f2;

  }

  .other-zoos-table td:hover 
  {
    background-color: #ffff99;
    cursor: pointer;
  }

  </style>
  