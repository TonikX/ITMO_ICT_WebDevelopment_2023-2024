<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const objs = ref([])

function getobjs(){
  instance.get('/system/aviaries/show_empty/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          objs.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteobj(id){
  instance.delete(`/system/aviaries/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getobjs()
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getobjs()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Пустые вольеры</h2>
    <template v-for="obj in objs" :key="obj.id">
      <v-card
          width="400"
          :title="obj.name"
          :subtitle="`${obj.area}`"
          :text="`${obj.additional}`"
      ><v-card-actions>
        <v-btn @click="router.push('/aviarys/' + obj.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteobj(obj.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
  </div>
</template>

<style scoped>
</style>
