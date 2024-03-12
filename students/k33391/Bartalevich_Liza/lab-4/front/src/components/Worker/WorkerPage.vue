<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  num: "",
  name: "",
  birthday: "",
  type: "",
})


function getPaper(){
  instance.get(`/system/workers/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(error => console.log(error))

}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/workers/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/workers')
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
      <h2>Работник</h2>
      <v-text-field label="Номер" v-model="form.num"></v-text-field>
      <v-text-field label="Название" v-model="form.name"></v-text-field>
      <v-text-field label="Дата рождения (гггг-мм-дд)" v-model="form.birthday"></v-text-field>
      <v-select
          label="Должность"
          v-model="form.type"
          :items="['V', 'W']"
      ></v-select>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

