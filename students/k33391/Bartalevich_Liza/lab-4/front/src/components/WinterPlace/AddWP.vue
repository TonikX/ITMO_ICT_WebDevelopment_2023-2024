<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  code : "",
  name : "",
  date_to : "",
  date_from : "",
})

function create(){
  instance.post('/system/winter-places/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/winter-places')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить место зимовки</h2>
      <v-text-field label="Код" v-model="form.code"></v-text-field>
      <v-text-field label="Название" v-model="form.name"></v-text-field>
      <v-text-field label="С" v-model="form.date_from"></v-text-field>
      <v-text-field label="До" v-model="form.date_to"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
