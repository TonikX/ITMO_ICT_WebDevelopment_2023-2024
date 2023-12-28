<template>
  <form @submit.prevent="login">
    <h2>Вход</h2>
    <div class="input-wrapper">
      <input type="text" v-model="userData.username" placeholder="Имя пользователя">
    </div>
    <div class="input-wrapper">
      <input type="password" v-model="userData.password" placeholder="Пароль">
    </div>
    <button type="submit">Получить токен</button>
    <!-- Добавленный элемент для отображения сообщения об ошибке -->
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    <div v-if="token">Токен: {{ token }}</div>
  </form>

  <!-- форма для входа по токену -->
  <form @submit.prevent="loginWithToken">
    <h2>Войти с токеном</h2>
    <div class="input-wrapper">
      <input type="text" v-model="token" placeholder="Введите токен">
    </div>
    <button @click="loginWithTokenClick">Войти с токеном</button>
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
      token: '',
      errorMessage: '',
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
          body: JSON.stringify(this.userData)
        });

        if (response.ok) {
          const data = await response.json();
          this.token = data.access;
          localStorage.setItem('userToken', data.access);
          this.errorMessage = ''; // Сброс сообщения об ошибке
        } else {
          this.errorMessage = 'Введите корректные данные'; // Обновленное сообщение об ошибке
        }
      } catch (error) {
        console.error('Ошибка сети', error);
      }
    },
    loginWithTokenClick() {
      if (this.token) {
        localStorage.setItem('userToken', this.token);
        this.$emit('show-user-profile');
      } else {
        this.errorMessage = 'Введите токен';
      }
    }
  }
};
</script>

<style>
.input-wrapper {
  margin-bottom: 10px;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>
