<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  num: "",
  address: "",
})

function getPaper(){
  instance.get(`/system/post-office/${router.currentRoute.value.params.id}/`).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/post-office/${router.currentRoute.value.params.id}/`, rest).then(response => {
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
      <h2>Почтовое отделение</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Адресс" v-model="form.address"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
