<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  full_name : "",
})

function create(){
  instance.post('/main/rooms/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/rooms')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить аудиторию</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Без специализации" v-model="form.base"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
