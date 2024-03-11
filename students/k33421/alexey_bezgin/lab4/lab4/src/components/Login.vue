<template>
  <div class="container">
    <form @submit.prevent="login">
      <h2 class="mb-3">Авторизация</h2>
      <div class="input">
        <input
          class="form-control"
          type="text"
          v-model="username"
          name="логин"
          placeholder="логин"
        />
      </div>
      <div class="input">
        <input
          class="form-control"
          v-model="password"
          type="password"
          name="password"
          placeholder="пароль"
        />
      </div>
      <div class="alternative-option mt-4">
        Нет аккаунта? <span @click="gotoSignUp">Зарегистрироваться</span>
      </div>
      <button type="submit" class="mt-4 btn-pers" id="login_button" @click="signin">
        Войти
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    signin() {
      axios.post('http://127.0.0.1:8000/login/', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        console.log(response.data);
        if(response.status==200){this.$router.push({ path: '/collective/'});}
      });
    },
    gotoSignUp() {
        this.$router.push({ path: '/register'});
    }
  }
}
</script>