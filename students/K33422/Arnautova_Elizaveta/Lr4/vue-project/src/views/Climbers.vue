<template>

  <div class="container">
    <h1>Climbers</h1>
    <div class="card" v-for="climber in climbers">
      <h3>{{ climber.first_name}} {{ climber.last_name}}:</h3>
      <strong>address:</strong> {{ climber.address}}<br>
      <strong>birth_date:</strong> {{ climber.birth_date}}<br>
      <strong>phone:</strong> {{ climber.phone}}
      <br>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Climbers",
  data() {
    return {
      climbers: ['']
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/climbers/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
        );
        this.climbers = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("token")) {
        return true
      }
    }
  },
  mounted() {
    this.getData();
  }
}
</script>
<style scoped>
</style>
