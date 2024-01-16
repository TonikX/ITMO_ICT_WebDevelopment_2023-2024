<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const objs = ref([])

function getobjs(){
  instance.get('/system/ownings/show_in_lease/', {
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
  instance.delete(`/system/ownings/${id}/`, {
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
    <h2>Животные в аренде</h2>
    <template v-for="obj in objs" :key="obj.id">
      <v-card
          width="400"
          :title="`${obj.animal} в ${obj.here_now}`"
          :subtitle="`В аренде: ${obj.in_lease}`"
          :text="`Владелец ${obj.owner}`"
      ><v-card-actions>
        <v-btn @click="router.push('/ownings/' + obj.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteobj(obj.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-owning')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
