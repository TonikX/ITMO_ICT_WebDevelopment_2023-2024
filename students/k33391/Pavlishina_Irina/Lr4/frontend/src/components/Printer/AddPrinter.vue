<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  name: "",
  address: "",
  max_capacity: "",
})

function create(){
  instance.post('/system/printer/', form.value, {
    headers: {
      'Authorization': `${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/printers')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить типографию</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Адресс" v-model="form.address"></v-text-field>
      <v-text-field label="Максимальная производительность" v-model="form.max_capacity"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
