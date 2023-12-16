<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="text-h5">Вход</v-card-title>
          <v-card-text>
            <v-text-field v-model="username" label="Логин"></v-text-field>
            <v-text-field v-model="password" label="Пароль" type="password"></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-btn @click="login">Войти</v-btn>
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
    };
  },
  methods: {
    login() {
      axios.post(this.$websiteURL + '/auth/token/login/', {
        username: this.username,
        password: this.password,
      })
        .then(response => {
          const token = response.data.auth_token;
          localStorage.setItem('token', token);
          this.$router.push('/');
        })
        .catch(error => {
            const errorMessage = Object.entries(error.response.data)
              .map(([key, value]) => `${key}: ${value}`)
              .join('\n');

            alert(errorMessage);
            console.error('Login error:', error);
          }
        );
    },
  },
};
</script>
