<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'
import router from "@/router";

const selectedBroker = ref(null)

const brokers = ref([])
let fetching = ref(true)

 async function fetchBrokers() {
     try {
       fetching.value = true
       const response = await axios.get('http://127.0.0.1:8000/exchange/broker',
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       brokers.value = response.data
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     } finally {
       fetching.value = false
     }
   }

  async function deleteBroker() {
     try {
       const response = await axios.delete(`http://127.0.0.1:8000/exchange/broker/${selectedBroker.value}/delete`,
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       selectedBroker.value = null
       await fetchBrokers()
       await router.push({path: '/'})
     } catch (e) {
       selectedBroker.value = null
       alert('Cannot delete this broker')
       await router.push({path: '/'})
     }
   }

onMounted(fetchBrokers)
</script>

<template>
  <v-btn variant="outlined" @click="fetchBrokers" style="margin-bottom: 20px; margin-left: 20px">
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
          First Name
        </th>
        <th class="text-left">
          Last Name
        </th>
        <th class="text-left">
          Telephone
        </th>
        <th class="text-left">
          Company
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in brokers"
        :key="item.id"
      >
        <td>{{ item.id }}</td>
        <td>{{ item.first_name }}</td>
        <td>{{ item.last_name }}</td>
        <td>{{ item.telephone }}</td>
        <td>{{ item.company }}</td>
      </tr>
    </tbody>
  </v-table>
  <v-divider style="margin-top: 5%; margin-bottom: 3%"></v-divider>
  <v-select
    label="broker id"
    :items="brokers"
    item-title="id"
    item-value="id"
    v-model="selectedBroker"
  ></v-select>
  <v-btn @click="deleteBroker" variant="outlined" style="margin-bottom: 20px; margin-left: 20px">
          Delete
  </v-btn>
</template>
