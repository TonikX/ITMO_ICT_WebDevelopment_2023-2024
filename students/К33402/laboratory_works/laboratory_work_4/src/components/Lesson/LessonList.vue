<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const lessons = ref([])

function getLessons(){
  instance.get('/main/lessons/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          lessons.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteLesson(id){
  instance.delete(`/main/lessons/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getLessons()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getLessons()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Предметы</h2>
    <v-btn @click="router.push('/count-teachers')">Статистика по числу учителей</v-btn>
    <template v-for="lesson in lessons" :key="lesson.id">
      <v-card
          width="400"
          :title="lesson.name"
      ><v-card-actions>
        <v-btn @click="router.push('/lessons/' + lesson.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteLesson(lesson.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-lesson')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
