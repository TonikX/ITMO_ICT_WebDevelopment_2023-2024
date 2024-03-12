<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  num: "",
  name: "",
  birthday: "",
  type: "",
})

function create(){
  instance.post('/system/workers/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/workers')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить работника</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Название" v-model="form.name"></v-text-field>
      <v-text-field label="Дата рождения (гггг-мм-дд)" v-model="form.birthday"></v-text-field>
      <v-select
          label="Должность"
          v-model="form.type"
          :items="['V', 'W']"
      ></v-select>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
