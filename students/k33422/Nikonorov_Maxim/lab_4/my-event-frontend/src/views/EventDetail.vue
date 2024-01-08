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
      <!-- Registration Form -->
      <div v-if="user && event.Status === 'OPENED' && !registrationError">
        <button class="btn btn-primary" @click="registerForEvent">Зарегистрироваться</button>
      </div>
      <div v-else-if="registrationError">
        <button class="btn btn-danger">Вы уже зарегистрированы на это мероприятие.</button>
      </div>
      <div v-else-if="event.Status !== 'OPENED'">
        <p :class="statusClass(event.Status)">Регистрация на мероприятие: {{ event.Status }}</p>
      </div>
      <div v-else>
        <p>Войдите, чтобы зарегистрироваться на мероприятие.</p>
      </div>
    </div>
    <div v-else>
      <p>Загрузка данных...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      event: null,
      user: null,
      registrationError: false,
    };
  },
  watch: {
    '$route.params.id': 'fetchEventData',
  },
  mounted() {
    this.fetchEventData();
    this.getUserData();
  },
  methods: {
    statusClass(status) {
      switch (status) {
        case 'OPENED':
          return 'status-opened';
        case 'CANCELED':
          return 'status-canceled';
        case 'CLOSED':
          return 'status-closed';
        default:
          return '';
      }
    },
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
    async getUserData() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/event/auth/users/me', {
          headers: { Authorization: 'Token ' + sessionStorage.getItem('token') },
        });
        this.user = response.data;
      } catch (error) {
        console.log('Ошибка при получении данных пользователя:', error);
      }
    },
    async registerForEvent() {
      try {
        const eventId = this.$route.params.id;
        const userId = this.user.id;

        const response = await axios.post('http://127.0.0.1:8000/users-events/', {
          EventUser: userId,
          EventCard: eventId,
        },
        {
          headers: { Authorization: 'Token ' + sessionStorage.getItem('token') },
        });

        console.log('Successfully registered for the event:', response.data);
        this.$router.push({ name: 'EventHome' });
      } catch (error) {
        if (error.response && error.response.data.non_field_errors && error.response.data.non_field_errors.includes('The fields EventUser, EventCard must make a unique set.')) {
          this.registrationError = true;
        } else {
          console.log('Error while registering:', error);
        }
      }
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

.status-opened {
  color: green;
}

.status-canceled {
  color: orange;
}

.status-closed {
  color: red;
}

</style>
