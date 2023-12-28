<template>
  <form @submit.prevent="login">
    <h2>Вход</h2>
    <div class="input-wrapper">
      <input type="text" v-model="userData.username" placeholder="Имя пользователя">
    </div>
    <div class="input-wrapper">
      <input type="password" v-model="userData.password" placeholder="Пароль">
    </div>
    <button type="submit">Войти</button>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
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
  localStorage.setItem('userToken', data.access);

  // Сохраните имя пользователя в состоянии Vuex
  this.$store.commit('setUser', { username: this.userData.username, token: data.access });

  this.$emit('show-user-profile');
  this.errorMessage = '';
}     
         else {
          this.errorMessage = 'Введите корректные данные';
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
  margin-bottom: 10px;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>
