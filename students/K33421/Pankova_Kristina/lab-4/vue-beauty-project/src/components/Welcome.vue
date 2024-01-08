<template>
    <UserComponent />
  <div >
    <div v-if="!showComponent">
      <v-btn @click="showSignIn">Sign in</v-btn>
      <v-btn @click="showSignUp">Sign up</v-btn>
      <v-btn @click="showSalons">Show Salons</v-btn>
      <v-btn @click="showService">Register for a service</v-btn>
      <v-btn @click="showAppointment">Show appointments</v-btn>


    </div>

    <div v-if="showComponent === 'signIn'">
      <SignIn />
    </div>

    <div v-if="showComponent === 'signUp'">
      <SignUpChoice />
    </div>

    <div v-if="showComponent === 'salons'">
      <Salons />
    </div>

     <div v-if="showComponent === 'service'">
      <SalonServiceForm />
    </div>

     <div v-if="showComponent === 'appointment'">
       <appointment-edit-form
         v-if="editingAppointment"
         :appointment="editingAppointment"
         @cancel-edit="cancelEdit"
       />
       <appointment-list
         v-else
         :appointments="appointments"
         @edit-appointment="startEdit"
       />
    </div>


    <v-btn v-if="showComponent" @click="goBack">Go back</v-btn>
  </div>
</template>

<style>
button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  margin: 5px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

.select-selected {
  background-color: DodgerBlue;
}


select {
  border: 1px;
  background-color: DodgerBlue;
  border-color: black;
}

</style>

<script>
import axios from 'axios';
import SignIn from './SignIn.vue';
import SignUpChoice from './SignUpChoice.vue';
import UserComponent from './UserComponent.vue';
import Salons from '@/views/Salons.vue';
import SalonServiceForm from './SalonServiceForm.vue';
import AppointmentList from './AppointmentList.vue';
import AppointmentEditForm from "@/components/AppointmentEditForm.vue";


export default {
  components: {
    SignIn,
    SignUpChoice,
    UserComponent,
    Salons,
    SalonServiceForm,
    AppointmentList,
    AppointmentEditForm
  },
  data() {
    return {
      showComponent: null,
      editingAppointment: null,
      appointments: []
    };
  },
  created() {
    this.fetchAppointments();
  },
  methods: {
    showSignIn() {
      this.showComponent = 'signIn';
    },
    showSignUp() {
      this.showComponent = 'signUp';
    },
    showSalons() {
      this.showComponent = 'salons';
    },
    showAppointment() {
      this.showComponent = 'appointment';
    },
    showService() {
      this.showComponent = 'service';
    },
    goBack() {
      this.showComponent = null;
    },
    fetchAppointments() {
      axios
        .get("http://127.0.0.1:8000/salon/appointments/")
        .then((response) => {
          this.appointments = response.data;
        })
        .catch((error) => {
          console.error(error);
          alert("Error fetching appointments");
        });
    },
    startEdit(appointment) {
      this.editingAppointment = appointment;
    },
    cancelEdit() {
      this.editingAppointment = null;
    },
  },

};
</script>
