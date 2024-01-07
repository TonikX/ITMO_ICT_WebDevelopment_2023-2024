<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const schedules = ref([])

function getSchedules(){
  instance.get('/main/schedules/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          schedules.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteSchedule(id){
  instance.delete(`/main/schedules/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getSchedules()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getSchedules()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Расписание</h2>
    <v-btn @click="router.push('/find-concrete')">Искать конкретно</v-btn>
    <template v-for="schedule in schedules" :key="schedule.id">
      <v-card
          width="400"
          :title="`${schedule.day}, ${schedule.num_lesson}`"
          :subtitle="`${schedule.student_class}, ${schedule.teacher}, ${schedule.lesson}`"
      ><v-card-actions>
        <v-btn @click="router.push('/schedules/' + schedule.id + '/add-mark/')">
          Добавить оценку
        </v-btn>
        <v-btn @click="router.push('/schedules/' + schedule.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteSchedule(schedule.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-schedule')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
