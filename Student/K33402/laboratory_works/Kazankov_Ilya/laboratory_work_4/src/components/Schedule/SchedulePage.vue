<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  day : "",
  num_lesson : "",
  student_class : "",
  room: "",
  lesson_teacher: ""
})

function getPaper(){
  instance.get(`/main/schedules/${router.currentRoute.value.params.id}/`, {
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
  instance.patch(`/main/schedules/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/schedules')
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
      <h2>Расписание</h2>
      <v-select
          label="День недели"
          v-model="form.day"
          :items="['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']"
      ></v-select>
      <v-text-field label="Порядковый номер урока" v-model="form.num_lesson"></v-text-field>
      <v-text-field label="Класс" v-model="form.student_class"></v-text-field>
      <v-text-field label="Аудитория" v-model="form.room"></v-text-field>
      <v-text-field label="Учитель" v-model="form.lesson_teacher"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
