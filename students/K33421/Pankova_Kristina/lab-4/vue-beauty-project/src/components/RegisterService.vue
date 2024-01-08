<template>
  <form @submit.prevent="submitForm">
    <!-- Other form fields -->
    <div>
      <label for="salon">Salon:</label>
      <select id="salon" v-model="salon" required>
        <option v-for="salon in salons" :value="salon.id">{{ salon.name }}</option>
      </select>
      <br />
            <label for="name">Customer:</label>
      <input type="text" id="customer" v-model="salon.customer" required>
    </div>
    <div>
      <label for="type">Type:</label>
      <input type="text" id="type" v-model="salon.type" required>
    </div>
    <div>
      <label for="city">City:</label>
      <input type="text" id="city" v-model="salon.city">
    </div>
    <div>
      <label for="description">Description:</label>
      <input type="text" id="description" v-model="salon.description">
      <input type="hidden" id="date_registered" v-model="salon.date_registered" />

    </div>
    <button type="submit">Submit</button>
  </form>
</template>
<style scoped>
.button["submit"] {
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

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>

<script>
import axios from 'axios';
import moment from 'moment';

export default {
  data() {
    return {
      salon: {
        name: '',
        type: '',
        city: '',
        description: '',
        owner: null,  // Initialize owner as null
        date_registered: moment(new Date().toISOString()).format('YYYY-MM-DD')  // Initialize date_registered with current time
      },
      owners: []  // Array to store the list of owners
    };
  },
  computed: {
    formattedDate() {
      return moment(this.salon.date_registered).format('YYYY-MM-DD');
    }
  },
  created() {
    // Fetch the list of owners from the Django backend when the component is created
    axios.get('http://127.0.0.1:8000/salon/owners/')
      .then(response => {
        this.owners = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/salon/salons/create/', this.salon)
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
