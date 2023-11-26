<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'

import ProductTable from './tables/ProductTable.vue'
import ConsignmentOverviewTable from "@/components/tables/ConsignmentOverviewTable.vue"
import ConsignmentForm from "@/components/forms/ConsignmentForm.vue"
import ProductInConsignmentForm from "@/components/forms/ProductInConsignmentForm.vue"
import ConsignmentEditForm from "@/components/forms/ConsignmentEditForm.vue"
import ProductInConsignmentTable from "@/components/tables/ProductInConsignmentTable.vue"
import router from "@/router";

const consignment_form = ref(null)
const consignment_edit_form = ref(null)
const product_table = ref(null)
const product_consignment_table = ref(null)

const c_added = ref(false)
const c_edited = ref(false)

const consignments = ref([])
const fetching = ref(true)
 async function fetchConsignments() {
     try {
       fetching.value = true
       const response = await axios.get('http://127.0.0.1:8000/exchange/consignment',
           { params: {broker: sessionStorage.getItem('broker_id')},
           headers: {Authorization: 'Token ' + sessionStorage.getItem('token')} })
       consignments.value = response.data
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
   } finally {
       fetching.value = false
     }
 }

 async function submitConsignment() {
  await consignment_form.value.createConsignment()
  c_added.value = true
  await fetchConsignments()
  setTimeout(() => { c_added.value = false }, 3000)
}

 async function editConsignment() {
  await consignment_edit_form.value.editConsignment()
  c_edited.value = true
  await fetchConsignments()
  setTimeout(() => { c_edited.value = false }, 3000)
}

onMounted(fetchConsignments)
</script>

<template>
  <v-container justify="center" style="margin-top: 10%; margin-left: 0%; margin-right: 10%">
     <v-row align="stretch">
      <v-col cols=5>
      <v-card width="100%" color="lime">
        <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
          <b>Create consignment</b>
        </v-card-title>
        <consignment-form ref="consignment_form"></consignment-form>
        <v-btn @click="submitConsignment" variant="outlined" style="margin-bottom: 20px; margin-left: 20px" v-if="!c_added">
          Submit
        </v-btn>
        <p v-if="c_added" style="color:white"><b>Consignment successfully added</b></p>
        <br>
      </v-card>
         <br>
      <v-card width="100%" color="lime">
        <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
          <b>Add product to consignment</b>
        </v-card-title>
        <product-in-consignment-form :consignments="consignments" :pc_table="product_consignment_table" :p_table="product_table">
        </product-in-consignment-form>
      </v-card>
          <br>
        <v-card width="100%" color="lime">
        <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
          <b>Edit consignment</b>
        </v-card-title>
          <consignment-edit-form :consignments="consignments" ref="consignment_edit_form"></consignment-edit-form>
        <v-btn @click="editConsignment" variant="outlined" style="margin-bottom: 20px; margin-left: 20px" v-if="!c_edited">
          Submit
        </v-btn>
        <p v-if="c_edited" style="color:white"><b>Consignment successfully updated</b></p>
        <br>
      </v-card>
      </v-col>

       <v-col cols=1>
        <v-card width="1100%" color="lime">
          <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
            <b>Available products</b>
          </v-card-title>
          <product-table ref="product_table"></product-table>
        </v-card>
         <br>
        <v-card width="1100%" color="lime">
          <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
            <b>Featured consignments</b>
          </v-card-title>
          <v-btn variant="outlined" @click="fetchConsignments" style="margin-bottom: 20px; margin-left: 20px">
            Update
          </v-btn>
          <consignment-overview-table :consignments="consignments" :fetching="fetching">
          </consignment-overview-table>
        </v-card>
         <br>
         <v-card width="1100%" color="lime">
          <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
            <b>Products in consignment</b>
          </v-card-title>
          <product-in-consignment-table :consignments="consignments" ref="product_consignment_table">
          </product-in-consignment-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
