<template>
  <v-container>
    <v-expansion-panels>
      <v-expansion-panel
        title="Возникшие экстренные ситуации"
        color="black"
      >
        <v-expansion-panel-text>
          <v-card>
            <v-card-title></v-card-title>
            <v-card-text v-for="em in emergency">
              Тип: {{ em.type }}<br>
              Описание: {{ em.description }}<br>
              Пострадавший: {{ em.participating_id.alpinist_id.first_name }} {{ em.participating_id.alpinist_id.last_name }}
            </v-card-text>

          </v-card>
        </v-expansion-panel-text>
      </v-expansion-panel>

    </v-expansion-panels>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Emergency",
  props: {climbing: {required:true}},
  data() {
    return {
      emergency: [],
    }
  },
  methods: {
    async getEmergency() {

      const response = await axios.get('http://localhost:8000/alp/emergency/',
        {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      const array = response.data;
      console.log(array)
      for (let a in array) {
        const alp = array[a].participating_id.climbing_id
        console.log(alp.id, this.climbing.id)

        if (alp.id === this.climbing.id) {
          this.emergency.push(array[a]);
        }
      }
      console.log(this.emergency);

    },
  },
  computed: {

  },
  mounted() {
    this.getEmergency();
  }
}
</script>

<style scoped>

</style>
