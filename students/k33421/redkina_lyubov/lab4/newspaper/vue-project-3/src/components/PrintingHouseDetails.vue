<template>
    <div class="printinghouse-details">
      <h2>{{ printinghouse.name }}</h2>
      <p><strong>Название:</strong> {{ printinghouse.name }}</p>
      <p><strong>Адрес:</strong> {{ printinghouse.address }}</p>
      <p><strong>Статус:</strong> {{ printinghouse.is_closed }}</p>
      <!-- Другие поля газеты, которые вы хотите отобразить -->
      <router-link :to="{ name: 'PrintingHouseList' }">
        <button class="transparent-button">Назад к списку издательств</button>
      </router-link>
      <router-link :to="{ name: 'PrintingHouseEdit', params: { id: printinghouse.id }}">
        <button class="transparent-button">Редактировать издательство</button>
      </router-link>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        printinghouse: null,
      };
    },
    methods: {
      async fetchPrintinghouseDetails() {
        try {
          const response = await axios.get(`http://127.0.0.1:8000/api/printinghouses/${this.$route.params.id}/`);
          this.printinghouse = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    created() {
      this.fetchPrintinghouseDetails();
    },
  };
  </script>
  
  <style scoped>
  .printinghouse-details {
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
  
  .printinghouse-details p {
    text-align: left;
    margin: 10px 0;
  }
  </style>
  