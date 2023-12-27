<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  how_many_to_print: "",
  newspaper: "",
  printer: "",
})

function create(){
  instance.post('/system/printing-newspapers/', form.value, {
    headers: {
      'Authorization': `${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/printing')
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить печать</h2>
      <v-text-field label="Газета" v-model="form.newspaper"></v-text-field>
      <v-text-field label="Типография" v-model="form.printer"></v-text-field>
      <v-text-field label="Сколько печатать" v-model="form.how_many_to_print"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
