<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'
import moment from "moment"

const formatter = new Intl.DateTimeFormat('us')
const today = formatter.format(new Date()).split('/').reverse().join('-')

const types = ref([])
const selectedType = ref(null)
const size = ref(null)
const price = ref(null)
const amount = ref(null)
const date = ref(null)

 async function fetchTypes() {
     try {
       const response = await axios.get(`http://127.0.0.1:8000/exchange/producttype`,
       { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       console.log(response.data)
       types.value = response.data
     } catch (e) {
       alert('Error: ' + e.toString())
     }
   }

async function createProduct() {
     try {
       const response = await axios.post(`http://127.0.0.1:8000/exchange/product/create/`,
           { type: selectedType.value,
                  manufacturer: sessionStorage.getItem('manufacturer_id'),
                  size: size.value,
                  price: price.value,
                  amount: amount.value,
                  manufacturing_date: moment(date.value).format('YYYY-MM-DD HH:mm:ss') },
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
       selectedType.value = null
       size.value = null
       price.value = null
       amount.value = null
       date.value = null
     } catch (e) {
       alert('Invalid data')
     }
   }

defineExpose({
    createProduct, fetchTypes
})

onMounted(fetchTypes)
</script>


<template>
  <v-select
      label="type"
      :items="types"
      item-title="name"
      item-value="id"
      v-model="selectedType"
  ></v-select>
  <p>size</p>
  <v-text-field v-model="size"></v-text-field>
  <p>price</p>
  <v-text-field v-model="price"></v-text-field>
  <p>amount</p>
  <v-text-field v-model="amount"></v-text-field>
  <p>manufacturing date</p>
  <v-date-picker width="100%" color="lime" v-model="date" :max="today"></v-date-picker>
  <br>
</template>