<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'

import ConsignmentOverviewTable from "@/components/tables/ConsignmentOverviewTable.vue"
import BrokerTable from "@/components/tables/BrokerTable.vue"
import ManufacturerTable from "@/components/tables/ManufacturerTable.vue";
import router from "@/router";

const consignments = ref([])
let fetching = ref(true)
 async function fetchConsignments() {
     try {
       fetching.value = true
       const response = await axios.get('http://127.0.0.1:8000/exchange/consignment',
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
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
  <v-container justify="center" style="margin-top: 10%; margin-left: 0%; margin-right: 10%">
     <v-row align="stretch">
      <v-col cols=10>
        <v-card width="130%" color="lime">
          <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
            <b>Manufacturers</b>
          </v-card-title>
          <manufacturer-table/>
        </v-card>
           <br>
        <v-card width="130%" color="lime">
          <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
            <b>Brokers</b>
          </v-card-title>
          <broker-table/>
        </v-card>
        <br>
        <v-card width="130%" color="lime">
            <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
              <b>Consignments</b>
            </v-card-title>
            <v-btn variant="outlined" @click="fetchConsignments" style="margin-bottom: 20px; margin-left: 20px">
              Update
            </v-btn>
            <consignment-overview-table :consignments="consignments" :fetching="fetching">
            </consignment-overview-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
