<script setup>
import { ref } from 'vue'
import axios from "axios"

const items = [
        { text: 'pieces', value: 'pc' },
        { text: 'kilograms', value: 'kg' },
        { text: 'grams', value: 'gr' },
        { text: 'liters', value: 'li' },
        { text: 'milliliters', value: 'ml' }
      ]
const selectedUnits = ref('')
const name = ref('')
const days_valid = ref('')

async function createProductType() {
     try {
       const response = await axios.post(`http://127.0.0.1:8000/exchange/producttype/create/`,
           { name: name.value,
                  days_valid: days_valid.value,
                  units: selectedUnits.value },
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
       name.value = null
       days_valid.value = null
       selectedUnits.value = null
     } catch (e) {
       alert('Invalid data' + e)
     }
   }

defineExpose({
    createProductType
})
</script>


<template>
  <p>name</p>
  <v-text-field v-model="name"></v-text-field>
  <v-select
    label="units"
    :items="items"
    item-title="text"
    item-value="value"
    v-model="selectedUnits"
  ></v-select>
  <p>days_valid</p>
  <v-text-field v-model="days_valid"></v-text-field>
</template>