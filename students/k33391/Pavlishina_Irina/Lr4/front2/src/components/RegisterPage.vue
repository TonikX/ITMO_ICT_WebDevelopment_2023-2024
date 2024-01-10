<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";

const form = ref({
  username: '',
  type: '',
  password: '',
  password2: ''
})

function register(){
  instance.post('/system/register/', form.value).then(response => {
        if (response.status === 201){
          router.push('/newspapers')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Регистрация</h2>
      <v-text-field label="Логин" v-model="form.username"></v-text-field>
      <v-select
          label="Тип"
          v-model="form.type"
          :items="['A', 'P', 'PO', 'N']"
      ></v-select>
      <v-text-field label="Пароль" v-model="form.password"></v-text-field>
      <v-text-field label="Повторите пароль" v-model="form.password2"></v-text-field>
      <v-btn @click="register">Зарегистрироваться</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
