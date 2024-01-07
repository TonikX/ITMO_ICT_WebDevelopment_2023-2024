<template>
    <div class="event-detail">
        <router-link to="/" class="back-button">&lt;</router-link>
      <div v-if="event">
        <br>
        <br>
        <h1>{{ event.PostTitle || 'Название не указано' }}</h1> 
        <p v-html="event.Description || 'Описание не указано'"></p>
        <p>Дата: {{ event.DateOfEvent || 'Дата не указана' }}</p>
        <p>
          Место: {{ event.EventPlace ? event.EventPlace.PlaceTitle || 'Место не указано' : 'Место не указано' }}
        </p>
      </div>
      <div v-else>
        <p>Загрузка данных...</p>
      </div>
    </div>
  </template>
  
  <script>
  
  export default {
    data() {
      return {
        event: null,
      };
    },
    watch: {
      '$route.params.id': 'fetchEventData',
    },
    mounted() {
      this.fetchEventData();
    },
    methods: {
      fetchEventData() {
        const eventId = this.$route.params.id;
        this.$axios
          .get(`http://127.0.0.1:8000/events/${eventId}/`)
          .then((response) => {
            this.event = response.data;
          })
          .catch((error) => {
            console.error('Ошибка при загрузке мероприятий:', error);
          });
      },
    },
  };
  </script>
  
  <style scoped>
  .event-detail {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    position: relative;
  }
  
  h1 {
    font-family: 'Poppins', sans-serif;
    color: #0080ff;
  }
  
  p {
    font-family: 'Poppins', sans-serif;
    color: #333;
    margin-bottom: 10px;
  }
  
  .back-button {
    font-size: 24px;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: #0080ff;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none;
    position: absolute;
    top: 20px;
    left: 20px;
  }
  
  .back-button:hover {
    background-color: #00588e;
  }
  </style>