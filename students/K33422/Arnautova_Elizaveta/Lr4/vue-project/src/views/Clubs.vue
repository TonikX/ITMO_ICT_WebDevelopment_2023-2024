<template>
  <div className="app">
    <h1>Clubs</h1>
    <ClubsList
        v-bind:clubs="clubs"
    />
  </div>
</template>

<script>
import ClubsList from "@/components/ClubsList.vue"
import axios from "axios"

export default {
  name: "ClubList",
  components: {
    ClubsList,
  },
  data() {
    return {
      clubs: ['']
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/clubs/',
            {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.clubs = response.data;
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