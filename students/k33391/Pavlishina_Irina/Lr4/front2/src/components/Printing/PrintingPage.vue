<script setup>
import {onMounted, ref} from "vue";
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

function getPaper(){
  instance.get(`/system/printing-newspapers/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/printing-newspapers/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/printing')
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
      <h2>Печать</h2>
      <v-text-field label="Газета" v-model="form.newspaper"></v-text-field>
      <v-text-field label="Типография" v-model="form.printer"></v-text-field>
      <v-text-field label="Сколько печатать" v-model="form.how_many_to_print"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
