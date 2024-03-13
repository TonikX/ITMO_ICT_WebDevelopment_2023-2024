<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  num : "",
  name : "",
  age : "",
  sex : "",
  birthdate : "",
  diet : "",
  winter_place : "",
  winter_sleeping : "",
  normal_temperature : "",
  vet : "",
  cleaner : "",
})

const objs = ref([])
const objs2 = ref([])
const objs3 = ref([])

function create(){
  instance.post('/system/animals/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/animals')
        }
      }
  ).catch(error => console.log(error))
}

function getRooms(){
  instance.get('/system/winter-places/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200) {
          objs.value = response.data
        }
      }
  ).catch(error => console.log(error))

  instance.get('/system/diets/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200) {
          objs2.value = response.data
        }
      }
  ).catch(error => console.log(error))

  instance.get('/system/workers/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200) {
          objs3.value = response.data
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
      <h2>Добавить животное</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Название" v-model="form.name"></v-text-field>
      <v-text-field label="Возраст" v-model="form.age"></v-text-field>
      <v-select
          label="Пол"
          v-model="form.sex"
          :items="['m', 'f']"
      ></v-select>
      <v-text-field label="День рождения (гггг-мм-дд)" v-model="form.birthdate"></v-text-field>
      <v-select
          label="Место зимовки"
          v-model="form.winter_place"
          :items="objs"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-select
          label="Диета"
          v-model="form.diet"
          :items="objs2"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-text-field label="Длительност зимней спячки (в днях)" v-model="form.winter_sleeping"></v-text-field>
      <v-text-field label="Нормальная температура" v-model="form.normal_temperature"></v-text-field>
      <v-select
          label="Ветеринар"
          v-model="form.vet"
          :items="objs3"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-select
          label="Диета"
          v-model="form.cleaner"
          :items="objs3"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
