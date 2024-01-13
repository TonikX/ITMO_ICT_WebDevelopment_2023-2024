<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const lessons = ref([])
const headrs = [{
  title: 'Студент',
  value: 'name'
},
  {
    title: 'Оценки',
    value: 'marks'
  },
  {
    title: 'Среднее',
    value: 'mean'
  },
]

function getClasses(){
  instance.get( `/main/classes/${router.currentRoute.value.params.id}/statistics/`, {
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

onMounted(() => {getClasses()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Оценки по предметам</h2>
    <template v-for="lesson in lessons" :key="lesson.id">
      <v-card
        width="700"
        :title="lesson.name"
      ></v-card>

      <v-data-table :items="lesson.students" :headers="headrs"> </v-data-table>
    </template>
  </div>
</template>

<style scoped>
</style>
