<template>
  <form @submit.prevent="NewMountain">
    <h1>Register one more mountain</h1>

    <div class="from-group">
      <input type="text" class="form-control" v-model="name" placeholder="name"/>
    </div>
    <br>

    <div class="from-group">
      <input type="mountain" class="form-control" v-model="height" placeholder="height"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="country" placeholder="country"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="region" placeholder="region"/>
    </div>
    <br>

    <button class="button button">Let's add it!</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "NewMountain",
  data() {
    return {
      name: '',
      height: '',
      country: '',
      region: '',
    }
  },
  methods: {
    async NewMountain() {
      const response = await axios.post('http://localhost:8000/alp/mountains/', {
        name: this.name,
        height: this.height,
        country: this.country,
        region: this.region,
      });
      console.log(response);
      await this.$router.push({name: 'Mountains'});
    }
  },
}
</script>
<style scoped>
</style>