<template>
  <div class="card">
    <h1>{{ club.name }}</h1>
    {{club.country}}, {{ club.city }}
    <br>
    <h2>Контактное лицо:</h2>
    <h3>{{club.contact_person}}</h3>
    email: {{club.email}} <br> phone: {{club.phone}}

  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Club",
  data() {
    return {
      club: '',
    }
  },
  methods: {
    async getData() {
      try {
        const club_id = this.$route.params.club_id;
        const response = await axios.get(`http://localhost:8000/alp/clubs/${club_id}`,
            { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.club = response.data;
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