<template>
  <form @submit.prevent="GroupUpdate">
    <h1>Update group information</h1>

    <div class="from-group">
      <input type="text" class="form-control" v-model="ascension" placeholder="ascension"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="result" placeholder="result"/>
    </div>
    <br>

    <div class="from-group">
      <input type="text" class="form-control" v-model="comment" placeholder="comment"/>
    </div>
    <br>

    <button class="button button">Let's add it!</button>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "GroupUpdate",
  data() {
    return {
      ascension: '',
      result: '',
      comment: '',
      climbers: '',
    }
  },
  methods: {
    async GroupUpdate() {
      const group_id = this.$route.params.group_id;
      const response = await axios.post(`http://localhost:8000/alp/groups/${group_id}/`, {
        group_id: group_id,
        ascension_id: this.ascension,
        result: this.result,
        comment: this.comment,
        climbers: [1]
      });
      console.log(response);
      await this.$router.push({name: 'Groups'});
    }
  },
}
</script>
<style scoped>
</style>