<template>
    <div class="newspaperorder-details">
      <h2>{{ newspaperorder.user_profile }}</h2>
      <p><strong>Получатель:</strong> {{ newspaperorder.user_profile }}</p>
      <p><strong>Газета:</strong> {{ newspaperorder.newspaper }}</p>
      <p><strong>Количество:</strong> {{ newspaperorder.quantity }}</p>
      <p><strong>Дата получения:</strong> {{ newspaperorder.order_date }}</p>
      <router-link :to="{ name: 'NewsPaperOrderList' }">
        <button class="transparent-button">Назад к списку заказов</button>
      </router-link>
      <router-link :to="{ name: 'NewsPaperOrderEdit', params: { id: newspaperorder.id }}">
        <button class="transparent-button">Редактировать заказ</button>
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newspaperorder: null,
      };
    },
    methods: {
      async fetchNewspaperorderDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/newspaperorders/${this.$route.params.id}/`);
          this.newspaperorder = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchNewspaperorderDetails();
    },
  };
  </script>
  
  <style scoped>
  .newspaperorder-details {
    text-align: center;
    padding: 20px;
  }
  
  .transparent-button {
    padding: 15px 20px;
    font-size: 16px;
    border-radius: 30px;
    background-color: transparent;
    color: #3498db;
    text-decoration: none;
    cursor: pointer;
    border: 1px solid #3498db;
    transition: background-color 0.3s, color 0.3s;
    margin: 10px;
  }
  
  .transparent-button:hover {
    background-color: #3498db;
    color: #fff;
  }
  
  .newspaperorder-details p {
    text-align: left;
    margin: 10px 0;
  }
  </style>
  