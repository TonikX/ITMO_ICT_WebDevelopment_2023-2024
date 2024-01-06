<template>
  <div class="container">
    <form @submit.prevent="register">
      <h2 class="mb-3">Регистрация</h2>
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
        Есть аккаунт? <span @click="gotoSignIn">Авторизироваться</span>
      </div>
      <button type="submit" class="mt-4 btn-pers" id="login_button" @click="signup">
        Зарегистрироваться 
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
    signup() {
      axios.post('http://127.0.0.1:8000/register/', {
        username: this.username,
        password: this.password
      })
      .then(response => {
        console.log(response.data);
        if(response.status==200){this.$router.push({ path: '/login/'});}
      });
    },
    gotoSignIn() {
        this.$router.push({ path: '/login'});
    }
  }
}
</script>