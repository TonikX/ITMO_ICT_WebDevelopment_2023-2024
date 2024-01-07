<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  student : "",
  schedule : "",
  mark : "",
})

function create(){
  form.value.schedule = router.currentRoute.value.params.id

  instance.post('/main/marks/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/classes')
        }
      }
  ).catch(error => console.log(error))
}



</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить оценку</h2>
      <v-text-field label="Студент" v-model="form.student"></v-text-field>
      <v-text-field label="Оценка" v-model="form.mark"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
