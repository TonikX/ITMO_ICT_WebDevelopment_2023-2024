<template>

  <div>
    <h1>Groups</h1>
      <div class="card" v-for='group in groups'>
        <h3>{{ group.ascension }}</h3>
        <strong>Ascention result: </strong>{{ group.result }} <br>
        <strong>Leader comment:</strong> {{ group.comment }}<br>
        <strong>Who is there?</strong>
        <li v-for='one in group.climbers'>
           {{ one }} <br>
        </li>
        <div class="buttoncard">
        <button class="button button" @click="$router.push(`/alp/groups/${group.id}`)">details</button> <br> <br>
      </div>
      </div>
  </div>
</template>

<script>
import axios from "axios"
export default {
  name: "groups",
  data() {
    return {
      groups: [''],
      ascension: '',
      result: '',
      comment: '',
      climbers: '',
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/groups/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
        );
        this.groups = response.data;
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