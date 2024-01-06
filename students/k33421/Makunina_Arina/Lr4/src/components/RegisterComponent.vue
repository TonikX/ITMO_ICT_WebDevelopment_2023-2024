<script setup>
import { ref } from 'vue';
import { fetchWrapper } from "@/helpers";
import { useAuthStore } from "@/stores";

const baseUrl = import.meta.env.VITE_API_URL;

let email = ref('');
let username = ref('');
let password = ref('');
let confirmPassword = ref('');
let valid = ref(false);

const emailRules = [
  v => !!v || 'Email обязателен',
  v => /.+@.+\..+/.test(v) || 'Email должен быть действительным',
];
const usernameRules = [v => !!v || 'Имя пользователя обязательно'];
const passwordRules = [
  v => !!v || 'Пароль обязателен',
  v => (v && v.length >= 8) || 'Пароль должен содержать минимум 8 символов',
];
const confirmPasswordRules = [
  v => !!v || 'Подтверждение пароля обязательно',
  v => v === password.value || 'Пароли не совпадают',
];

const submit = async () => {
  try {
    const response = await fetchWrapper.post(`${baseUrl}/auth/users/`, {
      email: email.value,
      username: username.value,
      password: password.value,
    });

    console.log('Registration successful:', response);
    router.push('/login');
  } catch (error) {
    console.error('Registration error:', error);
  }
};
</script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col md="6" xs="12">
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Форма регистрации</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="Электронная почта"
                name="email"
                type="email"
              ></v-text-field>

              <v-text-field
                v-model="username"
                :rules="usernameRules"
                label="Имя пользователя"
                name="username"
                type="text"
              ></v-text-field>

              <v-text-field
                v-model="password"
                :rules="passwordRules"
                label="Пароль"
                name="password"
                type="password"
              ></v-text-field>

              <v-text-field
                v-model="confirmPassword"
                :rules="confirmPasswordRules"
                label="Подтвердите пароль"
                name="confirmPassword"
                type="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="secondary" to="/login">У меня уже есть аккаунт</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" :disabled="!valid" @click="submit">Зарегистрироваться</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
