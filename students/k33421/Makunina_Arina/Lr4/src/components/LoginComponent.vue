<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores';

let username = ref('');
let password = ref('');
let valid = ref(false);

const passwordRules = [
  v => !!v || 'Пароль обязателен',
  v => (v && v.length >= 5) || 'Пароль должен быть не менее 5 символов',
];
const usernameRules = [v => !!v || 'Имя пользователя обязательно'];

const submit = async () => {
  if (valid.value) {
    try {
      const authStore = useAuthStore();
      await authStore.login(username.value, password.value);
    } catch (error) {
      if (error.data && error.data.detail) {
        alert(error.data.detail);
      } else {
        alert('Произошла непредвиденная ошибка.');
      }
    }
  }
}
</script>

<template>
  <v-container>
    <v-row justify="center">
      <v-col md="6" xs="12">
        <v-card class="elevation-12">
          <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Вход</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="username"
                :rules="usernameRules"
                label="Имя пользователя"
                name="username"
                type="text"
              ></v-text-field>

              <v-text-field
                label="Пароль"
                name="password"
                type="password"
                v-model="password"
                :rules="passwordRules"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn color="secondary" to="/register">У меня нет аккаунта</v-btn>
            <v-spacer></v-spacer>
            <v-btn color="primary" :disabled="!valid" @click="submit">Войти</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>

</style>
