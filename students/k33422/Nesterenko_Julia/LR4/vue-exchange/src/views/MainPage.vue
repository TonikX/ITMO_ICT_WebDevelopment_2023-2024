<script setup>
import {onMounted, ref} from 'vue'
import router from "@/router";
import Header from '../components/Header.vue'
import MainManufacturer from '../components/MainManufacturer.vue'
import MainBroker from "@/components/MainBroker.vue"
import MainAdmin from "@/components/MainAdmin.vue"
import axios from "axios";

const role = ref(sessionStorage.getItem('role'))

async function checkAuth() {
     try {
      const response = await axios.get('http://127.0.0.1:8000/auth/users/me/',
           {headers: {Authorization: `Token ${ sessionStorage.getItem('token') }`}})
     } catch (e) {
        sessionStorage.clear()
        await router.push({path: 'login'})
     }
 }

onMounted(checkAuth)
</script>

<template>
  <Header place="main"></Header>
    <body>
      <div v-if="role === 'm'">
        <main-manufacturer/>
      </div>
      <div v-if="role === 'b'">
        <main-broker/>
      </div>
      <div v-if="role === 'e'">
        <main-admin/>
      </div>
    </body>
</template>

<style>
p {margin-left: 20px}
</style>