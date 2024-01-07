<template>
    <div>
      <h1>Личный кабинет</h1>
      <div>
        <h2>Информация о пользователе</h2>
        <p><strong>Имя:</strong> {{ user.id }} {{ user.username }}</p>
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
        user: {},
        events: [],
      };
    },
    mounted() {
        
        axios.get(`http://127.0.0.1:8000/current_user/`)
            .then(response => {
                
                console.log(response.data);  
                this.user = response.data;
            })
            .catch(error => {
              
                console.error('Ошибка при получении данных пользователя:', error);
            });

       
        axios.get('http://127.0.0.1:8000/users-events/')
            .then(response => {
                this.events = response.data;
            })
            .catch(error => {
                console.error('Ошибка при загрузке мероприятий пользователя:', error);
            });
    },

  };
  </script>
  
  <style scoped>

  </style>
  