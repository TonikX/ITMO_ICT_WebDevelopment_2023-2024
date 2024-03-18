<template>
  <form @submit.prevent="AscensionUpdate">
    <h1>Update ascension</h1>

    <div class="from-group">
      <input type="text" class="form-control" v-model="start_date" placeholder="yyyy-mm-dd"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="planned_end_date" placeholder="yyyy-mm-dd"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="actual_end_date" placeholder="yyyy-mm-dd"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="comment" placeholder="comment"/>
    </div>
    <br>


    <button class="button button">Update!</button>
  </form>
</template>

<script>
import axios from "axios";
export default {
  name: "AscensionUpdate",
  data() {
    return {
      start_date: '',
      planned_end_date: '',
      actual_end_date: '',
      comment: '',
    }
  },
  methods: {

    async AscensionUpdate() {
      const ascension_id = this.$route.params.ascension_id;
      const response = await axios.post(`http://localhost:8000/alp/ascensions/${ascension_id}/`, {
        route_id: ascension_id,
        start_date: this.start_date,
        planned_end_date: this.planned_end_date,
        actual_end_date: this.actual_end_date,
        comment: this.comment,
      });
      console.log(response);
      await this.$router.push({name: 'Ascensions'});
    },
  },
}

</script>
<style scoped>
</style>