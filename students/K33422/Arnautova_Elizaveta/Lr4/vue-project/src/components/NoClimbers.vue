<template>

  <div class="container">
    <h1>Mountains</h1>
    <h2>Peaks that have not yet been conquered by anyone</h2>
    <br>
    <div class="card" v-for='mountain in mountains'>
      <h3>{{ mountain.name }}</h3>
      height: {{ mountain.height }} <br> country: {{ mountain.country }}, region: {{ mountain.region }}
      <br>
    </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "mountains",
  data() {
    return {
      mountains: [''],
      name: '',
      height: '',
      country: '',
      region: '',
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/mountains/noclimbers/',
            {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.mountains = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  created() {
    this.getData();
  }
}
</script>
<style scoped>
</style>