<template>
  <div>
    <br/><button @click="createMembership">Стать членом клуба</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ClubMembershipForm",
  props: {club: {required:true}},
  methods: {
    async createMembership() {
      try {

        console.log(sessionStorage.getItem('user_id'));
        console.log(this.club.name)
        const response = await axios.post(`http://localhost:8000/alp/userpage/${sessionStorage.getItem('user_id')}/club-membership/create/`,
          {
          club_id: this.club.id,
          alpinist_id: sessionStorage.getItem('user_id')
        },
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});

      } catch (error) {
        console.log(error);
      }
    },

  }
}
</script>

<style scoped>

</style>
