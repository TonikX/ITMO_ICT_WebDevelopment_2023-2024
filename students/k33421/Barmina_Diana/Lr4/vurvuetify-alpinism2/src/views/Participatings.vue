<template>
  <v-container>
    <v-expansion-panels>
      <v-expansion-panel
        title="Мои предстоящие участия"
        color="deep-orange-accent-4"
      >
        <v-expansion-panel-text>
          <v-card>
            <v-card-title></v-card-title>
            <v-card-text v-for="p in participatings_future">
              <a :href="`/climbings/${p.climbing_id.id}`">
                {{ p.climbing_id.name }}</a><br>

              Подтверждено администратором: {{ p.admin_confirmation }}<br>
              <br>
              <ParticipatingDelete
                v-bind:climbing="p.climbing_id">
              </ParticipatingDelete>

            </v-card-text>

          </v-card>
        </v-expansion-panel-text>
      </v-expansion-panel>

    </v-expansion-panels>
    <br>
    <v-expansion-panels>
      <v-expansion-panel
        title="Мои прошедшие участия"
        color="deep-purple-accent-2">
        <v-expansion-panel-text>
        <v-card>
          <v-card-text v-for="p in participatings_past">
            <a :href="`/climbings/${p.climbing_id.id}`">
              {{ p.climbing_id.name }}</a><br>

            Понравилось: {{ (p.succeed) }}<br>
            <br><ParticipatingUpdate
            v-bind:climbing="p">
          </ParticipatingUpdate>
          </v-card-text>
        </v-card>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-container>

</template>

<script>
import axios from "axios";
import ParticipatingDelete from "@/components/ParticipatingDelete.vue";
import ParticipatingUpdate from "@/components/ParticipatingUpdate.vue";

export default {
  name: "Participatings",
  components: {ParticipatingUpdate, ParticipatingDelete},

  data() {
    return {
      participatings_future: [],
      participatings_past: [],
      today: new Date().toISOString().substr(0, 10),
    }
  },
  methods: {
    async getParticipatings() {

      const response = await axios.get('http://localhost:8000/alp/participatings/',
        {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      const array = response.data;
      console.log(array)
      for (let a in array) {
        const alp = array[a].alpinist_id

        if (alp.id == sessionStorage.getItem('user_id')) {
          //this.participatings.push(array[a]);
          if (array[a].succeed === true) {
            array[a].succeed = 'Да';
          }
          if (array[a].succeed === false) {
            array[a].succeed = 'Нет'
          }
          if (array[a].admin_confirmation === true) {
            array[a].admin_confirmation = 'Да';
          }
          if (array[a].admin_confirmation === false) {
            array[a].admin_confirmation = 'Нет'
          }
          if (array[a].climbing_id.start_date_plan >= this.today) {
            this.participatings_future.push(array[a]);
          }
          if (array[a].climbing_id.start_date_plan < this.today) {
            this.participatings_past.push(array[a]);
          }

        }
      }
      console.log(this.participatings_past);
      console.log(this.participatings_future);
    },
  },
  computed: {

  },
  mounted() {
    this.getParticipatings();
  }
}
</script>

<style scoped>

</style>
