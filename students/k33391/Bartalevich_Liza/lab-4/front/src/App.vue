<template>
    <v-layout class="rounded rounded-md">
      <v-navigation-drawer permanent>
        <v-list-item title="Зоопарк"></v-list-item>
        <v-divider></v-divider>
        <template v-if="!Token.token">
        <router-link to="/login" style="text-decoration: none; color: inherit;"><v-list-item link title="Войти"></v-list-item></router-link>
        <router-link to="/register" style="text-decoration: none; color: inherit;"><v-list-item link title="Зарегистрироваться"></v-list-item></router-link>
        </template>
        <v-list-item v-else class="text-red" @click="Token.deleteToken">Выйти</v-list-item>

        <router-link to="/aviarys" style="text-decoration: none; color: inherit;"><v-list-item link title="Вольеры"></v-list-item></router-link>
        <router-link to="/locations" style="text-decoration: none; color: inherit;"><v-list-item link title="Зоны"></v-list-item></router-link>
        <router-link to="/zoos" style="text-decoration: none; color: inherit;"><v-list-item link title="Зоопарки"></v-list-item></router-link>
        <router-link to="/foods" style="text-decoration: none; color: inherit;"><v-list-item link title="Еда"></v-list-item></router-link>
        <router-link to="/diets" style="text-decoration: none; color: inherit;"><v-list-item link title="Диеты"></v-list-item></router-link>
        <router-link to="/habitats" style="text-decoration: none; color: inherit;"><v-list-item link title="Зоны обитания"></v-list-item></router-link>
        <router-link to="/animals" style="text-decoration: none; color: inherit;"><v-list-item link title="Животные"></v-list-item></router-link>
        <router-link to="/winter-places" style="text-decoration: none; color: inherit;"><v-list-item link title="Места зимовки"></v-list-item></router-link>
        <router-link to="/ownings" style="text-decoration: none; color: inherit;"><v-list-item link title="Владение"></v-list-item></router-link>
        <router-link to="/who-is-theres" style="text-decoration: none; color: inherit;"><v-list-item link title="Проживание"></v-list-item></router-link>
        <router-link to="/workers" style="text-decoration: none; color: inherit;"><v-list-item link title="Работники"></v-list-item></router-link>

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
