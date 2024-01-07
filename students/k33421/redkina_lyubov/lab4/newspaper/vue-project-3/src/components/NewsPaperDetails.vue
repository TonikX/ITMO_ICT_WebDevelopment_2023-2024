<template>
    <div class="newspaper-details">
      <h2>{{ newspaper.title }}</h2>
      <p><strong>Edition Index:</strong> {{ newspaper.edition_index }}</p>
      <p><strong>Editor:</strong> {{ newspaper.editor_last_name }}, {{ newspaper.editor_first_name }} {{ newspaper.editor_middle_name }}</p>
      <p><strong>Price:</strong> {{ newspaper.price }}</p>
      <!-- Другие поля газеты, которые вы хотите отобразить -->
      <router-link :to="{ name: 'NewsPaperList' }">
        <button class="transparent-button">Назад к списку газет</button>
      </router-link>
      <router-link :to="{ name: 'NewsPaperEdit', params: { id: newspaper.id }}">
        <button class="transparent-button">Редактировать газету</button>
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        newspaper: null,
      };
    },
    methods: {
      async fetchNewspaperDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/newspapers/${this.$route.params.id}/`);
          this.newspaper = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchNewspaperDetails();
    },
  };
  </script>
  
  <style scoped>
  .newspaper-details {
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
  
  .newspaper-details p {
    text-align: left;
    margin: 10px 0;
  }
  </style>
  