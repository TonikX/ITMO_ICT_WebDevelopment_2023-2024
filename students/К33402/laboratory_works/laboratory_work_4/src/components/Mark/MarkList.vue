<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const marks = ref([])

function getmarks(){
  instance.get('/main/marks/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          marks.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteMark(id){
  instance.delete(`/main/marks/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getmarks()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getmarks()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Оценки</h2>
    <template v-for="mark in marks" :key="mark.id">
      <v-card
          width="400"
          :title="mark.mark"
          :subtitle="`${mark.student} (ID занятия: ${mark.schedule})`"
      ><v-card-actions>
        <v-btn @click="router.push('/marks/' + mark.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteMark(mark.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-mark')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
