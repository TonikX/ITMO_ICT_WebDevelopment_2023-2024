<script setup>
import {ref, watch} from 'vue'
import axios from "axios";
import moment from "moment/moment";
import router from "@/router";

const props = defineProps({
  consignments: Array,
})

const formatter = new Intl.DateTimeFormat('us')
const today = formatter.format(new Date()).split('/').reverse().join('-')

const terms = [
        { text: 'afterpay', value: 'ap' },
        { text: 'prepay', value: 'pp' },
      ]
const status = [
        { text: 'active', value: 'a' },
        { text: 'cancelled', value: 'c' },
        { text: 'signed', value: 's' },
      ]

const selectedConsignment = ref(null)
const selectedTerms = ref(null)
const selectedStatus = ref(null)
const date = ref(null)

function updateFields () {
  if (selectedConsignment.value) {
    let object = props.consignments.filter(function(item) {
      return item.id == selectedConsignment.value
    })[0]
    selectedTerms.value = object.terms
    selectedStatus.value = object.status
    date.value = new Date(object.delivery_date)
  }
}

 async function editConsignment() {
     try {
       const response = await axios.patch(`http://127.0.0.1:8000/exchange/consignment/${selectedConsignment.value}/edit`,
       { terms: selectedTerms.value,
              status: selectedStatus.value,
              delivery_date: moment(date.value).format('YYYY-MM-DD HH:mm:ss') },
       { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       selectedTerms.value = null
       selectedStatus.value = null
       selectedConsignment.value = null
     } catch (e) {
       alert('Invalid data')
       await router.push({path: '/'})
     }
 }

watch(selectedConsignment, updateFields)

defineExpose({
    editConsignment
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
  <v-select
    label="terms"
    :items="terms"
    item-title="text"
    item-value="value"
    v-model="selectedTerms"
  ></v-select>
  <v-select
    label="status"
    :items="status"
    item-title="text"
    item-value="value"
    v-model="selectedStatus"
  ></v-select>
  <p>delivery date</p>
  <v-date-picker width="100%" color="lime" v-model="date" :min="today"></v-date-picker>
  <br>
</template>