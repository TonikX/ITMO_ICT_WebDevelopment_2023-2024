<template>

    <div v-if="isAuthenticated">
      <!-- Show authenticated content -->
      <h1>Welcome, {{ user }}!</h1>
      <button @click="logout">Logout</button>
    </div>
    <div v-else>
      <h1>Welcome, AnonUser!</h1>
    </div>

</template>
<style>
.div {
  padding: 0;
  margin: 0;
}

.button {
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


<script>
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
      currentUser: {}
    };
  },
  mounted() {
    this.fetchCurrentUser();
  },
  methods: {
    async fetchCurrentUser() {
      try {
        const response = await fetch('http://127.0.0.1:8000/salon/api/current_user/');
        console.log(response);
        const data = await response.json();
        console.log(data);
        this.currentUser = data;
      } catch (error) {
        console.error('Error fetching current user:', error);
      }
    }
  }
};
</script>