<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const classs = ref([])

function getClasses(){
  instance.get('/main/classes/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          classs.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteClass(id){
  instance.delete(`/main/classes/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getClasses()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getClasses()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Классы</h2>
    <template v-for="student_class in classs" :key="student_class.id">
      <v-card
          width="700"
          :title="`${student_class.year}${student_class.letter}`"
      ><v-card-actions>
        <v-btn @click="router.push('/classes/' + student_class.id + '/students/')">
          Смотреть подробнее
        </v-btn>
        <v-btn @click="router.push('/classes/' + student_class.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteClass(student_class.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-class')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
