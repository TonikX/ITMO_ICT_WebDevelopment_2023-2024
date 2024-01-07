<template>
  <div class="container mt-5">
    <form @submit.prevent="register">
      <header>
        <h1>Регистрация</h1>
      </header>
      <div class="mb-3">
        <label for="username" class="form-label">Имя пользователя :</label>
        <input v-model="registerData.username" type="text" id="username" name="username" class="form-control"
               required>
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email:</label>
        <input v-model="registerData.email" type="email" id="email" name="email" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="middle_name" class="form-label">Отчество:</label>
        <input v-model="registerData.middle_name" type="text" id="middle_name" name="middle_name" class="form-control"
               required>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Пароль:</label>
        <input v-model="registerData.password" type="password" id="password" name="password" class="form-control"
               required minlength="6">
      </div>
      <div class="mb-3 text-danger">{{ errorMessage }}</div>
      <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
    </form>

    <div class="text-center цщ">
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
</template>

<script>

export default {
  data() {
    return {
      registerData: {
        username: '',
        email: '',
        password: '',
        middle_name: ''
      },
      errorMessage: '',
    };
  },
  methods: {
    async register()
    {
      try {
        this.errorMessage = '';
        const response = await fetch('http://127.0.0.1:8000/auth/users/', {
          method: 'POST',
          body: JSON.stringify(this.registerData),
          headers: {
            'Content-Type': 'application/json',
          },
        });
        await response.json();

        this.$router.push('/newspapers')

      } catch (error) {
        this.errorMessage = 'Ошибка при регистрации. Пожалуйста, попробуйте еще раз.';
      }
    }

    ,
  },
  mounted() {

  },
};
</script>


<style scoped>

</style>
