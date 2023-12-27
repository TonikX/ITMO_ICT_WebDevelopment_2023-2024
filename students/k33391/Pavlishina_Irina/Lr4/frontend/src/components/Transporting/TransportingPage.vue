<script setup>
import {onMounted, ref} from "vue";
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

function getPaper(){
  instance.get(`/system/transporting/${router.currentRoute.value.params.id}/`).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/transporting/${router.currentRoute.value.params.id}/`, rest).then(response => {
        if (response.status === 200){
          router.push('/transporting')
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
      <h2>Перевозка</h2>
      <v-text-field label="Заказ" v-model="form.post_office_order"></v-text-field>
      <v-text-field label="Газета" v-model="form.printing_newspaper"></v-text-field>
      <v-text-field label="Количество" v-model="form.amount"></v-text-field>
      <div v-if="error" class="text-red">
        Возникла ошибка
      </div>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
