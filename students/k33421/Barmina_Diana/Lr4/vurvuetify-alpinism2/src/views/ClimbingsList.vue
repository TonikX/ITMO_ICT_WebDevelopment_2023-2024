<template>
  <HelloWorld/>
  <v-container >
    <div class="py-12 text-center text-pink-darken-4">
      <h2>В О С Х О Ж Д Е Н И Я</h2>
    </div>
    <br>
    <v-expansion-panels  style="max-width: 500px; left: 28.6%;">
      <v-expansion-panel
        title="Фильтрация"
        color="pink-darken-4">

        <v-expansion-panel-text >
          <v-select
            v-model="club_id"
            label="Клуб-организатор"
            :items="club_variants"
            item-title="name"
            item-value="id"
            variant="outlined">
            <template v-slot:item="{ props, item }">
              <v-list-item v-bind="props" ></v-list-item>
            </template>
          </v-select>
          <v-select
            v-model="mountain_id"
            label="Цель восхождения"
            :items="mountain_variants"
            item-title="name"
            item-value="id"
            variant="outlined">
            <template v-slot:item="{ props, item }">
              <v-list-item v-bind="props" ></v-list-item>
            </template>
          </v-select>
          <v-select
            v-model="level"
            label="Уровень сложности"
            :items="levels"
            variant="outlined">
          </v-select>
          <v-text-field
            v-model="min_cost"
            variant="outlined"
            label="Минимальная цена"
            required
            ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="max_cost"
            label="Максимальная цена"
            required
            ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="min_date_start"
            class="form-control"
            type="date"
            label="Дата начала от"
            required
          ></v-text-field>
          <v-text-field
            variant="outlined"
            v-model="max_date_start"
            class="form-control"
            type="date"
            label="Дата начала до"
            required
          ></v-text-field>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn variant="text" color="black" @click="applyFilter"> Применить фильтры </v-btn>
              <v-btn variant="text" color="red" @click="getData"> Сбросить фильтры </v-btn>
            </v-card-actions>
        </v-expansion-panel-text>

      </v-expansion-panel>
    </v-expansion-panels>
    <br><br>
    <v-row v-if="isAnything" align="center" justify="center">
      <v-col
        v-for="c in climbings"
        :key="c"
        cols="12"
        margin-bottom="20px"
      >
        <v-card
          class="mx-auto"
          max-width="550px"
          color="pink-darken-4"
          variant="outlined"
        >
          <v-card-item>
            <div>
              <div class="text-overline mb-1" style="color: black">
                {{ c.level }}
              </div>
              <div class="text-h6 mb-1" >
                {{ c.name }}
              </div>
              <div class="text-caption" style="color: black">{{ c.start_date_plan }} - {{ c.finish_date_plan }}</div>
              <div class="text-caption" style="color: black">Цена: {{ c.cost }}, Максимальное количество участников: {{ c.max_participants }}</div>
            </div>

          </v-card-item>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn variant="text" v-if="auth" color="black" @click="$router.push(`/climbings/${c.id}/`)"> Подробнее </v-btn>
          </v-card-actions>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import moment from "moment/moment";
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "ClimbingsList",
  components: {HelloWorld},
  data() {
    return {
      climbings: [],
      club_id: '',
      mountain_id: '',
      level: '',
      min_cost: '',
      max_cost: '',
      min_date_start: '',
      max_date_start: '',
      club_variants: [],
      mountain_variants: [],
      levels: ['Для всех', 'Для продвинутых', 'Для профи'],
      today: new Date().toISOString().substr(0, 10),
      //start_date_plan: '',
      //finish_date_plan: '',
    }
  },
  methods: {
    async getData() {
      try {
        this.climbings = []
        const response = await axios.get('http://localhost:8000/alp/climbings/')
          //{ headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        const array = response.data;
        for (let a in array) {
          if (array[a].start_date_plan >= this.today) {
            this.climbings.push(array[a]);
          }
        }
        for (const a in this.climbings) {
          this.climbings[a].start_date_plan = moment(this.climbings[a].start_date_plan).format('DD.MM.YYYY HH:mm');
          this.climbings[a].finish_date_plan = moment(this.climbings[a].finish_date_plan).format('DD.MM.YYYY HH:mm');
        }

      } catch (error) {
        console.log(error);
      }
    },
    async applyFilter() {
      this.climbings = []
      const filter = `http://localhost:8000/alp/climbings/?club_id=${this.club_id}&mountain_id=${this.mountain_id}&level=${this.level}&min_cost=${this.min_cost}&max_cost=${this.max_cost}&min_date=${this.min_date_start}&max_date=${this.max_date_start}`
      const response = await axios.get(filter,
        { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      const array = response.data;
      for (let a in array) {
        if (array[a].start_date_plan >= this.today) {
          this.climbings.push(array[a]);
        }
      }
      for (const a in this.climbings) {
        this.climbings[a].start_date_plan = moment(this.climbings[a].start_date_plan).format('DD.MM.YYYY HH:mm');
        this.climbings[a].finish_date_plan = moment(this.climbings[a].finish_date_plan).format('DD.MM.YYYY HH:mm');
      }
      //this.start_date_plan = response.data.start_date_plan;
      //this.finish_date_plan = response.data.finish_date_plan;
    },
    async getClubs() {
      const response = await axios.get('http://localhost:8000/alp/clubs/',
        { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      //this.club_variants = response.data;

      let array = response.data;
      for (const a in array) {
        this.club_variants.push({name: array[a].name, id: array[a].id});
      }
      console.log(this.club_variants)
    },
    async getMountains() {
      const response = await axios.get('http://localhost:8000/alp/mountains/',
        { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});


      let array = response.data;
      for (const a in array) {
        this.mountain_variants.push({name: array[a].name, id: array[a].id});
      }

    }
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("token")) {
        return true
      }
    },
    isAnything() {
      if (this.climbings.length > 0) {
        return true
      }
    }

  },
  mounted() {
    this.getData();
    this.getClubs();
    this.getMountains();
  }
}
</script>

<style scoped>

</style>
