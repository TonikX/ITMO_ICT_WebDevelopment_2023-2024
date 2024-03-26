<template>
  <div>
    <h2>Create your account</h2>
    <form @submit.prevent="register">
      <div style="display: flex;">
        <div style="flex: 1;">
          <div style="margin-bottom: 10px;">
            <label for="username" style="display: inline-block; width: 100px;">Username: </label>
            <input id="username" v-model="user.username" type="text" required>
          </div>
          <div style="margin-bottom: 10px;">
            <label for="email" style="display: inline-block; width: 100px;">Email: </label>
            <input id="email" v-model="user.email" type="email" required>
          </div>
          <div>
            <label for="password" style="display: inline-block; width: 100px;">Password: </label>
            <input id="password" v-model="user.password" type="password" required>
          </div>
        </div>
        <div style="flex: 1;">
          <!-- Вторая колонка -->
        </div>
      </div>

      <button type="submit">Create account</button>
      <router-link to="/login">Log in</router-link>
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
        console.log('Registration successful', response.data);

        const response_login = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
          username: this.user.username,
          password: this.user.password,
        });

        const accessToken = response_login.data.auth_token;
        localStorage.setItem('access_token', accessToken);
        console.log('Login successful. Token:', accessToken);

        this.$router.push('/');
      } catch (error) {
        console.error('Ошибка при регистрации:', error.response.data);
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