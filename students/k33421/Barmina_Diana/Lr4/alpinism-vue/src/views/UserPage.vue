<template>
  <div>
    <h2>{{ user.first_name }} {{ user.last_name }} ({{ user.id }})</h2>
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
        const response = await axios.get('http://localhost:8000/alp/auth/users/me',
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
