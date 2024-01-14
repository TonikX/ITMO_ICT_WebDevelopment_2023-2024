<template>
  <v-container class="mt-10">
    <v-row justify="center">
      <v-col cols="12" class="text-center">
        <h1>Страница заместителя декана</h1>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Преподаватели</v-card-title>
          <v-card-actions>
            <v-btn text color="primary" @click="goToTeachers">Перейти</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      <v-col cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>Учебные группы</v-card-title>
          <v-card-actions>
            <v-btn text color="primary" @click="goToGroups">Перейти</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" class="text-center mt-4">
        <v-btn @click="logout" color="error" dark>Выход</v-btn>
      </v-col>
    </v-row>

  </v-container>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth.store.js';
import { fetchWrapper } from "@/helpers";

const router = useRouter()

const goToTeachers = () => {
  router.push('/teachers')
}

const goToGroups = () => {
  router.push('/groups')
}

const logout = async () => {
  try {
    const authStore = useAuthStore();
    await fetchWrapper.post('/auth/logout/');

    authStore.logout();
    router.push('/login');
  } catch (error) {
    console.error("Error during logout:", error);
  }
};
</script>

<style>
  .mt-10 {
    margin-top: 10px;
  }
</style>
