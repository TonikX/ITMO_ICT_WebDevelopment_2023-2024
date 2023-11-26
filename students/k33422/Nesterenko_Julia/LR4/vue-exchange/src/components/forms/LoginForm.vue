<script setup>
import axios from "axios";
import {ref} from 'vue'
import router from "@/router";

const username = ref('')
const password = ref('')

 async function loginUser() {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
        {username: username.value, password: password.value})
    sessionStorage.setItem('token', response.data.auth_token)
    sessionStorage.setItem('username', username.value)
    sessionStorage.setItem('password', password.value)
    await getUserInfo()
    await router.push({path: '/'})
  } catch (e) {
     alert('Incorrect username and/or password')
  }
 }

 async function getUserInfo() {
   const response = await axios.get("http://127.0.0.1:8000/auth/users/me/",
         { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')} })
   const data = response.data
   sessionStorage.setItem('role', data.role)
   if (Boolean(data.manufacturer)) {
     sessionStorage.setItem('manufacturer_id', data.manufacturer)
   }
   if (Boolean(data.broker)) {
     sessionStorage.setItem('broker_id', data.broker)
   }
 }
</script>


<template>
  <p>username</p>
  <v-text-field v-model="username"></v-text-field>
  <p>password</p>
 <v-text-field type="password" v-model="password"></v-text-field>
  <v-btn @click="loginUser" variant="outlined"
           style="margin-bottom: 20px; margin-left: 20px">
        Log In
  </v-btn>
</template>