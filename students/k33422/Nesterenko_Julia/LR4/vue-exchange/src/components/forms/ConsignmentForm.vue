<script setup>
import { ref } from 'vue'
import axios from "axios";
import moment from "moment/moment";
import router from "@/router";

const formatter = new Intl.DateTimeFormat('us')
const today = formatter.format(new Date()).split('/').reverse().join('-')

const date = ref(null)
const selectedTerms = ref('')
const items = [
        { text: 'afterpay', value: 'ap' },
        { text: 'prepay', value: 'pp' },
      ]

async function createConsignment() {
     try {
       const response = await axios.post(`http://127.0.0.1:8000/exchange/consignment/create/`,
           { terms: selectedTerms.value,
                  status: 'a',
                  broker: sessionStorage.getItem('broker_id'),
                  delivery_date: moment(date.value).format('YYYY-MM-DD HH:mm:ss') },
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
       selectedTerms.value = null
       date.value = null
     } catch (e) {
       alert('Invalid data')
       await router.push({path: '/'})
     }
   }

defineExpose({
    createConsignment
})
</script>


<template>
  <v-select
    label="terms"
    :items="items"
    item-title="text"
    item-value="value"
    v-model="selectedTerms"
  ></v-select>
  <p>delivery date</p>
  <v-date-picker width="100%" color="lime" v-model="date" :min="today"></v-date-picker>
  <br>
</template>