<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  amount: "",
  printing_newspaper: "",
  post_office_order: "",
})

function create(){
  instance.post('/system/transporting/', form.value, {
    headers: {
      'Authorization': `${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/transporting')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить перевозку</h2>
      <v-text-field label="Заказ" v-model="form.post_office_order"></v-text-field>
      <v-text-field label="Газета" v-model="form.printing_newspaper"></v-text-field>
      <v-text-field label="Количество" v-model="form.amount"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
