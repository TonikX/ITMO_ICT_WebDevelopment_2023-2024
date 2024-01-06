<template>
  <v-app id="app">
    <v-main class="flex items-center justify-center min-h-screen">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card class="rounded-lg shadow-md">
              <v-card-title class="text-center">
                <h1 class="text-3xl font-bold text-gray-800 mb-6">Вход в систему</h1>
              </v-card-title>

              <v-card-text>
                <v-form ref="loginForm" @submit.prevent="login">
                  <v-text-field
                    v-model="username"
                    label="Имя пользователя"
                    placeholder="Введите имя пользователя"
                    outlined
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    label="Пароль"
                    placeholder="Введите пароль"
                    type="password"
                    outlined
                  ></v-text-field>

                  <v-btn type="submit" class="w-full" color="indigo" dark>
                    Войти
                  </v-btn>
                </v-form>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores';
import {router} from "@/helpers";

const authStore = useAuthStore();

const username = ref('');
const password = ref('');

const login = async () => {
  try {
    const formData = new FormData();
    formData.append('username', username.value);
    formData.append('password', password.value);

    const response = await fetch('/journal/api/login/', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      const data = await response.json();
      if (data) {
        authStore.setToken(data.auth_token);
        authStore.setRole(data.role);
        console.log('Role:', data.role);

        // Log the authStore.role just before navigating
        console.log('Auth Store Role:', authStore.role);

        // Redirect to the student's cabinet after successful login
        if (data.role === 'student') {
          router.push({ name: 'student-cabinet' });
        }

        console.log('Login successful');
      } else {
        console.error('Authentication failed: Empty response');
      }
    } else {
      const errorData = await response.json();
      console.error(`Authentication failed: ${errorData.error}`);
    }
  } catch (error) {
    console.error('Error during authentication:', error);
  }
};


</script>
