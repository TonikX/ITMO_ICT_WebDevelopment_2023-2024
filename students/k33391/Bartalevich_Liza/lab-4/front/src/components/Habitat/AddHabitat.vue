<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  name : "",
  location: "",
  characteristic: "",
})

const objs = ref([])

function create(){
  instance.post('/system/habitats/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/habitats')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить зону</h2>
      <v-text-field label="Название" v-model="form.name"></v-text-field>
      <v-text-field label="Локация" v-model="form.location"></v-text-field>
      <v-text-field label="Характеристика" v-model="form.characteristic"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
