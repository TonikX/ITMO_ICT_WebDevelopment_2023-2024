<template>
  <div>
    <form @submit.prevent="submitForm">
      <div >
        <label for="salon">Salon:</label>
        <select v-model="editedAppointment.salon" id="salon">
          <option v-for="salon in salons" :value="salon.id">{{ salon.name }}</option>
        </select>
      </div>
      <div>
        <label for="customer">Customer:</label>
        <select v-model="editedAppointment.customer" id="customer">
          <option v-for="customer in customers" :value="customer.id">{{ customer.username }}</option>
        </select>
      </div>
      <div>
        <label for="service">Service:</label>
        <select v-model="editedAppointment.service" id="service">
          <option v-for="service in services" :value="service.id">{{ service.name }}</option>
        </select>
      </div>
      <div>
        <label for="datetime">Date and Time:</label>
        <input type="datetime-local" v-model="editedAppointment.datetime" id="datetime">
      </div>
      <button type="submit">Save</button>
      <button v-on:click="cancelEdit">Cancel</button>
    </form>
  </div>
</template>


<style scoped>
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

select {
  border: 2px solid grey;
}
input {
  border: 2px solid grey;
}
</style>


<script>
import moment from "moment";
import axios from "axios";

export default {
  props: ["appointment"],
  data() {
    return {
      editedAppointment: { ...this.appointment },
      salons: [],
      customers: [],
      services: [],
    };
  },
  created() {
    this.fetchSalons();
    this.fetchCustomers();
    this.fetchServices();
  },
  methods: {
    fetchSalons() {
      fetch("http://127.0.0.1:8000/salon/salons/")
        .then((response) => response.json())
        .then((data) => {
          this.salons = data;
        });
    },
    fetchCustomers() {
      fetch("http://127.0.0.1:8000/salon/customers/")
        .then((response) => response.json())
        .then((data) => {
          this.customers = data;
        });
    },
    fetchServices() {
      fetch("http://127.0.0.1:8000/salon/services/")
        .then((response) => response.json())
        .then((data) => {
          this.services = data;
        });
    },
    submitForm() {
      const formattedDate = moment(this.editedAppointment.datetime).format(
        "YYYY-MM-DD"
      );
      this.editedAppointment.datetime = formattedDate;
      console.log(this.editedAppointment);
      axios
        .put(
          `http://127.0.0.1:8000/salon/appointments/${this.editedAppointment.id}/edit/`,
          this.editedAppointment
        )
        .then((response) => {
          // Handle successful form submission
          console.log(response.data);
        })
        .catch((error) => {
          // Handle form submission error
          console.error(error);
        });
    },
    cancelEdit() {
      this.$emit("cancel-edit");
    },
  },
};
</script>
