<template>
  <div class="container mt-5">
    <div class="card">
      <div class="card-header">
        <h1>Личный кабинет</h1>
      </div>
      <div class="card-body">
        <h2>Аккаунт</h2>
        <p><strong>Логин:</strong> {{ user.username }}</p>
        <p><strong>Имя:</strong> {{ user.FirstName }} {{ user.LastName }}</p>
      </div>
    </div>

    <div class="card mt-5">
      <div class="card-header">
        <h2>Мероприятия, на которые вы зарегистрированы</h2>
      </div>
      <div class="card-body">
        <ul class="list-group">
          <li class="list-group-item" v-for="event in events" :key="event.id">
            <h5><strong>Название мероприятия:</strong> {{ event.EventCard.PostTitle }}</h5>
            <p><strong>Дата:</strong> {{ event.EventCard.DateOfEvent }}</p>
            <p><strong>Адрес:</strong> {{ event.EventCard.EventPlace.PlaceAddress }}</p>
            <CButton color="danger" @click="openModal(event.id)">Удалить</CButton>
          </li>
        </ul>
      </div>

      <CModal
        v-model:visible="visible"
        @close="closeModal"
      >
      <CModalHeader :on-close="closeModal">
        <CModalTitle>Удалить мероприятие</CModalTitle>
      </CModalHeader>
      <CModalBody>
        Вы уверены, что хотите отписаться от этого мероприятия?
      </CModalBody>
      <CModalFooter>
        <CButton color="secondary" @click="closeModal">Отмена</CButton>
        <CButton color="primary" @click="deleteEvent">Удалить</CButton>
      </CModalFooter>
      </CModal>

    </div>
  </div>
</template>
  
  <script>
  import { CButton, CModal, CModalHeader, CModalTitle, CModalBody, CModalFooter } from '@coreui/vue';
  import axios from 'axios';
  
  export default {

    components: {
    CButton,
    CModal,
    CModalHeader,
    CModalTitle,
    CModalBody,
    CModalFooter
  },

    data() {
      return {
        events: [],
        user: '',
        visible: false,
        eventToDelete: null
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
    openModal(eventId) {
      this.visible = true;
      this.eventToDelete = eventId;
    },
    closeModal() {
      this.visible = false;
    },
    deleteEvent() {
      axios.delete(`http://127.0.0.1:8000/users-events/${this.eventToDelete}/`, {
        headers: { Authorization: 'Token ' + sessionStorage.getItem('token') },
      })
        .then(() => {
          console.log('Registration deleted');
          this.getEvents(); 
          this.closeModal();
        })
        .catch(error => {
          console.error('Error deleting registration:', error);
        });
    }
    },
  };
  </script>
  
  <style scoped>
  </style>
  