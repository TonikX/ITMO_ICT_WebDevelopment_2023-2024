<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Имя пользователя:</label>
        <input id="username" v-model="user.username" type="text" required>
      </div>
      <div>
        <label for="email">Электронная почта:</label>
        <input id="email" v-model="user.email" type="email" required>
      </div>
      <div>
        <label for="password">Пароль:</label>
        <input id="password" v-model="user.password" type="password" required>
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      }
    }
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/users/', this.user);
        console.log('Регистрация прошла успешно', response.data);
        this.$router.push('/');
      } catch (error) {
        console.error('Ошибка при регистрации:', error.response.data);
      }
    }
  }
}
</script>



<style scoped>

</style>