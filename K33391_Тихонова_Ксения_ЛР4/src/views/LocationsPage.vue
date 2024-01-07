<template>
    <div class="container">
      <h1>Места обитания</h1>
      <p> Здесь вы можете посмотреть места обитания животных в нашем зоопарке. </p>
      <table class="locations-table">
        <thead>
          <tr>
            <th>Название места</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="locationItem in locationItems" :key="locationItem.id">
            <td>{{ locationItem.name }}</td>
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
        locationItems: [],
      };
    },
    methods: {
      async fetchLocationData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/system/locations/' , {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          console.log(response.data);
      
          this.locationItems = response.data;
        } catch (error) {
          console.error('Error fetching location data:', error);
        }
      },
    },
    created() {
      this.fetchLocationData();
    },
  };
  </script>
  
  <style scoped>
  
  .locations-table {
    border-collapse: collapse;
    margin: 0 auto;
  }
  
  .locations-table th, .locations-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    background-color: #f2f2f2;

  }

  .locations-table td:hover 
  {
    background-color: #ffff99;
    cursor: pointer;
  }
  </style>
  