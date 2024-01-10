<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";
import {tr} from "vuetify/locale";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  how_many_needed: "",
  newspaper: "",
  post_office: "",
})

function create(){
  error.value = false
  instance.post('/system/ordering-newspapers/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/orders')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Создать заказ</h2>
      <v-text-field label="Отделение" v-model="form.post_office"></v-text-field>
      <v-text-field label="Газета" v-model="form.newspaper"></v-text-field>
      <v-text-field label="Сколько нужно" v-model="form.how_many_needed"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
