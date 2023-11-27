<script setup>
import axios from "axios";
import {onMounted, ref} from 'vue'

import Header from "@/components/Header.vue";
import router from "@/router";
import moment from "moment/moment";

const formatter = new Intl.DateTimeFormat('us')
const today = formatter.format(new Date()).split('/').reverse().join('-')

const first_name = ref('')
const last_name = ref('')
const email = ref('')
const username = ref('')
const password = ref('')
const telephone = ref('')
const company = ref('')
const name = ref('')
const address = ref('')
const ceo = ref('')
const date = ref(null)

const role = ref('')
const editing = ref(false)
const loggingout = ref(false)
const deleting = ref(false)

function switchMode () {
  editing.value = !editing.value
}

function switchLogout () {
  loggingout.value = !loggingout.value
}
function switchDelete () {
  deleting.value = !deleting.value
}

async function fillFields() {
     try {
       const response = await axios.get("http://127.0.0.1:8000/auth/users/me/",
         { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')} })
       const data = response.data
       first_name.value = data.first_name
       last_name.value = data.last_name
       email.value = data.email
       username.value = data.username

       role.value = sessionStorage.getItem('role')
       if (role.value === 'm') {
         const response = await axios.get(
             `http://127.0.0.1:8000/exchange/manufacturer/${sessionStorage.getItem('manufacturer_id')}`,
             { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
         )
         const data = response.data
         name.value = data.name
         address.value = data.address
         ceo.value = data.ceo
         date.value = new Date(data.establishment_date)
       }

       if (role.value === 'b') {
         const response = await axios.get(
             `http://127.0.0.1:8000/exchange/broker/${ sessionStorage.getItem('broker_id') }`,
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
         const data = response.data
         telephone.value = data.telephone
         company.value = data.company
       }

     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     }
   }

   async function logOut() {
     try {
       const response = await axios.post("http://127.0.0.1:8000/auth/token/logout/",
           {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       sessionStorage.clear()
       await router.push({path: 'login'})
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     }
   }

 async function deleteAccount() {
     try {
       if (role.value === 'b') {
         const response2 = await axios.delete(`http://127.0.0.1:8000/exchange/broker/${sessionStorage.getItem('broker_id')}/delete`,
             {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       }
       const response1 = await axios.delete("http://127.0.0.1:8000/auth/users/me/",
            { data: {current_password: sessionStorage.getItem('password')},
              headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}
            })
       sessionStorage.clear()
     } catch (e) {
       sessionStorage.clear()
       await router.push({path: 'login'})
     }
   }

  async function updateAccount() {
     try {
       const response = await axios.patch("http://127.0.0.1:8000/auth/users/me/",
           { first_name: first_name.value,
                  last_name: last_name.value,
                  email: email.value },
         { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})

       if (sessionStorage.getItem('role') === 'm') {
         await updateManufacturer()
       }
       if (sessionStorage.getItem('role') === 'b') {
         await updateBroker()
       }
       if (sessionStorage.getItem('username') !== username.value) {
         await updateUsername()
       }
       if (Boolean(password.value)) {
         await updatePassword()
       }
       await fillFields()
       switchMode()
     } catch (e) {
       alert('Invalid data')
     }
   }

   async function updateManufacturer() {
     try {
       const response = await axios.patch(`http://127.0.0.1:8000/exchange/manufacturer/${sessionStorage.getItem('manufacturer_id')}/edit`,
           { name: name.value,
                  address: address.value,
                  ceo: ceo.value,
                  establishment_date: moment(date.value).format('YYYY-MM-DD')},
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
     } catch (e) {
       alert('Invalid data')
     }
   }

   async function updateBroker() {
     try {
       const response = await axios.patch(`http://127.0.0.1:8000/exchange/broker/${sessionStorage.getItem('broker_id')}/edit`,
           { first_name: first_name.value,
                  last_name: last_name.value,
                  telephone: telephone.value,
                  company: company.value },
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
     } catch (e) {
       alert('Invalid data')
     }
   }

   async function updateUsername() {
     try {
       const response = await axios.post(`http://127.0.0.1:8000/auth/users/set_username/`,
           { new_username: username.value,
                  current_password: sessionStorage.getItem('password') },
           { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
       )
       sessionStorage.setItem('username', username.value)
     } catch (e) {
       alert('Invalid username')
     }
   }

   async function updatePassword() {
     try {
       const response = await axios.post(`http://127.0.0.1:8000/auth/users/set_password/`,
           { new_password: password.value,
                  current_password: sessionStorage.getItem('password')},
       { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}})
       sessionStorage.setItem('password', password.value)
       password.value = ''
     } catch (e) {
       alert('Invalid password')
     }
   }

onMounted(fillFields)
</script>

<template>
  <Header place="account"></Header>
  <body>
  <v-container style="alignment: center; margin-top: 10%">
    <div class="d-flex align-left flex-column">
    <v-card variant="text" width="100%" height="80">
      <v-card-title style="text-align: left; font-size: 30px; color: #ffffff">
        Account settings
      </v-card-title>
    </v-card>

    <v-card width="100%" color="lime">
      <p style="font-size: 20px; margin-top: 3%; margin-bottom: 3%; margin-left: 20px;">
        <b>General Info</b>
      </p>
      <p>first name</p>
      <v-text-field :readonly="!editing" v-model="first_name"></v-text-field>
      <p>last name</p>
      <v-text-field :readonly="!editing" v-model="last_name"></v-text-field>
      <p>email</p>
      <v-text-field :readonly="!editing" v-model="email"></v-text-field>
      <p>username</p>
     <v-text-field :readonly="!editing" v-model="username"></v-text-field>
      <p>password</p>
      <v-text-field :readonly="!editing" type="password" v-model="password"></v-text-field>
      <div v-if="role === 'b'">
        <v-divider style="margin-top: 5%; margin-bottom: 5%"></v-divider>
        <p style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 20px;">
        <b>Broker</b>
        </p>
        <p>telephone</p>
        <v-text-field :readonly="!editing" v-model="telephone"></v-text-field>
        <p>company</p>
        <v-text-field :readonly="!editing" v-model="company"></v-text-field>
      </div>
      <div v-if="role === 'm'">
        <v-divider style="margin-top: 5%; margin-bottom: 5%"></v-divider>
        <p style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 20px;">
        <b>Manufacturer</b>
        </p>
        <p>name</p>
        <v-text-field :readonly="!editing" v-model="name"></v-text-field>
        <p>address</p>
        <v-text-field :readonly="!editing" v-model="address"></v-text-field>
        <p>ceo</p>
        <v-text-field :readonly="!editing" v-model="ceo"></v-text-field>
        <p>establishment date</p>
        <v-date-picker width="100%" color="lime" v-model="date"
                       :max="today" :disabled="!editing"></v-date-picker>
        <br>
      </div>
      <v-btn @click="switchMode" variant="outlined"
             style="margin-bottom: 20px; margin-left: 20px" v-if="!editing">
        Edit
      </v-btn>
      <v-btn @click="updateAccount" variant="outlined"
             style="margin-bottom: 20px; margin-left: 20px" v-if="editing">
        Submit
      </v-btn>
    </v-card>
    <v-card variant="text" width="400" style="margin-top: 60px">
      <v-btn @click="switchLogout" variant="tonal" style="margin-top: 10px; margin-right: 10px" v-if="!deleting && !loggingout">
        Log Out
      </v-btn>
      <v-btn @click="switchDelete" variant="tonal" style="margin-top: 10px" v-if="!deleting && !loggingout" color="red">
        Delete account
      </v-btn>
      <v-banner text="Are you sure you want to leave?"
                :stacked="false" v-if="loggingout">
        <template v-slot:actions>
          <v-btn @click="switchLogout">Cancel</v-btn>
          <v-btn @click="logOut">Confirm</v-btn>
        </template>
      </v-banner>
       <v-banner text="Are you sure you want to delete your account?"
                :stacked="false" v-if="deleting">
        <template v-slot:actions>
          <v-btn @click="switchDelete">Cancel</v-btn>
          <v-btn @click="deleteAccount">Confirm</v-btn>
        </template>
      </v-banner>
    </v-card>
    </div>
  </v-container>
  </body>
</template>

<style>
p {margin-left: 20px}
</style>