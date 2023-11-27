<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'
import router from "@/router";

const selectedManufacturer = ref(null)

const manufacturers = ref([])
let fetching = ref(true)

 async function fetchManufacturers() {
     try {
       fetching.value = true
       const response = await axios.get('http://127.0.0.1:8000/exchange/manufacturer',
       { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       console.log(response.data)
       manufacturers.value = response.data
     } catch (e) {
       alert('Error: ' + e.toString())
     } finally {
       fetching.value = false
     }
   }

 async function deleteManufacturer() {
     try {
       const response = await axios.delete(`http://127.0.0.1:8000/exchange/manufacturer/${selectedManufacturer.value}/delete`,
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       selectedManufacturer.value = null
       await fetchManufacturers()
       await router.push({path: '/'})
     } catch (e) {
       selectedManufacturer.value = null
       alert('Cannot delete this manufacturer')
       await router.push({path: '/'})
     }
   }

onMounted(fetchManufacturers)
</script>

<template>
  <v-btn variant="outlined" @click="fetchManufacturers" style="margin-bottom: 20px; margin-left: 20px">
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
          Name
        </th>
        <th class="text-left">
          Address
        </th>
        <th class="text-left">
          CEO
        </th>
        <th class="text-left">
          Establishment date
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in manufacturers"
        :key="item.id"
      >
        <td>{{ item.id }}</td>
        <td>{{ item.name }}</td>
        <td>{{ item.address }}</td>
        <td>{{ item.ceo }}</td>
        <td>{{ item.establishment_date }}</td>
      </tr>
    </tbody>
  </v-table>
  <v-divider style="margin-top: 5%; margin-bottom: 3%"></v-divider>
  <v-select
    label="manufacturer id"
    :items="manufacturers"
    item-title="id"
    item-value="id"
    v-model="selectedManufacturer"
  ></v-select>
  <v-btn @click="deleteManufacturer" variant="outlined" style="margin-bottom: 20px; margin-left: 20px">
          Delete
  </v-btn>
</template>
