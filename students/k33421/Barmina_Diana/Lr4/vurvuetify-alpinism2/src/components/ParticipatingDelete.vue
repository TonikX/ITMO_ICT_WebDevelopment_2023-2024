<template>
  <v-btn variant="flat" color="red" @click="deleteParticipating">Отказаться от участия</v-btn>
</template>

<script>
import axios from "axios";

export default {
  name: "ParticipatingDelete",
  props: {
    climbing: {
      required: true
    }
  },
  methods: {
    async deleteParticipating() {
      try {
        const response = await axios.delete(`http://localhost:8000/alp/userpage/participatings/${this.climbing.id}/delete/`,
          {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
        ).then(() => {
          // Обновление данных прошло успешно
          location.reload(); // перезагрузить страницу
        })
      } catch (error) {
        console.log(error);
      }
    }
  },
}
</script>

<style scoped>

</style>
