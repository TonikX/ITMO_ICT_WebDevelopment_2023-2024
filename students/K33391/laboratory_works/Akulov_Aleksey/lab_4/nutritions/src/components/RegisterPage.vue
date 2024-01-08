<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Имя пользователя:</label>
        <input id="username" v-model="user.username" type="text" required>
      </div>
      <div>
        <label for="email">Электронная почта:</label>
        <input id="email" v-model="user.email" type="email" required>
      </div>
      <div>
        <label for="password">Пароль:</label>
        <input id="password" v-model="user.password" type="password" required>
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
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
        // Здесь должен быть код для отправки данных на сервер
        // Например: await axios.post('/api/register', this.user)
        this.$router.push('/login');
      } catch (error) {
        console.error(error);
        // Обработка ошибок
      }
    }
  }
}
</script>


<style scoped>

</style>