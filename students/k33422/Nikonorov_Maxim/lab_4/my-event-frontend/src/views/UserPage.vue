<template>
    <div>
      <h1>Личный кабинет</h1>
      <div>
        <h2>Информация о пользователе</h2>
        <p><strong>Логин:</strong> {{ user.username }}</p>
        <p><strong>Имя:</strong> {{ user.FirstName }} {{ user.LastName }}</p>
      </div>
  
      <div>
        <h2>Мероприятия, на которые вы зарегистрированы</h2>
        <ul>
          <li v-for="event in events" :key="event.id">
            <p><strong>Название мероприятия:</strong> {{ event.EventCard.PostTitle }}</p>
            <p><strong>Юзер:</strong> {{ event.EventUser.id }}</p>
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        events: [],
        user: '',
      };
    },
    mounted() {
      this.getUserData();
      this.getEvents();
    },
    methods: {
      async getUserData() {
        try {
          const user_id = sessionStorage.getItem('user_id');
          const response = await axios.get(`http://127.0.0.1:8000/users/${user_id}`, {
            headers: { Authorization: 'Token ' + sessionStorage.getItem('token') },
          });
          this.user = response.data;
          
        } catch (error) {
          console.log('Ошибка при получении данных пользователя:', error);
        }
      },
      async getEvents() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/users-wide-events/', {
          headers: { Authorization: 'Token ' + sessionStorage.getItem('token') },
        });
        this.events = response.data.filter(event => event.EventUser.id === this.user.id);
      } catch (error) {
        console.log('Ошибка при получении данных мероприятий:', error);
      }
    },
    },
  };
  </script>
  
  <style scoped>
  </style>
  