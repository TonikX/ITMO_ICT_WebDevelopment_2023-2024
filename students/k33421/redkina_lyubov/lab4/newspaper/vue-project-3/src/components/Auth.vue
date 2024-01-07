<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="setLogin">
      <label for="username">Username:</label>
      <input v-model="login" type="text" id="username" required />

      <label for="password">Password:</label>
      <input v-model="password" type="password" id="password" required />

      <button type="submit">Login</button>
    </form>

    <router-link to="/registration" class="register-button">
      Register
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Auth',
  data() {
    return {
      login: '',
      password: '',
    };
  },
  methods: {
    async setLogin() {
      try {
        const response = await axios.post(
          'http://127.0.0.1:8000/auth/token/login/',
          {
            username: this.login,
            password: this.password,
          },
          {
            headers: {
              'Content-Type': 'application/json',
              Accept: 'application/json',
            },
          }
        );

        localStorage.setItem('access_token', response.data.access);
        this.$router.push({ name: 'UserProfile' });
      } catch (error) {
        console.error(error);

        if (error.response && error.response.status === 401) {
          this.$router.push({ name: 'ErrorPage' });
        }
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  width: 400%;
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login-container h2 {
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 5px;
}

input {
  margin-bottom: 15px;
  padding: 10px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button,
.register-button {
  background-color: transparent;
  color: #333;
  border: 2px solid #3498db;
  padding: 15px 20px;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
  display: block;
  margin-bottom: 15px;
  width: 100%;
}

button:hover,
.register-button:hover {
  background-color: #3498db;
  color: #fff;
}
</style>
