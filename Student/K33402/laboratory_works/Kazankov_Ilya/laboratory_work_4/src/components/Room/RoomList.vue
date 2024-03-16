<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
const rooms = ref([])
const base = ref([])
const spec = ref([])

function getRooms(){
  instance.get('/main/rooms/', {
    headers: {
      'Authorization': `Token ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          rooms.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function getBase(){
  instance.get('/main/rooms/count_base', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          base.value = response.data
        }
      }
  ).catch(error => console.log(error))

  instance.get('/main/rooms/count_specific', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          spec.value = response.data
        }
      }
  ).catch(error => console.log(error))
}

function deleteRoom(id){
  instance.delete(`/main/rooms/${id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 204){
          getRooms()
        }
      }
  ).catch(error => console.log(error))
}

function start(){
  getRooms()
  getBase()
}
onMounted(() => {start()})

</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Аудитории</h2>
    <v-card
        width="500"
        :title="`${base.base} базовых, ${spec.specific} специализированных`"
    ></v-card>
    <template v-for="room in rooms" :key="room.id">
      <v-card
          width="400"
          :title="room.num"
          :subtitle="`Наличие специализации: ${!room.base}`"
      ><v-card-actions>
        <v-btn @click="router.push('/rooms/' + room.id)">
          Изменить
        </v-btn>
        <v-btn @click="deleteRoom(room.id)">
          Удалить
        </v-btn>
      </v-card-actions></v-card>
    </template>
    <v-btn @click="router.push('/add-room')">Добавить</v-btn>
  </div>
</template>

<style scoped>
</style>
