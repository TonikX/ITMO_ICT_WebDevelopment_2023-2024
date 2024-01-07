<template>
    <div class="container">
      <h1>Ассортимент магазина</h1>
      <p> Проверьте еду в наличии, приходите в магазин и кормите милых животных! </p>
  
      <table class="shop-table">
        <thead>
          <tr>
            <th>Доступная еда</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="foodItem in foodItems" :key="foodItem.id">
            <td>{{ foodItem.name }}</td>
          </tr>
        </tbody>
      </table>
      <br />

    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        foodItems: [],
      };
    },
    methods: {
      async fetchFoodData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/system/food/');
          this.foodItems = response.data;
        } catch (error) {
          console.error('Error fetching food data:', error);
        }
      },
      goToShop() {
        this.$router.push('/');
      },
    },
    created() {
      this.fetchFoodData();
    },
  };
  </script>
  
  <style> 

.shop-table {
    border-collapse: collapse;
    margin: 0 auto;
  }
  
  .shop-table th, .shop-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
    background-color: #f2f2f2;

  }

  .shop-table td:hover 
  {
    background-color: #ffff99;
    cursor: pointer;
  }
  </style>
  