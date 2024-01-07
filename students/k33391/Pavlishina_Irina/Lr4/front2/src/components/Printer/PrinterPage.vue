<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  name: "",
  address: "",
  max_capacity: "",
})

function getPaper(){
  instance.get(`/system/printer/${router.currentRoute.value.params.id}/`, {
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
  instance.patch(`/system/printer/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/newspapers')
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
      <h2>Типография</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Адрес" v-model="form.address"></v-text-field>
      <v-text-field label="Максимальная производительность" v-model="form.max_capacity"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
