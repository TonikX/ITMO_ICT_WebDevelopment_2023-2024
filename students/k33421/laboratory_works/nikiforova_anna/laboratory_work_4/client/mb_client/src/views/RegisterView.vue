<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="text-h5">Регистрация</v-card-title>
          <v-card-text>
            <v-text-field v-model="username" label="Логин"></v-text-field>
            <v-text-field v-model="password" label="Пароль" type="password"></v-text-field>
            <v-text-field v-model="rePassword" label="Подтвредите пароль" type="password"></v-text-field>
            <v-text-field v-model="email" label="Email"></v-text-field>
            <v-text-field v-model="lastName" label="Фамилия"></v-text-field>
            <v-text-field v-model="firstName" label="Имя"></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn @click="register">Зарегистрироваться</v-btn>
            <v-spacer></v-spacer>
            <v-btn @click="$goTo('/')">Назад</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      rePassword: '',
      email: '',
      firstName: '',
      lastName: '',
    };
  },
  methods: {
    register() {
      axios.post(this.$websiteURL + '/auth/users/', {
        username: this.username,
        password: this.password,
        re_password: this.rePassword,
        email: this.email,
        first_name: this.firstName,
        last_name: this.lastName,
      })
        .then(response => {
          const token = response.data.auth_token; // token field
          localStorage.setItem('token', token);

          alert('Регистрация успешна. Теперь вы можете войти в свой аккаунт');
          this.$router.push('/login');
        })
        .catch(error => {
          const errorMessage = Object.entries(error.response.data)
            .map(([key, value]) => `${key}: ${value}`)
            .join('\n');

          alert(errorMessage);
          console.error('Registration error:', error);
        });
    },
  },
};
</script>
