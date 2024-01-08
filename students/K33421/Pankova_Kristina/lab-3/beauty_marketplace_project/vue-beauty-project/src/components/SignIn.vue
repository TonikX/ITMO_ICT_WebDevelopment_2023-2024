<template>
  <div>
    <div v-if="isAuthenticated">
      <!-- Show authenticated content -->
      <h3>You are already signed in as {{ user }}!</h3>
    </div>
    <div v-else>
      <!-- Show login form -->

      <input v-model="owners.username" type="text" placeholder="Username">
      <input v-model="owners.password" type="password" placeholder="Password">
      <button @click="login">Login</button>

    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    },
    user() {
      return this.$store.state.user;
    }
  },
  data() {
    return {
      owners: {
        password: '',
        username: '',
      },
    };
  },
  methods: {
    login() {
  const formData = new FormData();
  formData.append('username', this.owners.username);
  formData.append('password', this.owners.password);
  this.$store.dispatch('login', formData);
    },
    logout() {
      this.$store.dispatch('logout');
    },

  }
};
</script>


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
