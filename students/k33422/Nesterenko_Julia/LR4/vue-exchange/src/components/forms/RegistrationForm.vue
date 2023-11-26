<script setup>
import { ref } from 'vue'
import RegisterBroker from './RegisterBroker.vue'
import RegisterManufacturer from './RegisterManufacturer.vue'
import axios from "axios";
import router from "@/router";

const selected = ref('e')
const items = [
        { text: 'Exchange Admin', value: 'e' },
        { text: 'Broker', value: 'b' },
        { text: 'Manufacturer Representative', value: 'm' }
      ]

const represents_form = ref(null)

const first_name = ref('')
const last_name = ref('')
const email = ref('')
const username = ref('')
const password = ref('')


async function registerUser() {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/users/',
        { first_name: first_name.value,
          last_name: last_name.value,
          email: email.value,
          role: selected.value,
          username: username.value,
          password: password.value})
    await loginUser()
    sessionStorage.setItem('role', selected.value)
    if (Boolean(represents_form.value)) {
      await represents_form.value.registerRole()
    }
    await router.push({path: '/'})
  } catch (e) {
    alert('Check that all fields are filled in and the password is valid.')
    await deleteUser()
  }
 }

async function loginUser() {
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/token/login/',
        {username: username.value, password: password.value})
    sessionStorage.setItem('token', response.data.auth_token)
    sessionStorage.setItem('username', username.value)
    sessionStorage.setItem('password', password.value)
  } catch (e) {
     alert('Incorrect username and/or password')
  }
 }

 async function deleteUser() {
     try {
       const response1 = await axios.delete("http://127.0.0.1:8000/auth/users/me/",
            { data: {current_password: password.value},
              headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}
            })
       sessionStorage.clear()
     } catch (e) {
       await router.push({path: 'register'})
     }
   }
</script>


<template>
 <p>first name</p>
  <v-text-field v-model="first_name"></v-text-field>
  <p>last name</p>
  <v-text-field v-model="last_name"></v-text-field>
  <p>email</p>
  <v-text-field v-model="email"></v-text-field>
  <p>username</p>
  <v-text-field v-model="username"></v-text-field>
  <p>password</p>
  <v-text-field type="password" v-model="password"></v-text-field>
  <v-select
    label="role"
    :items="items"
    item-title="text"
    item-value="value"
    v-model="selected"
  ></v-select>
  <div v-if="selected === 'b'">
     <v-divider style="margin-top: 5%; margin-bottom: 5%"></v-divider>
    <register-broker ref="represents_form" :first_name="first_name" :last_name="last_name"></register-broker>
  </div>
  <div v-else-if="selected === 'm'">
     <v-divider style="margin-top: 5%; margin-bottom: 5%"></v-divider>
    <register-manufacturer ref="represents_form"></register-manufacturer>
  </div>
  <v-btn @click="registerUser" variant="outlined"
           style="margin-bottom: 20px; margin-left: 20px">
        Sign Up
  </v-btn>
</template>