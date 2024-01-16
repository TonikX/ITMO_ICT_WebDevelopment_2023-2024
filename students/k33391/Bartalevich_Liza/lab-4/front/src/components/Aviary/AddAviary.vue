<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  name : "",
  area : "",
  communal : "",
  winter_place : "",
  additional : "",
})

const objs = ref([])

function create(){
  instance.post('/system/aviaries/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/aviarys')
        }
      }
  ).catch(error => console.log(error))
}

function getRooms(){
  instance.get('/system/locations/', {
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
      <h2>Добавить клетку</h2>
      <v-text-field label="Название" v-model="form.name"></v-text-field>
      <v-select
          label="Зона"
          v-model="form.area"
          :items="objs"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-select
          label="Несколько животных"
          v-model="form.communal"
          :items="['True', 'False']"
      ></v-select>
      <v-select
          label="Зимнее место"
          v-model="form.winter_place"
          :items="['True', 'False']"
      ></v-select>
      <v-text-field label="Дополнительно" v-model="form.additional"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
