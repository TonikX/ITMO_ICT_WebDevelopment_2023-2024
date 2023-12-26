<template>
  <!-- Existing template code -->
  <form @submit.prevent="login">
    <h2>Войти</h2>
    <!-- form fields -->
    <div class="input-wrapper">
      <input type="text" v-model="userData.username" placeholder="Имя пользователя">
    </div>
    <div class="input-wrapper">
      <input type="password" v-model="userData.password" placeholder="Пароль">
    </div>
    <button type="submit">Войти</button>
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
        const response = await fetch('http://localhost:8000/hotel_api/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            username: this.userData.username,
            password: this.userData.password
          })
        });

        if (response.ok) {
          const data = await response.json();
          this.$store.commit('setUser', data); // Обновление состояния пользователя
          this.$router.push('/user-profile'); // Перенаправление на страницу профиля
        } else {
          this.errorMessage = 'Неверные учетные данные';
        }
      } catch (error) {
        console.error('Ошибка сети', error);
      }
    },
    

    logout() {
    // Логика для выхода пользователя
    this.$store.commit('clearUser'); // Очищаем данные пользователя в хранилище
    this.$router.push('/login'); // Перенаправляем на страницу входа
  }
  }
};
</script>

<style>
.input-wrapper {
  margin-bottom: 10px; /* Расстояние между полями ввода */
}
</style>

