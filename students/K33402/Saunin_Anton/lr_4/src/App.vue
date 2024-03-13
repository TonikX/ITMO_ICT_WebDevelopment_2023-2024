<template>
  <v-layout class="rounded rounded-md">
    <v-navigation-drawer permanent style="width: 200px">
      <v-list-item title="Школьная система" class="text"></v-list-item>
      <v-divider></v-divider>
      <template v-if="!Token.token">
        <router-link to="/login" style="text-decoration: none; color: inherit"
          ><v-list-item link title="Войти" class="text1"></v-list-item
        ></router-link>
        <router-link
          to="/register"
          style="text-decoration: none; color: inherit"
          ><v-list-item
            link
            title="Зарегистрироваться"
            class="text1"
          ></v-list-item
        ></router-link>
      </template>
      <v-list-item
        v-else
        class="text-red"
        @click="Token.deleteToken"
        style="text-align: center"
        >Выйти</v-list-item
      >
      <router-link to="/rooms" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Аудитории" class="text"></v-list-item
      ></router-link>
      <router-link to="/teachers" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Учителя" class="text"></v-list-item
      ></router-link>
      <router-link
        to="/teachers-lessons"
        style="text-decoration: none; color: inherit"
        ><v-list-item link title="Назначения" class="text"></v-list-item
      ></router-link>
      <router-link to="/lessons" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Предметы" class="text"></v-list-item
      ></router-link>
      <router-link to="/classes" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Классы" class="text"></v-list-item
      ></router-link>
      <router-link to="/schedules" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Расписание" class="text"></v-list-item
      ></router-link>
      <router-link to="/marks" style="text-decoration: none; color: inherit"
        ><v-list-item link title="Оценки" class="text"></v-list-item
      ></router-link>
    </v-navigation-drawer>
    <v-main
      class="d-flex align-center justify-center"
      style="min-height: 300px"
    >
      <router-view />
    </v-main>
  </v-layout>
</template>

<script setup>
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
</script>

<style scoped>
.d-flex {
  background-color: #1a1a1d;
  min-height: 100vh;
  color: #66fcf1;
}
.text {
  color: #66fcf1;
  text-align: center;
}
.text1 {
  color: #45a29e;
  text-align: center;
}
router-link {
  font-size: 1em !important;
}
</style>
