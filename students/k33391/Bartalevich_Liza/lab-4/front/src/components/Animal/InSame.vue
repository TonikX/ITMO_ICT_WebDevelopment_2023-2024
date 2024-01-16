<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const objs = ref([])

function getobjs(){
  instance.get(`/system/animals/${router.currentRoute.value.params.id}/in_the_same_aviary/`, {
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

onMounted(() => {getobjs()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Животные в одной клетке</h2>
    <template v-for="obj in objs" :key="obj.id">
      <v-card
          width="400"
          :title="`${obj.name} (номер: ${obj.num})`"
          :subtitle="`Лет: ${obj.age}`"
      ><v-card-actions>
        <v-btn @click="router.push('/animals/' + obj.id)">
          Изменить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-animal')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
