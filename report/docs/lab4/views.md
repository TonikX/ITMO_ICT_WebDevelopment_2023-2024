## Описание предметной области

У меня индивидуальный вариант, поэтому я решил создать сайт, на котором пользователи могут зарегистрироваться на разные мероприятия. Пользователь представлен абстрактным классом (`EventsUser`), который связан со встроенной моделью User. Также при регистрации он может указать почту, телефон и свой возраст.

Все мероприятия (`EventCard`) собраны на главной странице и имеют название, описание, тип (например, лекция или концерт), дату проведения, возрастное ограничение и максимальное количество мест. Список мероприятий представлен отдельной моделью (`EventTypeList`).

Мероприятия проходят в разных местах (`Place`), у которых есть название, адрес и вместимость. На мероприятие не может зарегистрироваться больше людей, чем может вмещать в себя площадка.

Также для пользователя действуют дополнительные ограничения. Он не может зарегистрироваться на мероприятие, если не проходит по возрасту, а также если мероприятие отменено или уже прошло.

## Авторизация

В папке `views` у меня лежат основные представления для логина, регистрации, отображения главной страницы и личного кабинета пользователя.

Получение информации о пользователе происходит через библиотеку djoser. Также во временное хранилище при логине сохраняются данные о токене, id и юзернейме пользователя.

``` js title="UserRegistration.vue"
<template>
  <div class="card" style="max-width: 50%; margin: 50px auto;">
    <h1 class="text-dark" style="text-align: center;">Регистрация</h1>
    <form @submit.prevent="register" class="card-body">
      <div class="form-group">
        <label for="username" class="text-secondary">Логин:</label>
        <input type="text" id="username" v-model="username" required class="form-control" placeholder="Логин">
      </div>
      <div class="form-group">
        <label for="FirstName" class="text-secondary">Имя:</label>
        <input type="text" id="FirstName" v-model="FirstName" required class="form-control" placeholder="Имя">
      </div>
      <div class="form-group">
        <label for="LastName" class="text-secondary">Фамилия:</label>
        <input type="text" id="LastName" v-model="LastName" required class="form-control" placeholder="Фамилия">
      </div>
      <div class="form-group">
        <label for="email" class="text-secondary">Email:</label>
        <input type="email" id="email" v-model="email" required class="form-control" placeholder="Почта">
      </div>
      <div class="form-group">
        <label for="password" class="text-secondary">Пароль:</label>
        <input type="password" id="password" v-model="password" required class="form-control" placeholder="Пароль">
      </div>
      <br>
      <button type="submit" class="btn btn-dark">Зарегистрироваться</button>
      <br>
      <p v-if="err" class="text-danger">{{ err }}</p>
    </form>
  </div>
</template>
  
<script>
import axios from 'axios';

export default {
  name: 'UserRegistration',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      LastName: '',
      FirstName: '',
      err: null
    };
  },
  methods: {
    register() {
      axios.post('http://127.0.0.1:8000/event/auth/users/', {
        username: this.username,
        email: this.email,
        password: this.password,
        LastName: this.LastName,
        FirstName: this.FirstName,
      }, )
      .then(response => {
        console.log('Успешная регистрация:', response.data);
        
        this.$router.push({ name: 'login' });
      })
      .catch(error => {
        console.error('Ошибка регистрации:', error.response.data);
        this.err = error.response.data;
      });
    },
  }
}
</script>
```

``` js title="UserLogin.vue"
<template>
  <div class="card" style="max-width: 50%; margin: 50px auto;">
    <h1 class="text-dark" style="text-align: center;">Вход</h1>
    <form @submit.prevent="login" class="card-body">
      <div class="form-group">
        <label for="username" class="text-secondary">Логин:</label>
        <input type="text" id="username" v-model="username" required class="form-control" placeholder="Логин">
      </div>
      <div class="form-group">
        <label for="password" class="text-secondary">Пароль:</label>
        <input type="password" id="password" v-model="password" required class="form-control" placeholder="Пароль">
      </div>
      <br>
      <button type="submit" class="btn btn-dark">Войти</button>
      <br>
      <p v-if="err" class="text-danger">{{ err }}</p>
    </form>
  </div>
</template>

  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'UserLogin',
    data() {
      return {
        username: '',
        password: '',
        err: null,
      };
    },
    methods: {
      login() {
        axios.post('http://127.0.0.1:8000/auth/token/login/', {
          username: this.username,
          password: this.password,
        })
        .then(response => {
          console.log('Успешный вход:', response.data);
          sessionStorage.setItem('token', response.data.auth_token)
          sessionStorage.setItem('username', this.username)
          sessionStorage.setItem('password', this.password)
  
          this.getUserData();
  
          this.$router.push({ name: 'EventHome' });
        })
        .catch(error => {
          console.error('Ошибка входа:', error.response.data);
          this.err = 'Неправильный логин или пароль';
        });
      },
      async getUserData() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/event/auth/users/me', {
            headers: { Authorization: 'Token ' + sessionStorage.getItem('token') },
          });
          this.user = response.data;
          sessionStorage.setItem('user_id', this.user.id);
          this.$store.commit('setAuthenticated', true);
          console.log('hi')
        } catch (error) {
          console.log('Ошибка при получении данных пользователя:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
```


## Страница события

На странице события пользователь может зарегистрироваться на мероприятие. Также страница предусматривает различные вариарты событий и не дает посетить мероприятие, если нет мест или пользователь уже взял билет.

``` js title="EventDetail.vue"
<template>
  <div class="event-detail card">
    <router-link to="/" class="btn btn-dark mb-3">&lt; Назад</router-link>
    <div v-if="event" class="card-body">
      <h1 class="card-title text-dark">{{ event.PostTitle || 'Название не указано' }}</h1>
      <div class="alert alert-dark" role="alert" v-html="event.Description || 'Описание не указано'"></div>
      <p class="card-text">Дата: {{ event.DateOfEvent || 'Дата не указана' }}</p>
      <p class="card-text">
        Место: {{ event.EventPlace ? event.EventPlace.PlaceTitle || 'Место не указано' : 'Место не указано' }}
      </p>
      <!-- Registration Form -->
      <div v-if="user && event.Status === 'OPENED' && !registrationError">
        <button class="btn btn-dark" @click="registerForEvent">Зарегистрироваться</button>
      </div>
      <div v-else-if="registrationError">
        <button class="btn btn-danger">Вы уже зарегистрированы на это мероприятие.</button>
      </div>
      <div v-else-if="event.Status !== 'OPENED'">
        <p :class="statusClass(event.Status)">Регистрация на мероприятие: {{ event.Status }}</p>
      </div>
      <div v-else>
        <b><p>Войдите, чтобы зарегистрироваться на мероприятие.</p></b>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { reactive } from 'vue';

export default {

  setup() {
    const authState = reactive({
      isAuthenticated: !!sessionStorage.getItem('token'),
    });

    return { authState };
  },

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
```
## Страница события

На странице пользователя он может посмотреть свои регистрации и отписаться от события.

``` js title="UserPage.vue"
<template>
  <div class="container mt-5">
    <div class="card">
      <div class="card-body">
        <h2>Аккаунт</h2>
        <div class="alert alert-dark" role="alert">Привет, {{ user.username }}</div>
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
```