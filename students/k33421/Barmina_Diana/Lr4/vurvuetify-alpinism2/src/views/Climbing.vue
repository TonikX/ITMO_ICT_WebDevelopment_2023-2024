<template>
  <HelloWorld/>
  <v-container>

    <v-row>
      <v-col cols="12">

        <v-card>
          <v-card-title >{{ climbing.name }}</v-card-title>

          <v-card-text >Даты проведения: {{ startDate }} - {{ endDate }}</v-card-text>
          <v-divider></v-divider>

          <v-row>
            <v-col cols="6" >
              <v-card-subtitle ><br>Подробная информация<br><br>
                Клуб-организатор: <a :href="`/clubs/${club.id}`">
                  {{ club.name }}</a><br>
                Цель восхождения: {{ mountain.name }}<br>
                Максимальное кол-во участников: {{ max_participants }}<br>
                <div v-if="dateCheck">Осталось мест: {{ free_tickets }}</div>
                Цена: {{ climbing.cost }} руб
              </v-card-subtitle>
            </v-col>
          </v-row>
          <br><v-divider></v-divider>
          <v-card-title><small>Описание:</small></v-card-title>
          <v-row>
            <v-col cols="6" >
              <v-card-text >
                {{ climbing.description }}
              </v-card-text>
            </v-col>
          </v-row>
          <br><v-divider></v-divider>
          <v-card-title><small>Участники:</small></v-card-title>

          <v-row>

            <v-col cols="6" v-for="alp in alpinists">
              <v-card-subtitle>
                {{ alp.first_name }} {{ alp.last_name }}<br>
                Уровень подготовки: {{ alp.experience_level }}<br>
              </v-card-subtitle>
            </v-col>
          </v-row>
          <br/><v-divider></v-divider>
          <br><v-card-actions>
          <v-spacer></v-spacer>
          <ParticipatingDelete v-if="allCheck"
                              v-bind:climbing="climbing"></ParticipatingDelete>
          <ParticipatingForm v-if="!alpinism && dateCheck" v-bind:climbing="climbing"></ParticipatingForm>
        </v-card-actions>
          <br>
        </v-card>
      <Emergency v-if="!dateCheck" v-bind:climbing="climbing"></Emergency>
      </v-col>
    </v-row>
  </v-container>

</template>

<script>
import axios from "axios";
import ParticipatingForm from "../components/ParticipatingForm.vue";
import ParticipatingDelete from "../components/ParticipatingDelete.vue";
import moment from 'moment';
import HelloWorld from "@/components/HelloWorld.vue";
import Emergency from "@/views/Emergency.vue";
export default {
  name: "Climbing",
  components: {Emergency, HelloWorld, ParticipatingDelete, ParticipatingForm},
  data() {
    return {
      climbing: '',
      club: '',
      mountain: '',
      alpinists: [''],
      start_date_plan: '',
      finish_date_plan: '',
      free_tickets: '',
      max_participants: '',
      today: new Date().toISOString().substr(0, 10),
    }
  },
  methods: {
    async getData() {
      try {
        const climbing_id = this.$route.params.climbing_id;

        const response = await axios.get(`http://localhost:8000/alp/climbings/${climbing_id}`,
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.climbing = response.data;
        this.club = response.data.club_id;
        this.mountain = response.data.mountain_id;
        this.alpinists = response.data.alpinists;
        this.start_date_plan = response.data.start_date_plan;
        this.finish_date_plan = response.data.finish_date_plan;
        this.max_participants = response.data.max_participants;
        this.free_tickets = this.max_participants - this.alpinists.length;
        if (this.free_tickets == 0) {
          this.free_tickets = "мест больше нет";
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    alpinism() {
      let array = [];
      let alpinists = this.alpinists;
      if (alpinists.length < this.climbing.max_participants) {
        for (const alp in alpinists) {
          array.push(alpinists[alp].id);
        }
        let user = sessionStorage.getItem("user_id")
        for (let i in array) {
          if (array[i] == user) {
            return true
          }
        }
      }
    },
    startDate() {
      return moment(this.start_date_plan).format('DD.MM.YYYY HH:mm');
    },
    endDate() {
      return moment(this.finish_date_plan).format('DD.MM.YYYY HH:mm');
    },
    dateCheck() {
      if (this.start_date_plan >= this.today) {
        return true
      }
    },
    allCheck() {
      if (this.dateCheck && this.alpinism) {
        console.log(this.dateCheck, this.alpinism)
        return true
      }
    }

    /*alpinism2() {
      let array = [];
      let alpinists = this.climbing.alpinists;

      for (const alp in alpinists) {
        array.push(alpinists[alp].id);
      }
      let user = sessionStorage.getItem("user_id")
      for (let i in array) {
        if (array[i] == user) {
          return true
        }
      }
    }*/
  },
  mounted() {
    this.getData();
  }
}
</script>

<style scoped>

</style>
