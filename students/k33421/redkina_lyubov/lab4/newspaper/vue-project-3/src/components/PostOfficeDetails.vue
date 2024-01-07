<template>
    <div class="postoffice-details">
      <h2>{{ postoffice.number }}</h2>
      <p><strong>Номер:</strong> {{ postoffice.number }}</p>
      <p><strong>Адрес:</strong> {{ postoffice.address }}</p>
      <router-link :to="{ name: 'PostOfficeList' }">
        <button class="transparent-button">Назад к списку отделений</button>
      </router-link>
      <router-link :to="{ name: 'PostOfficeEdit', params: { id: postoffice.id }}">
        <button class="transparent-button">Редактировать отделение</button>
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        postoffice: null,
      };
    },
    methods: {
      async fetchPostofficeDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/postoffices/${this.$route.params.id}/`);
          this.postoffice = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchPostofficeDetails();
    },
  };
  </script>
  
  <style scoped>
  .postoffice-details {
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
  
  .postoffice-details p {
    text-align: left;
    margin: 10px 0;
  }
  </style>
  