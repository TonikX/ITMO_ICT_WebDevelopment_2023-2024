<template>
  <div>
    <h1>{{ ascension.route}}</h1>
    <div><strong>Schedule:</strong> from {{ ascension.start_date }} till {{ ascension.planned_end_date }}</div>
    <div v-if="ascension.actual_end_date !== null"> <strong>Actual end date:</strong>  {{ ascension.actual_end_date }}</div>
    <div v-if="ascension.comment !== null"> <strong>Leader comment:</strong>  {{ ascension.comment }}</div>
    <a v-if="ascension.actual_end_date == null"> The ascension has not finished yet</a>
    <br><br>
    <h3>I want to update information a bit</h3>
    <button class="button button" @click="$router.push(`/alp/ascensions/update/${ascension.id}`)">update</button>

  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Ascension",
  data() {
    return {
      ascension: '',
    }
  },
  methods: {
    async getData() {
      try {
        const ascension_id = this.$route.params.ascension_id;
        const response = await axios.get(`http://localhost:8000/alp/ascensions/${ascension_id}`,
            { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.ascension = response.data;
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getData();
  }
}
</script>
<style scoped>
</style>