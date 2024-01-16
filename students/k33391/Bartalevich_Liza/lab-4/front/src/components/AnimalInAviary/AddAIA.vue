<script setup>
import {onMounted, ref} from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()

const form = ref({
  animal: "",
  aviary: "",
})

const objs = ref([])
const objs2 = ref([])


function create(){
  instance.post('/system/who-is-there/', form.value, {
    headers: {
      'Authorization': `Bearer ${Token.token}`
    }
  }).then(response => {
        if (response.status === 201){
          router.push('/who-is-theres')
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

  instance.get('/system/aviaries/', {
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
      <h2>Добавить проживание</h2>
      <v-select
          label="Животное"
          v-model="form.animal"
          :items="objs"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-select
          label="Вольер"
          v-model="form.aviary"
          :items="objs2"
          item-title="name"
          item-value="id"
      ></v-select>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped>

</style>
