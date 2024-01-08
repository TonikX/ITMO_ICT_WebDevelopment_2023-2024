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
  
          // Получение данных пользователя сразу после аутентификации
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