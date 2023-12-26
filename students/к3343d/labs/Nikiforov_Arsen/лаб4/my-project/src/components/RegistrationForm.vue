<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <label for="username">Имя пользователя:</label>
      <input type="text" id="username" v-model="userData.username" required>

      <label for="email">Электронная почта:</label>
      <input type="email" id="email" v-model="userData.email" required>

      <label for="password">Пароль:</label>
      <input type="password" id="password" v-model="userData.password" required>

      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        username: '',
        email: '',
        password: ''
      }
    };
  },
  methods: {
    async register() {
      try {
        const response = await fetch('http://127.0.0.1:8000/hotel_api/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.userData)
        });

        if (response.status === 201) {
          // Изменено на перенаправление на страницу входа после регистрации
          this.$router.push('/login');
        } else {
          // Обработка ошибок регистрации
          console.error('Ошибка регистрации:', response.statusText);
        }
      } catch (error) {
        console.error('Ошибка регистрации:', error);
      }
    }
  }
};
</script>
