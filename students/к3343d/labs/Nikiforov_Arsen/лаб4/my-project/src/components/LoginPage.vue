<template>
  <form @submit.prevent="login">
    <h2>Войти</h2>
    <div class="input-wrapper">
      <input type="text" v-model="userData.username" placeholder="Имя пользователя">
    </div>
    <div class="input-wrapper">
      <input type="password" v-model="userData.password" placeholder="Пароль">
    </div>
    <button type="submit">Войти</button>
    <div v-if="token">Токен: {{ token }}</div>
  </form>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        username: '',
        password: '',
      },
      errorMessage: '',
      token: '', // Состояние для хранения токена
    };
  },
  methods: {
    async login() {
  try {
    const response = await fetch('http://localhost:8000/hotel_api/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: this.userData.username,
        password: this.userData.password
      })
    });

// В вашем методе login
if (response.ok) {
  const data = await response.json();
  this.token = data.access; // Сохраняем токен доступа
  // TODO: Сохранить токен в localStorage или Vuex для последующего использования
}
else {
      console.error('Ошибка аутентификации', await response.text());
    }
  } catch (error) {
    console.error('Ошибка сети', error);
  }
}



  }
};
</script>

<style>
.input-wrapper {
  margin-bottom: 10px; /* Расстояние между полями ввода */
}
</style>
