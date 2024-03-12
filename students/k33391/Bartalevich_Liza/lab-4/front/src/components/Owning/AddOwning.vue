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

function create(){
  instance.post('/system/ownings/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/ownings')
        }
      }
  ).catch(error => console.log(error))
}

function getobjs(){
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

onMounted(() => {
  getobjs()
})


</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Добавить владение</h2>
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
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
