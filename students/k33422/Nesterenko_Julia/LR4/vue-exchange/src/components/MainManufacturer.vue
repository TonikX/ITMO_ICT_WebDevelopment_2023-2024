<script setup>
import ProductForm from './forms/ProductForm.vue'
import ProductTypeForm from './forms/ProductTypeForm.vue'
import ProductTable from './tables/ProductTable.vue'
import ConsignmentTable from './tables/ConsignmentTable.vue'
import {ref} from "vue";

const product_type_form = ref(null)
const product_form = ref(null)
const product_table = ref(null)

const pt_added = ref(false)
const p_added = ref(false)

async function submitProductType() {
  await product_type_form.value.createProductType()
  pt_added.value = true
  await product_form.value.fetchTypes()
  setTimeout(() => { pt_added.value = false }, 3000)
}

async function submitProduct() {
  await product_form.value.createProduct()
  p_added.value = true
  await product_table.value.fetchProducts()
  setTimeout(() => { p_added.value = false }, 3000)
}
</script>

<template>
  <v-container justify="center" style="margin-top: 10%; margin-left: 0%; margin-right: 10%">
     <v-row align="stretch">
      <v-col cols=5>
      <v-card width="100%" color="lime">
        <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
          <b>Add product type</b>
        </v-card-title>
        <product-type-form ref="product_type_form"></product-type-form>
        <v-btn @click="submitProductType" variant="outlined" style="margin-bottom: 20px; margin-left: 20px" v-if="!pt_added">
          Submit
        </v-btn>
        <p v-if="pt_added" style="color:white"><b>Product type successfully added</b></p>
        <br>
      </v-card>
         <br>
      <v-card width="100%" color="lime">
        <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
          <b>Add product</b>
        </v-card-title>
        <product-form ref="product_form"></product-form>
        <v-btn @click="submitProduct" variant="outlined" style="margin-bottom: 20px; margin-left: 20px" v-if="!p_added">
          Submit
        </v-btn>
        <p v-if="p_added" style="color:white"><b>Product successfully added</b></p>
        <br>
      </v-card>
          <br>
      <v-card width="265%" color="lime">
        <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
          <b>Featured consignments</b>
        </v-card-title>
        <consignment-table/>
      </v-card>
      </v-col>

       <v-col cols=1>
      <v-card width="1100%" color="lime">
        <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
          <b>Manufactured products</b>
        </v-card-title>
        <product-table ref="product_table"></product-table>
      </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
