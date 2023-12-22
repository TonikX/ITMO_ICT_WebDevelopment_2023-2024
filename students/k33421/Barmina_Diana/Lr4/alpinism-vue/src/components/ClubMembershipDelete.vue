<template>
  <div>
    <br/><button @click="deleteMembership">Выйти из клуба</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ClubMembershipDelete",
  props: {
    club: {
      required: true
    }
  },
  methods: {
    async deleteMembership() {
      try {
        const response = await axios.delete(`http://localhost:8000/alp/userpage/club-membership/${this.club.id}/delete/`,
          {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      } catch (error) {
        console.log(error);
      }
    }
  },
}
</script>

<style scoped>

</style>
