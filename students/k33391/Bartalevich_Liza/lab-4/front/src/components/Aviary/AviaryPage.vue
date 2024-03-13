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

function getPaper(){
  instance.get(`/system/aviaries/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(error => console.log(error))

  instance.get(`/system/locations/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          objs.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/aviaries/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/aviarys')
        }
      }
  ).catch(error => console.log(error))
}


onMounted(() => {
  getPaper()
})


</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Вольер</h2>
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
          :items="['true', 'false']"
      ></v-select>
      <v-select
          label="Зимнее место"
          v-model="form.winter_place"
          :items="['true', 'false']"
      ></v-select>
      <v-text-field label="Дополнительно" v-model="form.additional"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

