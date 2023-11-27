<script setup>
import axios from "axios";
import {onMounted, ref, watch} from 'vue'
import router from "@/router";

const props = defineProps({
  consignments: Array,
  pc_table: Object,
  p_table: Object
})

const pc_added = ref(false)
const pc_edited = ref(false)

const selectedConsignment = ref(null)
const selectedProduct = ref(null)
const amount = ref(null)

const products = ref([])
const productsinconsignments = ref([])

function updateAmount() {
if (selectedConsignment.value && selectedProduct.value) {
    let selectedPinC = productsinconsignments.value.filter(function(item) {
    return item.product.id === selectedProduct.value &&
        item.consignment.id === selectedConsignment.value
  })
    amount.value = (selectedPinC.length != 0) ? selectedPinC[0].amount : null
}
}

watch(selectedConsignment, updateAmount)
watch(selectedProduct, updateAmount)

async function fetchProducts() {
     try {
       const response = await axios.get('http://127.0.0.1:8000/exchange/product',
       { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       products.value = response.data
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     }
   }

 async function fetchProductInConsignments() {
     try {
       const response = await axios.get('http://127.0.0.1:8000/exchange/productinconsignment',
       { params: {broker: sessionStorage.getItem('broker_id')},
         headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       productsinconsignments.value = response.data
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     }
 }

 async function submitProductInConsignment() {
     try {
       const selectedPinC = productsinconsignments.value.filter(function (item) {
           return item.product.id === selectedProduct.value &&
               item.consignment.id === selectedConsignment.value
         })
        if (selectedPinC.length != 0) {
          const response = await axios.patch(`http://127.0.0.1:8000/exchange/productinconsignment/${selectedPinC[0].id}/edit`,
       { amount: amount.value },
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
          pc_edited.value = true
          setTimeout(() => { pc_edited.value = false }, 3000)
        } else {
          const response = await axios.post(`http://127.0.0.1:8000/exchange/productinconsignment/create/`,
       { product: selectedProduct.value,
              consignment: selectedConsignment.value,
              amount: amount.value },
              { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
          pc_added.value = true
          setTimeout(() => { pc_added.value = false }, 3000)
        }
       selectedProduct.value = null
       selectedConsignment.value = null
       amount.value = null
       await props.pc_table.fetchProductsInConsignment()
       await props.p_table.fetchProducts()
     } catch (e) {
       alert('Invalid data' + e)
     }
 }


onMounted(fetchProducts)
onMounted(fetchProductInConsignments)
</script>


<template>
  <v-select
    label="consignment id"
    :items="consignments"
    item-title="id"
    item-value="id"
    v-model="selectedConsignment"
  ></v-select>
  <v-select
    label="product id"
    :items="products"
    item-title="id"
    item-value="id"
    v-model="selectedProduct"
  ></v-select>
  <p>amount</p>
  <v-text-field v-model="amount"></v-text-field>
  <br>
   <v-btn @click="submitProductInConsignment" variant="outlined" style="margin-bottom: 20px; margin-left: 20px" v-if="!pc_added & !pc_edited">
          Submit
   </v-btn>
  <p v-if="pc_added" style="color:white"><b>Product successfully added to consignment</b></p>
  <p v-if="pc_edited" style="color:white"><b>Product amount in consignment successfully updated</b></p>
        <br>
</template>