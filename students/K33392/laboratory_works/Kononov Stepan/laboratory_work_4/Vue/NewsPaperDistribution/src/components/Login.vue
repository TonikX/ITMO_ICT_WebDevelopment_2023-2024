<template>
  <div class="container mt-5">
    <header>
      <h1 class="text-center">Вход</h1>
    </header>
    <form @submit.prevent="handleLoginFormSubmit" class="col-md-4 mx-auto">
      <div class="mb-3">
        <label for="username" class="form-label">Username:</label>
        <input v-model="username" type="text" id="username" name="username" class="form-control" required>
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Пароль:</label>
        <input v-model="password" type="password" id="password" name="password" class="form-control" required>
      </div>
      <button type="submit" class="btn btn-primary mt-3">Войти</button>

      <div v-if="error" class="alert alert-danger mt-3" role="alert">
        {{ error }}
      </div>
    </form>
    <div class="text-center">
      <p class="mt-3">
        <router-link to="/register">Создать аккаунт</router-link>
      </p>
    </div>
  </div>
  <theme-switcher></theme-switcher>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css';
import ThemeSwitcher from "@/components/ThemeSwitcher.vue";

export default {
  components: {ThemeSwitcher},
  data() {
    return {
      username: '',
      password: '',
      error: null,
      user: null,
    };
  },
  methods: {
    async sendLoginData(loginData) {
      try {
        const response = await fetch('http://127.0.0.1:8000/auth/token/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password
          })
        });

        const responseJson = await response.json();
        this.handleLoginResponse(responseJson);
      } catch (error) {
        console.error('Error:', error);
        this.displayErrorAlert();
      }
    },
    handleLoginResponse(responseJson) {
      if (responseJson.auth_token) {
        localStorage.setItem('authToken', responseJson.auth_token);
        localStorage.setItem('user', JSON.stringify(responseJson.user));
        this.$router.push('/newspapers');
      } else {
        this.displayErrorAlert();
      }
    },
    displayErrorAlert() {
      this.error = 'Неправильный username или пароль. Пожалуйста, попробуйте снова.';
      setTimeout(() => {
        this.error = null;
      }, 3000);
    },
    handleLoginFormSubmit() {
      const loginData = {
        email: this.email,
        password: this.password,
      };
      this.sendLoginData(loginData);
    },
  },
};
</script>


<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}

.alert.fade-in {
  animation: fadeIn 0.5s;
}

.alert.fade-out {
  animation: fadeOut 0.5s;
}
</style>
