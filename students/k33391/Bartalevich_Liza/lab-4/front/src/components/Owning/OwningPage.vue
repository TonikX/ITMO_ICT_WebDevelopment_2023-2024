<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  animal: "",
  in_lease: "",
  owner: "",
  here_now: "",
  since: "",
})

const objs = ref([])
const objs2 = ref([])


function getPaper(){
  instance.get(`/system/ownings/${router.currentRoute.value.params.id}/`, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          form.value = response.data
        }
      }
  ).catch(error => console.log(error))

  instance.get('/system/animals/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200) {
          objs.value = response.data
        }
      }
  ).catch(error => console.log(error))

  instance.get('/system/other-zoos/', {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200) {
          objs2.value = response.data
        }
      }
  ).catch(error => console.log(error))

}

function savePaper(){
  const {id, ...rest} = form.value
  instance.patch(`/system/ownings/${router.currentRoute.value.params.id}/`, rest, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 200){
          router.push('/ownings')
        }
      }
  ).catch(error => console.log(error))
}


onMounted(() => {
  getPaper()
})


</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Владение</h2>
      <v-select
          label="Животное"
          v-model="form.animal"
          :items="objs"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-select
          label="В аренде"
          v-model="form.in_lease"
          :items="['True', 'False']"
      ></v-select>
      <v-select
          label="Владелец"
          v-model="form.owner"
          :items="objs2"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-select
          label="Находится сейчас"
          v-model="form.here_now"
          :items="objs2"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-text-field label="Начиная с (гггг-мм-дд)" v-model="form.since"></v-text-field>
      <v-btn @click="savePaper">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>

