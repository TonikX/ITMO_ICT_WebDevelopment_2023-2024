<template>
    <div class="newspaperarrival-details">
      <h2>{{ newspaperarrival.newspaper }}</h2>
      <p><strong>Газета:</strong> {{ newspaperarrival.newspaper }}</p>
      <p><strong>Почтовое отделение:</strong> {{ newspaperarrival.post_office }}</p>
      <p><strong>Количество:</strong> {{ newspaperarrival.quantity }}</p>
      <router-link :to="{ name: 'NewsPaperArrivalList' }">
        <button class="transparent-button">Назад к списку поступлений</button>
      </router-link>
      <router-link :to="{ name: 'NewsPaperArrivalEdit', params: { id: newspaperarrival.id }}">
        <button class="transparent-button">Редактировать поступление</button>
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newspaperarrival: null,
      };
    },
    methods: {
      async fetchNewspaperarrivalDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/newspaperarrivals/${this.$route.params.id}/`);
          this.newspaperarrival = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchNewspaperarrivalDetails();
    },
  };
  </script>
  
  <style scoped>
  .newspaperarrival-details {
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
  
  .newspaperarrival-details p {
    text-align: left;
    margin: 10px 0;
  }
  </style>
  