<template>
  <div>
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <input type="text" v-model="userData.username" placeholder="Имя пользователя">
      <input type="email" v-model="userData.email" placeholder="Электронная почта">
      <input type="password" v-model="userData.password" placeholder="Пароль">
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
.registration-form {
  max-width: 400px; /* ограничение максимальной ширины формы */
  margin: 0 auto; /* центрирование формы */
  padding: 20px; /* добавление внутренних отступов */
  border: 1px solid #ccc; /* добавление границы */
  border-radius: 10px; /* скругление углов */
}


.form-group {
margin-bottom: 15px;
}

.form-group label,
.form-group input {
display: block;
width: 100%;
}

.form-group input {
margin-top: 5px;
}
</style>