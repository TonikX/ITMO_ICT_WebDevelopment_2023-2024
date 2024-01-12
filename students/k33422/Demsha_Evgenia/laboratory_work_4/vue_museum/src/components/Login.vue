<template>
  <div class="login-form">
    <h1>Авторизация</h1>
    <input v-model="login" type="text" placeholder="Логин"/>
    <input v-model="password" type="password" placeholder="Пароль"/>
    <button @click="setLogin">Войти</button>
  </div>
</template>

<script>
import $ from 'jquery';

export default {
  name: 'Login',

  data() {
    return {
      login: '',
      password: '',
    };
  },

  methods: {
    setLogin() {
      $.ajax({
        url: 'http://127.0.0.1:8000/auth/token/login',
        type: 'POST',
        data: {
          username: this.login,
          password: this.password,
        },
        success: (response) => {
          alert('Спасибо что Вы с нами');

          // Save the auth token in session storage
          // sessionStorage.setItem('auth_token', response.data.attributes.auth_token);

          // Navigate to the foundations route
          this.$router.push({ name: 'FoundationList' });
        },
        error: (response) => {
          if (response.status === 400) {
            alert('Логин или пароль не верен');
          }
        },
      });
    },
  },
};
</script>

<style scoped>
.login-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

input[type="text"],
input[type="password"] {
  padding: 10px;
  margin: 10px;
  border: none;
  border-radius: 5px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
}

button {
  padding: 10px;
  margin: 10px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
</style>
