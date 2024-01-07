<script setup>
import {ref} from "vue";
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

function create(){
  instance.post('/main/schedules/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/schedules')
        }
      }
  ).catch(error => console.log(error))
}

</script>

<template>
  day : "",
  num_lesson : "",
  student_class : "",
  room: "",
  lesson_teacher: ""
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить расписание</h2>
      <v-select
          label="День недели"
          v-model="form.day"
          :items="['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']"
      ></v-select>
      <v-text-field label="Порядковый номер урока" v-model="form.num_lesson"></v-text-field>
      <v-text-field label="Класс" v-model="form.student_class"></v-text-field>
      <v-text-field label="Аудитория" v-model="form.room"></v-text-field>
      <v-text-field label="Учитель" v-model="form.lesson_teacher"></v-text-field>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
