<script setup>
import axios from "axios"
import moment from "moment"
import {onMounted, ref} from 'vue'

const formatter = new Intl.DateTimeFormat('us')
const today = formatter.format(new Date()).split('/').reverse().join('-')


const toggle = ref('new')
const date = ref(null)
const selectedManufacturer = ref(null)
let manufacturers = []

 async function fetchManufacturers() {
     try {
       const response = await axios.get('http://127.0.0.1:8000/exchange/manufacturer')
       console.log(response.data)
       manufacturers = response.data
     } catch (e) {
       alert('Error: ' + e.toString())
     }
   }

const name = ref('')
const address = ref('')
const ceo = ref('')

async function registerRole() {
     try {
       if (toggle.value === 'new') {
         const response = await axios.post(`http://127.0.0.1:8000/exchange/manufacturer/create/`,
             {
               name: name.value,
               address: address.value,
               ceo: ceo.value,
               establishment_date: moment(date.value).format('YYYY-MM-DD')
             },
             {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
         )
         sessionStorage.setItem('manufacturer_id', response.data.id)
       }
       if (toggle.value === 'existing') {
         sessionStorage.setItem('manufacturer_id', selectedManufacturer.value)
       }
       const response = await axios.patch("http://127.0.0.1:8000/auth/users/me/",
           { manufacturer: sessionStorage.getItem('manufacturer_id') },
         { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
     } catch (e) {
       alert('Invalid data')
     }
   }

defineExpose({
    registerRole
})

onMounted(fetchManufacturers)
</script>

<template>
  <div class="d-flex align-center flex-column">
    <v-btn-toggle
      v-model="toggle"
      divided
      variant="outlined"
    >
      <v-btn value="new">new company</v-btn>
      <v-btn value="existing">existing company</v-btn>
    </v-btn-toggle>
  </div>
  <br>
  <div v-if="toggle === 'new'">
    <p>name</p>
    <v-text-field v-model="name"></v-text-field>
    <p>address</p>
    <v-text-field v-model="address"></v-text-field>
    <p>ceo</p>
    <v-text-field v-model="ceo"></v-text-field>
    <p>establishment date</p>
    <v-date-picker width="100%" color="lime" v-model="date" :max="today"></v-date-picker>
    <br>
  </div>
  <div v-if="toggle === 'existing'">
    <v-select
      label="manufacturer"
      :items="manufacturers"
      item-title="name"
      item-value="id"
      v-model="selectedManufacturer"
      style="margin-bottom:20%"
    ></v-select>
  </div>
</template>