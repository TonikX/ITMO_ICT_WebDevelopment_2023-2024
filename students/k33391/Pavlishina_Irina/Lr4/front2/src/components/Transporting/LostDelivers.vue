<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const delivers = ref([])

function getDelivers(){
  instance.get('/system/do/lost-delivers/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          delivers.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

onMounted(() => {getDelivers()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Список поставок</h2>
    <template v-for="deliver in delivers" :key="deliver.id">
      <v-card
          width="400"
          :title="deliver.id"
          :subtitle="`Отделение почты: ${deliver.post_office}`"
          :text="`Газета: ${deliver.newspaper}`"
      ><v-card-actions>
      </v-card-actions></v-card>
    </template>
  </div>
</template>

<style scoped>
</style>
