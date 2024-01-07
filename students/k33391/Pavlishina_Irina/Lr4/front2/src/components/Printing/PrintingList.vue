<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/printing-newspapers/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/printing-newspapers/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getNewspapers()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getNewspapers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Печати</h2>

    <v-btn @click="router.push('/find-where')">Найти поступления</v-btn>
    <v-btn @click="router.push('/find-address')">Найти, где издется газета</v-btn>

    <template v-for="newspaper in newspapers" :key="newspaper.id">
    <v-card
        width="400"
        :title="`(id: ${newspaper.id})`"
        :subtitle="`Газета: ${newspaper.newspaper.name}, Типография: ${newspaper.printer.address}`"
        :text="`Сколько печатать: ${newspaper.how_many_to_print}`"
    ><v-card-actions>
      <v-btn @click="router.push('/printing/' + newspaper.id)">
        Изменить
      </v-btn>
      <v-btn @click="deleteNewspaper(newspaper.id)">
        Удалить
      </v-btn>
    </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-printing')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
