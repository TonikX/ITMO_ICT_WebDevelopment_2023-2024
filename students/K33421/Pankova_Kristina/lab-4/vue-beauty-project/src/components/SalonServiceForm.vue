<template>
  <div>
    <form @submit.prevent="submitForm">
      <div>
        <label for="salon">Salon:</label>
        <select v-model="appointment.salon" id="salon">
          <option v-for="salon in salons" :value="salon.id">{{ salon.name }}</option>
        </select>
      </div>
      <div>
        <label for="customer">Customer:</label>
        <select v-model="appointment.customer" id="customer">
          <option v-for="customer in customers" :value="customer.id">{{ customer.username }}</option>
        </select>
      </div>
      <div>
        <label for="service">Service:</label>
        <select v-model="appointment.service" id="service">
          <option v-for="service in services" :value="service.id">{{ service.name }}</option>
        </select>
      </div>
      <div>
        <label for="datetime">Date and Time:</label>
        <input type="datetime-local" v-model="appointment.datetime" id="datetime">
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
  data() {
    return {
      appointment: {
        salon: null,
        customer: null,
        service: null,
        datetime: moment(new Date().toISOString()).format('YYYY-MM-DD')
      },
      salons: [],
      customers: [],
      services: []
    };
  },
  created() {
    // Fetch data from backend endpoints
    this.fetchSalons();
    this.fetchCustomers();
    this.fetchServices();
  },
 computed: {
    formattedDate() {
      return moment(this.appointment.datetime).format('YYYY-MM-DD');
    }
  },

  methods: {
    fetchSalons() {
      fetch('http://127.0.0.1:8000/salon/salons/')
        .then(response => response.json())
        .then(data => {
          this.salons = data;
        });
    },
    fetchCustomers() {
      fetch('http://127.0.0.1:8000/salon/customers/')
        .then(response => response.json())
        .then(data => {
          this.customers = data;
        });
    },
    fetchServices() {
      fetch('http://127.0.0.1:8000/salon/services/')
        .then(response => response.json())
        .then(data => {
          this.services = data;
        });
    },
    submitForm() {
    this.appointment.datetime = moment(this.appointment.datetime).format('YYYY-MM-DD');
    console.log(this.appointment);
      axios.post('http://127.0.0.1:8000/salon/appointments/create/', this.appointment)
        .then(response => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch(error => {
          // Handle form submission error
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
select {
  border: 2px solid grey;
}
input {
  border: 2px solid grey;
}

button {
  background-color: #04AA6D; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}

</style>
