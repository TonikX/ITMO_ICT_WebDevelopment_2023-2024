<script setup>
import axios from "axios";
import {onMounted, ref, watch} from 'vue'
import router from "@/router";

const props = defineProps({
  consignments: Array,
})

const fetching = ref(false)

const selectedConsignment = ref(null)
const products = ref([])

watch(selectedConsignment, fetchProductsInConsignment)

 async function fetchProductsInConsignment() {
     try {
       fetching.value = true
       const response = await axios.get('http://127.0.0.1:8000/exchange/productinconsignment',
       { params: {consignment: selectedConsignment.value},
         headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       products.value = response.data
       fetching.value = false
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     }
 }

 defineExpose({
    fetchProductsInConsignment
})
</script>


<template>
  <v-select
    label="consignment id"
    :items="consignments"
    item-title="id"
    item-value="id"
    v-model="selectedConsignment"
  ></v-select>
  <div class="text-center" v-if="fetching">
    <v-progress-circular
      indeterminate
      color="white"
      style="margin-bottom: 10%"
    ></v-progress-circular>
  </div>
  <v-table density="compact" v-if="!fetching && selectedConsignment && products.length">
    <thead>
      <tr>
        <th class="text-left">
          Product Id
        </th>
        <th class="text-left">
          Product Name
        </th>
        <th class="text-left">
          Product Manufacturer
        </th>
        <th class="text-left">
          Product Size
        </th>
        <th class="text-left">
          Product Amount
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in products"
        :key="item.id"
      >
        <td>{{ item.product.id }}</td>
        <td>{{ item.product.type.name }}</td>
        <td>{{ item.product.manufacturer.name }}</td>
        <td>{{ item.product.size + ' ' + item.product.type.units }}</td>
        <td>{{ item.amount }}</td>
      </tr>
    </tbody>
  </v-table>
  <p v-if="!fetching && selectedConsignment && !products.length" style="color:white"><b>There are no products in this consignment</b></p>
  <br>
</template>