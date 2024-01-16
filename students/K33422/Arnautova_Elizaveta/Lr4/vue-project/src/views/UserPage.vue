<template>
  <div>
    <h1> Hello, {{ user.username }}</h1>
    <h2>We are glad to see you here</h2>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "UserPage",
  data() {
    return {
      user: ''
    }
  },
  methods: {
    async getUserData() {
      try {
        const response = await axios.get('http://localhost:8000/auth/users/me',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.user = response.data;
        sessionStorage.setItem('user_id', this.user.id)
      } catch (error) {
        console.log(error);
      }
    }
  },
  created() {
    this.getUserData();
  }
}
</script>
<style scoped>
</style>