<template>
  <HelloWorld/>
  <div class="py-12 text-center text-teal-darken-4" color="teal-darken-4">
    <h2>К Л У Б Ы</h2>
  </div>
  <div class="app">

    <ClubsList
      v-bind:clubs="clubs"
    />
  </div>
</template>

<script>
import ClubsList from "@/components/ClubsList.vue"
import axios from "axios"
import HelloWorld from "@/components/HelloWorld.vue";
export default {
  name: "Clubs",
  components: {
    HelloWorld,
    ClubsList,
  },
  data() {
    return {
      clubs: []
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/clubs/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
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
