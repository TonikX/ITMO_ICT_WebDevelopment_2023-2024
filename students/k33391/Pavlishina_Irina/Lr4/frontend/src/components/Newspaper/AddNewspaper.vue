<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  name: "",
  index: "",
  redactor_last_name: "",
  redactor_first_name: "",
  redactor_patronic: "",
  cost: 0
})

function create(){
  instance.post('/system/newspaper/', form.value, {
    headers: {
      'Authorization': `${Token.token}`
    }
  }).then(response => {
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
      <h2>Добавить газету</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Номер" v-model="form.index"></v-text-field>
      <v-text-field label="Фамилия редактора" v-model="form.redactor_last_name"></v-text-field>
      <v-text-field label="Имя редактора" v-model="form.redactor_first_name"></v-text-field>
      <v-text-field label="Отчество редактора" v-model="form.redactor_patronic"></v-text-field>
      <v-text-field label="Цена" v-model="form.cost"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
