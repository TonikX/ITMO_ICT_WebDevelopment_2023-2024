<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const teachers_lessons = ref([])

function getTeachers(){
  instance.get('/main/teachers-lessons/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          teachers_lessons.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteTeacher(id){
  instance.delete(`/main/teachers-lessons/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getTeachers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getTeachers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Назначения</h2>
    <template v-for="teacher_lesson in teachers_lessons" :key="teacher_lesson.id">
      <v-card
          width="400"
          :title="`${teacher_lesson.teacher.name} ведет ${teacher_lesson.lesson.name}`"
      ><v-card-actions>
        <v-btn @click="router.push('/teachers-lessons/' + teacher_lesson.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteTeacher(teacher_lesson.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-teacher-lesson')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
