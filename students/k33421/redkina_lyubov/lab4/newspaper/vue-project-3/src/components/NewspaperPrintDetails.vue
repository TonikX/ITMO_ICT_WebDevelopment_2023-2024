<template>
    <div class="newspaperprint-details">
      <h2>{{ newspaperprint.newspaper }}</h2>
      <p><strong>Газета:</strong> {{ newspaperprint.newspaper }}</p>
      <p><strong>Издательство:</strong> {{ newspaperprint.printing_house }}</p>
      <p><strong>Тираж:</strong> {{ newspaperprint.circulation }}</p>
      <router-link :to="{ name: 'NewsPaperPrintList' }">
        <button class="transparent-button">Назад к списку выпусков</button>
      </router-link>
      <router-link :to="{ name: 'NewsPaperPrintEdit', params: { id: newspaperprint.id }}">
        <button class="transparent-button">Редактировать выпуск</button>
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newspaperprint: null,
      };
    },
    methods: {
      async fetchNewspaperprintDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/newspaperprints/${this.$route.params.id}/`);
          this.newspaperprint = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchNewspaperprintDetails();
    },
  };
  </script>
  
  <style scoped>
  .newspaperprint-details {
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
  
  .newspaperprint-details p {
    text-align: left;
    margin: 10px 0;
  }
  </style>
  