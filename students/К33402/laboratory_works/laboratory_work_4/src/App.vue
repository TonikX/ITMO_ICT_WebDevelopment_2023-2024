<template>
    <v-layout class="rounded rounded-md">
      <v-navigation-drawer permanent>
        <v-list-item title="Школьная система"></v-list-item>
        <v-divider></v-divider>
        <template v-if="!Token.token">
        <router-link to="/login" style="text-decoration: none; color: inherit;"><v-list-item link title="Войти"></v-list-item></router-link>
        <router-link to="/register" style="text-decoration: none; color: inherit;"><v-list-item link title="Зарегистрироваться"></v-list-item></router-link>
        </template>
        <v-list-item v-else class="text-red" @click="Token.deleteToken">Выйти</v-list-item>

        <router-link to="/categories" style="text-decoration: none; color: inherit;"><v-list-item link title="Категории"></v-list-item></router-link>
        <router-link to="/rooms" style="text-decoration: none; color: inherit;"><v-list-item link title="Аудитории"></v-list-item></router-link>
        <router-link to="/teachers" style="text-decoration: none; color: inherit;"><v-list-item link title="Учителя"></v-list-item></router-link>
        <router-link to="/teachers-lessons" style="text-decoration: none; color: inherit;"><v-list-item link title="Назначения"></v-list-item></router-link>
        <router-link to="/lessons" style="text-decoration: none; color: inherit;"><v-list-item link title="Предметы"></v-list-item></router-link>
        <router-link to="/classes" style="text-decoration: none; color: inherit;"><v-list-item link title="Классы"></v-list-item></router-link>
        <router-link to="/schedules" style="text-decoration: none; color: inherit;"><v-list-item link title="Расписание"></v-list-item></router-link>
        <router-link to="/marks" style="text-decoration: none; color: inherit;"><v-list-item link title="Оценки"></v-list-item></router-link>

      </v-navigation-drawer>
      <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
       <router-view/>
      </v-main>
    </v-layout>
</template>

<script setup>

import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
</script>

<style>
</style>
