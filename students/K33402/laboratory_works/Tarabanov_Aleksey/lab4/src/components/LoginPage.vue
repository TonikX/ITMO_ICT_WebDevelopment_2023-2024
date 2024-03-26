<template>
  <div>
    <h2>Log in</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">USERNAME: </label>
        <input id="username" v-model="username" type="text" required>
      </div>
      <div>
        <label for="password">PASSWORD: </label>
        <input id="password" v-model="password" type="password" required>
      </div>
      <button type="submit">Log in</button>
      <router-link to="/register" style="color: #2fa0ab;">Create your account</router-link>


    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
        username: '',
        password: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
          username: this.username,
          password: this.password,
        });

        const accessToken = response.data.auth_token;
        localStorage.setItem('access_token', accessToken);
        console.log('Login successful. Token:', accessToken);

        this.$router.push('/');

      } catch (error) {
        console.error('Login failed:', error.response.data);
      }
    }

  }
}
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

h2 {
  color: #3bbcb8;
  font-size: 5em;
  margin-bottom: 20px;
  text-align: center;
}

.router-link {
    color: #239db2;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

label {
  margin-bottom: 5px;
}

input {
  margin-bottom: 10px;
  padding: 10px;
  font-size: 1em;
}

button {
  background-color: #3bbcb8;
  color: #ffffff;
  padding: 10px;
  border: none;
  cursor: pointer;
  font-size: 1em;
  border-radius: 4px;
}
</style>
