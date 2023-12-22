<template>
  <div class="login-container">
    <h2>Войти как пациент</h2>
    <form @submit="login" class="login-form">
      <div class="form-field">
        <label for="username">Имя пользователя:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-field">
        <label for="password">Пароль:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit" class="submit-btn">Войти</button>
    </form>
    <div class="register-link">
      <h3>Еще не зарегистрированы?</h3>
      <button><router-link to="/registerpatient">Зарегистрироваться как пациент</router-link></button>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 20px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h2, h3 {
  text-align: center;
}

.login-form .form-field {
  margin-bottom: 15px;
}

.login-form label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.login-form input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.submit-btn {
  width: 100%;
  padding: 10px 15px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #45a049;
}

.register-link {
  text-align: center;
  margin-top: 20px;
}

.register-link button {
  background: none;
  border: none;
  padding: 0;
}

.register-link a {
  color: #4CAF50;
  text-decoration: none;
}
</style>

<script>
import axios from 'axios';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
setup() {
  const username = ref('');
  const password = ref('');
  const router = useRouter();

  const login = async (event) => {
  event.preventDefault();

  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/token/login/', {
      username: username.value,
      password: password.value,
    });

    if (response.data && response.data.auth_token) {
      localStorage.setItem('authToken', response.data.auth_token);
      router.push('/main');
    }
  } catch (error) {
    if (error.response && error.response.status === 400) {
      if (error.response.data.non_field_errors) {
        const errorMessage = error.response.data.non_field_errors[0];
        if (errorMessage == 'Unable to log in with provided credentials.') {
          alert('Неверный пароль');
        } else {
          console.log('Ошибка:', errorMessage);
        }
      } else {
        console.log('Ошибка статуса 400:', error.response.data);
      }
    } else {
      console.log('Другая ошибка:', error);
    }
  }
};

  return {
    username,
    password,
    login
  };
}
};
</script>