<template>
  <v-btn variant="flat" color="green" @click="createParticipating">Участвовать</v-btn>
</template>

<script>
import axios from "axios";

export default {
  name: "ParticipatingForm",
  props: {climbing: {required:true}},
  methods: {
    async createParticipating() {
      try {

        //console.log(sessionStorage.getItem('user_id'));
        //console.log(this.club.name)
        const response = await axios.post(`http://localhost:8000/alp/userpage/${sessionStorage.getItem('user_id')}/climbings-participation/${this.climbing.id}/create/`,
          {
            climbing_id: this.climbing.id,
            alpinist_id: sessionStorage.getItem('user_id')
          },
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
        ).then(() => {
          // Обновление данных прошло успешно
          location.reload(); // перезагрузить страницу
        })

      } catch (error) {
        console.log(error);
      }
    },

  }
}
</script>

<style scoped>

</style>
