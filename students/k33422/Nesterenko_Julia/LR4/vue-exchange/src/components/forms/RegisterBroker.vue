<script setup>
import { ref } from 'vue'
import axios from "axios";

const props = defineProps({
  first_name: String,
  last_name: String,
})

const telephone = ref('')
const company = ref('')

async function registerRole() {
     try {
       const response1 = await axios.post(`http://127.0.0.1:8000/exchange/broker/create/`,
           { first_name: props.first_name,
                  last_name: props.last_name,
                  telephone: telephone.value,
                  company: company.value },
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
       sessionStorage.setItem('broker_id', response1.data.id)
       const response2 = await axios.patch("http://127.0.0.1:8000/auth/users/me/",
           { broker: sessionStorage.getItem('broker_id') },
         { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
     } catch (e) {
       alert('Invalid data')
     }
   }

defineExpose({
    registerRole
})
</script>

<template>
  <p>telephone</p>
  <v-text-field v-model="telephone"></v-text-field>
  <p>company</p>
  <v-text-field v-model="company"></v-text-field>
</template>
