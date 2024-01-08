<template>
  <form @submit.prevent="submitForm">
    <!-- Other form fields -->
    <div>
      <br />

    <label for="password">Password:</label>
      <input type="text" id="password" v-model="owner.password" required>
    </div>
    <div>
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="owner.username" required>
    </div>
    <div>
      <label for="first_name">First name:</label>
      <input type="text" id="first_name" v-model="owner.first_name">
    </div>
    <div>
      <label for="last_name">Last name:</label>
      <input type="text" id="last_name" v-model="owner.last_name">
    </div>

    <div>
      <label for="email">Email:</label>
      <input type="text" id="email" v-model="owner.email">
    </div>

    <div>
      <label for="phone_number">Phone number:</label>
      <input type="text" id="phone_number" v-model="owner.phone_number">
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

input[type=submit]:hover {
  background-color: #45a049;
}

div {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding-left: 0px;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      owner: {
        password: '',
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
      },
      owners: []  // Array to store the list of owners
    };
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8000/salon/owners/create/', this.owner)
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
