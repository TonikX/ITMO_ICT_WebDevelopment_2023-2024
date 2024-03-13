<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";


const Token = TokenStore()
const objs = ref({})

function getobjs(){
  instance.get(`/system/locations/${router.currentRoute.value.params.id}/count_animals_in/`, {
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
    <h2>Животные зоны:</h2>
    <v-card
        width="400"
        :title="objs.name"
        :subtitle="`Всего животных: ${objs.count_animals_in}`"
    ></v-card>
    <h3>Список: </h3>
    <template v-for="obj in objs.animals_in" :key="obj.id">
      <v-card
          width="400"
          :title="`${obj.name} (номер: ${obj.num})`"
          :subtitle="`Лет: ${obj.age}`"
      ><v-card-actions>
      </v-card-actions></v-card>
    </template>
  </div>
</template>

<style scoped>
</style>
