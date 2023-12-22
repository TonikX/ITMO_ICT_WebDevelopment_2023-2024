
<template>
  <HelloWorld/>
  <v-container >
    <div class="py-12 text-center text-indigo">
      <h2>Г О Р Ы</h2>
    </div>
    <v-expansion-panels style="max-width: 500px; left: 28.6%; ">
      <v-expansion-panel
        title="Фильтрация"
        color="indigo">

        <v-expansion-panel-text>
          Название:<v-text-field
          v-model="name"
          hide-details
          placeholder="название содержит слова"
          variant="outlined"
        ></v-text-field>
          Страна:<v-text-field
          v-model="state"
          hide-details
          placeholder="название содержит слова"
          variant="outlined"
        >
        </v-text-field>
          Высота:<v-text-field
          v-model="min_height"
          hide-details
          placeholder="минимальная высота"
          variant="outlined"
        ></v-text-field>
          <br>
          <v-text-field
            v-model="max_height"
            hide-details
            placeholder="максимальная высота"
            variant="outlined"
          ></v-text-field>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn variant="text" color="primary" @click="applyFilter"> Применить фильтры </v-btn>
          </v-card-actions>
        </v-expansion-panel-text>

      </v-expansion-panel>
    </v-expansion-panels>
    <br>
    <v-row align="center" justify="center">
      <v-col
        v-for="mountain in mountains"
        :key="mountain"
        cols="auto"
        margin-bottom="20px"
      >
        <v-card
          class="mx-auto"
          max-width="500px"
          color="indigo"
          variant="outlined"
        >
          <v-card-item>
            <div>
              <div class="text-overline mb-1">
                Высота: {{ mountain.hight }} м
              </div>
              <div class="text-h6 mb-1">
                {{ mountain.name }}
              </div>
              <div class="text-caption">{{ mountain.state }}, {{ mountain.area }}</div>
            </div>
          </v-card-item>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>



<script>
import axios from "axios"
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "mountains",
  components: {HelloWorld},

  data() {
    return {
      mountains: [],
      name: '',
      state: '',
      max_height: '',
      min_height: '',
    }
  },
  methods: {
    async getData() {
      try {
        const response = await axios.get('http://localhost:8000/alp/mountains/',
          { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
        this.mountains = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async applyFilter() {
      const filter = `http://localhost:8000/alp/mountains/?name=${this.name}&state=${this.state}&min_height=${this.min_height}&max_height=${this.max_height}`
      const response = await axios.get(filter,//`http://localhost:8000/alp/mountains/?search=${this.filterValue}`,
        { headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}});
      this.mountains = response.data;
    },
  },
  created() {
    this.getData();
  }
}
</script>

<style scoped>
.hero {
  background: url('../assets/images.jpg');
  background-size: cover;
  height: 100vh;
}
</style>
