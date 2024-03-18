<template>

  <div class="container">
    <h1>Mountains</h1>
    <div class="card" v-for='mountain in mountains'>
      <h3>{{ mountain.name }}</h3>
      height: {{ mountain.height }} <br>
      country: {{ mountain.country }}, region: {{ mountain.region }}
    </div>
    <br>
    <div class="card">
      <h1> Hasn't find your favorite mountain? </h1>
      <button class="button button" @click="$router.push(`/alp/mountains/new`)">Add it to our list</button>
    </div>
    <br>
    <div class="card">
      <h1> By the way! </h1>
      <h3> There are mountains that no one has climbed yet. You can be the first!</h3>
      <button class="button button" @click="$router.push(`/mountains/noclimbers/`)">Get information!</button>

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
        const response = await axios.get('http://localhost:8000/alp/mountains/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
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
.button {
  padding: 2px 200px;
}
</style>