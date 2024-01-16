<template>
  <div>
    <h1>{{ group.id}}</h1>
    <h3 v-if="group.result !== null">result {{ group.result }}</h3>
    <h3 v-if="group.comment !== null">comment {{ group.comment }}</h3>
    <li v-for='one in group.climbers'>
           {{ one }} <br>
    </li>
    <br>
    <h3>I want to update information a bit</h3>
    <button class="button button" @click="$router.push(`/alp/groups/update/${group.id}`)">update</button>

  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Group",
  data() {
    return {
      group: '',
    }
  },
  methods: {
    async getData() {
      try {
        const group_id = this.$route.params.group_id;
        const response = await axios.get(`http://localhost:8000/alp/groups/${group_id}`,
            { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.group = response.data;
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