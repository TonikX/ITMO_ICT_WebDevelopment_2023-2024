<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  num: "",
  name : "",
  type: "",
})

const objs = ref([])

function create(){
  instance.post('/system/diets/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/diets')
        }
      }
  ).catch(error => console.log(error))
}


function getRooms(){
  instance.get('/system/food/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200) {
          objs.value = response.data
        }
      }
  ).catch(error => console.log(error))

}

onMounted(() => {
  getRooms()
})

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить диету</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Название" v-model="form.name"></v-text-field>
      <v-select
          label="Тип"
          v-model="form.type"
          :items="objs"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
