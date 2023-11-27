<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'
import router from "@/router";

const status = {'a': 'active', 'c':'cancelled', 's':'signed'}
const terms = {'ap': 'afterpay', 'pp': 'prepay'}

const consignments = ref([])
let fetching = ref(true)

 async function fetchConsignments() {
     try {
       fetching.value = true
       const response = await axios.get(`http://127.0.0.1:8000/exchange/productinconsignment`,
       { params: {manufacturer: sessionStorage.getItem('manufacturer_id')},
         headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       consignments.value = response.data
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     } finally {
       fetching.value = false
     }
   }

onMounted(fetchConsignments)
</script>

<template>
  <v-btn variant="outlined" @click="fetchConsignments" style="margin-bottom: 20px; margin-left: 20px">
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
          Consignment Id
        </th>
        <th class="text-left">
          Broker Company
        </th>
        <th class="text-left">
          Broker Name
        </th>
        <th class="text-left">
          Broker Phone
        </th>
        <th class="text-left">
          Consignment Terms
        </th>
        <th class="text-left">
          Consignment Status
        </th>
        <th class="text-left">
          Opening Date
        </th>
        <th class="text-left">
          Delivery Date
        </th>
        <th class="text-left">
          Product Id
        </th>
        <th class="text-left">
          Product Amount
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in consignments"
        :key="item.id"
      >
        <td>{{ item.consignment.id }}</td>
        <td>{{ item.consignment.broker.company }}</td>
        <td>{{ item.consignment.broker.first_name }} {{ item.consignment.broker.last_name }}</td>
        <td>{{ item.consignment.broker.telephone }}</td>
        <td>{{ terms[item.consignment.terms] }}</td>
        <td>{{ status[item.consignment.status] }}</td>
        <td>{{ item.consignment.opening_date }}</td>
        <td>{{ item.consignment.delivery_date }}</td>
        <td>{{ item.product.id }}</td>
        <td>{{ item.amount }}</td>
      </tr>
    </tbody>
  </v-table>
</template>
