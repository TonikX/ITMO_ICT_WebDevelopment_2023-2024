<template>
  <div>
    <h2>Регистрация</h2>
    <!-- Форма регистрации -->
    <form @submit.prevent="register">
      <div class="input-wrapper">
        <input type="text" v-model="userData.username" placeholder="Имя пользователя">
      </div>
      <div class="input-wrapper">
        <input type="password" v-model="userData.password" placeholder="Пароль">
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>

    <!-- Сообщение об успешной регистрации -->
    <div v-if="registrationSuccess" class="success-message">
      Регистрация прошла успешно! Теперь вы можете войти.
    </div>
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
      },
      registrationSuccess: false, // Добавляем переменную для отслеживания успешной регистрации
    };
  },
  methods: {
    async register() {
      try {
        const response = await fetch('http://localhost:8000/hotel_api/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.userData)
        });

        if (response.ok) {
          const data = await response.json();
          console.log('Успешная регистрация', data);
          this.registrationSuccess = true; // Устанавливаем успешную регистрацию в true
        } else {
          console.error('Ошибка регистрации', response.statusText);
        }
      } catch (error) {
        console.error('Ошибка сети', error);
      }
    }
  }
};
</script>

<style scoped>
.navigation-links {
  text-align: center;
  margin-bottom: 20px;
}

.navigation-links a {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.navigation-links a:hover {
  color: #007bff;
  text-decoration: underline;
}

.input-wrapper {
  margin-bottom: 10px; /* Расстояние между полями ввода */
}

.success-message {
  color: green;
  margin-top: 10px;
}
</style>
