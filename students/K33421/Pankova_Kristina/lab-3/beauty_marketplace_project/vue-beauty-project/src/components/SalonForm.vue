<template>
  <form @submit.prevent="submitForm">
    <!-- Other form fields -->
    <div>
      <label for="owner">Owner:</label>
      <select id="owner" v-model="salon.owner" required>
        <option v-for="owner in owners" :value="owner.id">{{ owner.username }}</option>
      </select>
      <br />

            <label for="name">Name:</label>
      <input type="text" id="name" v-model="salon.name" required>
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
<style>
input[type=text], select {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

input[type=submit] {
  width: 100%;
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button[type="submit"] {
  background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 10px;
}

button[type="submit"]:hover {
  background-color: #45a049; /* Darker green */
}


input[type=submit]:hover {
  background-color: #45a049;
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
