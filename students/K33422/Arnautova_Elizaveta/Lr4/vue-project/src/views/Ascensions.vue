<template>

  <div class="container">
    <h1>Ascensions</h1>
    <div class="card" v-for="ascension in ascensions">
      <strong>Ascension:</strong> {{ ascension.route}}<br>
      <strong>Calendar:</strong> from {{ ascension.start_date }} till {{ ascension.planned_end_date }}
      <br>
      <div class="buttoncard">
        <button class="button button" @click="$router.push(`/alp/ascensions/${ascension.id}`)">details</button> <br> <br>
      </div>
    </div> <br>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AscensionsList",
  data() {
    return {
      ascensions: ['']
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/ascensions/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
        );
        this.ascensions = response.data;
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
.button {
  padding: 2px 180px;
}
</style>