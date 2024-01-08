<template>
  <div class="salon-appointment">
    <div v-for="appointment in appointments" :key="appointment.id">
      <div><strong>Customer:</strong> {{ appointment.customer }} </div>
      <div><strong>Service:</strong> {{ appointment.service }}</div>
      <div><strong>Datetime:</strong> {{ appointment.datetime }}</div>
      <v-btn v-on:click="editAppointment(appointment)">Edit</v-btn>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    salonId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      appointments: []
    };
  },
  methods: {
    async fetchSalonAppointments() {
      const url = 'http://127.0.0.1:8000/salon/appointments/';
      try {
        const response = await axios.get(url);
        const appointments = response.data;

        for (const appointment of appointments) {
          const customerResponse = await axios.get(`http://127.0.0.1:8000/salon/customers/${appointment.customer}`);
          appointment.customer = customerResponse.data.username;
          const serviceResponse = await axios.get(`http://127.0.0.1:8000/salon/services/${appointment.service}`);
          appointment.service = serviceResponse.data.name;
        }
        this.appointments = appointments;
      } catch (error) {
        console.error(error);
        alert("Error fetching salon appointments");
      }
    },
    editAppointment(appointment) {
      this.$emit("edit-appointment", appointment);
    },
  },
  mounted() {
    this.fetchSalonAppointments();
  }
};
</script>

<style>
.salon-appointment {
  padding: 20px;
  margin: 10px;
  margin-top: 20px;
  border: 1px solid gray;
  padding: 8px;
  text-align: center;
  text-transform: uppercase;
  color: #4CAF50;
}
</style>
