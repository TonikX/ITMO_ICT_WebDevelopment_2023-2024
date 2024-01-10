<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  name:'',
  where_printed:''
})
const addresses = ref()

function create(){
  instance.post('/system/do/where-to-sell/', form.value,{
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          addresses.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Найти куда поступает</h2>
      <v-text-field label="Название газеты" v-model="form.name"></v-text-field>
      <v-text-field label="Где печатается" v-model="form.where_printed"></v-text-field>
      <v-btn @click="create">Найти</v-btn>
    </div>
    <div v-if="error" class="text-red">
      Не найдено
    </div>
    <div v-else-if="addresses">
        <v-card
            width="400"
            :title="`Отделение № ${addresses?.post_office_order.post_office.num}`"
        ></v-card>
    </div>
  </v-app>
</template>

<style scoped>

</style>
