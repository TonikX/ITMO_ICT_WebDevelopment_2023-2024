<template>
  <div class="container mt-5">
    <form @submit.prevent="register">
      <header>
        <h1>Регистрация</h1>
      </header>
      <div class="mb-3">
        <label for="username" class="form-label">Имя пользователя:</label>
        <input v-model="registerData.username" type="text" id="username" name="username" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="first_name" class="form-label">Имя:</label>
        <input v-model="registerData.first_name" type="text" id="first_name" name="first_name" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">Фамилия:</label>
        <input v-model="registerData.last_name" type="text" id="last_name" name="last_name" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input v-model="registerData.email" type="email" id="email" name="email" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="middle_name" class="form-label">Отчество:</label>
        <input v-model="registerData.middle_name" type="text" id="middle_name" name="middle_name" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Пароль:</label>
        <input v-model="registerData.password" type="password" id="password" name="password" class="form-control" required minlength="6">
      </div>
      <div class="mb-3 text-danger">{{ errorMessage }}</div>
      <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
    </form>

    <div class="text-center">
      <p class="mt-3">
        Уже есть аккаунт?
        <router-link to="/">Войти</router-link>
      </p>
    </div>
    <div class="bottom-right-container">
      <svg class="themeIcon" id="themeIcon" role="img">
      </svg>
    </div>
  </div>

  <theme-switcher></theme-switcher>

</template>

<script>
import ThemeSwitcher from "@/components/ThemeSwitcher.vue";

export default {
  components: {ThemeSwitcher},
  data() {
    return {
      registerData: {
        first_name: '',
        last_name: '',
        username: '',
        email: '',
        password: '',
        middle_name: '',
      },
      errorMessage: '',
    };
  },
  methods: {
    async register() {
      try {
        this.errorMessage = '';

        // Отправляем запрос на регистрацию
        await fetch('http://127.0.0.1:8000/auth/users/', {
          method: 'POST',
          body: JSON.stringify(this.registerData),
          headers: {
            'Content-Type': 'application/json',
          },
        });

        // Отправляем запрос на получение токена
        const response = await fetch('http://127.0.0.1:8000/auth/token/login/', {
          method: 'POST',
          body: JSON.stringify({
            username: this.registerData.username,
            password: this.registerData.password,
          }),
          headers: {
            'Content-Type': 'application/json',
          },
        });

        const data = await response.json();

        if (response.ok) {
          localStorage.setItem('authToken', data.auth_token);

          this.$router.push('/newspapers');
        } else {
          this.errorMessage = 'Ошибка при получении токена. Пожалуйста, попробуйте еще раз.';
        }
      } catch (error) {
        this.errorMessage = 'Ошибка при регистрации. Пожалуйста, попробуйте еще раз.';
      }
    },
  },
  mounted() {},
};
</script>



<style scoped>
</style>
