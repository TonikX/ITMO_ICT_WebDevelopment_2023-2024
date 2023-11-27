<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'

const products = ref([])
let fetching = ref(true)

 async function fetchProducts() {
    try {
       fetching.value = true
       const man = sessionStorage.getItem('manufacturer_id')
       const params = (Boolean(man)) ? {manufacturer: sessionStorage.getItem('manufacturer_id')} : {}
       const response = await axios.get(`http://127.0.0.1:8000/exchange/product`,
           { params: params,
             headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       console.log(response.data)
       products.value = response.data
     } catch (e) {
       alert('Error: ' + e.toString())
     } finally {
       fetching.value = false
     }
   }

defineExpose({
    fetchProducts
})

onMounted(fetchProducts)
</script>


<template>
  <v-btn variant="outlined" @click="fetchProducts" style="margin-bottom: 20px; margin-left: 20px">
          Update
  </v-btn>
  <div class="text-center" v-if="fetching">
    <v-progress-circular
      indeterminate
      color="white"
      style="margin-bottom: 10%"
    ></v-progress-circular>
  </div>
  <v-table density="compact" v-else>
    <thead>
      <tr>
        <th class="text-left">
          Id
        </th>
        <th class="text-left">
          Type
        </th>
        <th class="text-left">
          Size
        </th>
        <th class="text-left">
          Price
        </th>
        <th class="text-left">
          Amount
        </th>
        <th class="text-left">
          Manufacturing Date
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in products"
        :key="item.id"
      >
        <td>{{ item.id }}</td>
        <td>{{ item.type.name + ' ' + item.type.units }}</td>
        <td>{{ item.size }}</td>
        <td>{{ item.price }}</td>
        <td>{{ item.amount }}</td>
        <td>{{ item.manufacturing_date }}</td>
      </tr>
    </tbody>
  </v-table>
</template>
