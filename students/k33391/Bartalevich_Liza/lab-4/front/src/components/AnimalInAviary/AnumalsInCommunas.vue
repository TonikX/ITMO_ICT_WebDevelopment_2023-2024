<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const objs = ref([])

function getobjs(){
  instance.get('/system/animals/animals_in_communas/', {
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
    <h2>Только проживающие в "общежитиях"</h2>
    <template v-for="obj in objs" :key="obj.id">
      <v-card
          width="400"
          :title="`${obj.animal} - ${obj.aviary}`"
      ><v-card-actions>
        <v-btn @click="router.push('/who-is-theres/' + obj.id)">
          Изменить
        </v-btn>

      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-who-is-there')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
