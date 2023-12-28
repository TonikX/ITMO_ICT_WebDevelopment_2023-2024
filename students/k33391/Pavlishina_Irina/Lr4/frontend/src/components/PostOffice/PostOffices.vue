<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const newspapers = ref([])

function getNewspapers(){
  instance.get('/system/post-office/').then(response => {
        if (response.status === 200){
          newspapers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteNewspaper(id){
  instance.delete(`/system/post-office/${id}/`).then(response => {
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
    <h2>Почтовые отделения</h2>
    <template v-for="newspaper in newspapers" :key="newspaper.id">
      <v-card
          width="400"
          :title="`№ ${newspaper.num}`"
          :text="`Адрес: ${newspaper.address}`"
      ><v-card-actions>
        <v-btn @click="router.push('/post-offices/' + newspaper.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteNewspaper(newspaper.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-post-office')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
