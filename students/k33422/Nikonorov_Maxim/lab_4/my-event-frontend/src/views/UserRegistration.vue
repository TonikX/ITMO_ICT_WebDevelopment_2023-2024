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
