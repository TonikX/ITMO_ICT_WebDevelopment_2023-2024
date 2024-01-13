<script setup>
import {ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const error = ref(false)

const form = ref({
  day : "",
  num_lesson : "",
  room: "",
})

const schedules = ref()

function find(){
  instance.post('/main/schedules/find/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          schedules.value = response.data
        }
      }
  ).catch(e => error.value = true )
}

</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Найти расписание:</h2>
      <v-text-field label="День недели" v-model="form.day"></v-text-field>
      <v-text-field label="Номер урока" v-model="form.num_lesson"></v-text-field>
      <v-text-field label="Номер удитории" v-model="form.room"></v-text-field>
      <v-btn @click="find">Найти</v-btn>
    </div>
    <div v-if="error" class="text-red">
      Не найдено
    </div>
    <div v-else-if="schedules">
      <template v-for="schedule in schedules" :key="schedule">
        <v-card
            width="400"
            :title="`${schedule.day}, ${schedule.num_lesson}`"
            :subtitle="`${schedule.student_class}, ${schedule.teacher}, ${schedule.lesson}`"
        ></v-card>
      </template>

    </div>
  </v-app>
</template>

<style scoped>

</style>