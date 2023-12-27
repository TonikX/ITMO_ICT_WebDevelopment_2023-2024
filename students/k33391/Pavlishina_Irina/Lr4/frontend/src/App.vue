<template>
    <v-layout class="rounded rounded-md">
      <v-navigation-drawer permanent>
        <v-list-item title="Newspapers"></v-list-item>
        <v-divider></v-divider>
        <template v-if="!Token.token">
        <router-link to="/login" style="text-decoration: none; color: inherit;"><v-list-item link title="Войти"></v-list-item></router-link>
        <router-link to="/register" style="text-decoration: none; color: inherit;"><v-list-item link title="Зарегистрироваться"></v-list-item></router-link>
        </template>
        <v-list-item v-else class="text-red" @click="Token.deleteToken">Выйти</v-list-item>
        <router-link to="/newspapers" style="text-decoration: none; color: inherit;"><v-list-item link title="Газеты"></v-list-item></router-link>
        <router-link to="/post-offices" style="text-decoration: none; color: inherit;"><v-list-item link title="Почтовые отделения"></v-list-item></router-link>
        <router-link to="/orders" style="text-decoration: none; color: inherit;"><v-list-item link title="Заказы газет"></v-list-item></router-link>
        <router-link to="/printers" style="text-decoration: none; color: inherit;"><v-list-item link title="Типографии"></v-list-item></router-link>
        <router-link to="/printing" style="text-decoration: none; color: inherit;"><v-list-item link title="Печати"></v-list-item></router-link>
        <router-link to="/transporting" style="text-decoration: none; color: inherit;"><v-list-item link title="Перевозка"></v-list-item></router-link>
        <router-link to="/report" style="text-decoration: none; color: inherit;"><v-list-item link title="Отчет"></v-list-item></router-link>
        <router-link to="/find-address" style="text-decoration: none; color: inherit;"><v-list-item link title="Найти адрес"></v-list-item></router-link>
        <router-link to="/find-price" style="text-decoration: none; color: inherit;"><v-list-item link title="Найти по цене"></v-list-item></router-link>
        <router-link to="/find-where" style="text-decoration: none; color: inherit;"><v-list-item link title="Найти куда поступает"></v-list-item></router-link>
        <router-link to="/lost-delivers" style="text-decoration: none; color: inherit;"><v-list-item link title="Потерянные доставки"></v-list-item></router-link>
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
