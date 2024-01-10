<template>
  <v-container>
    <!-- Детали Горы -->
    <v-row class="my-5" v-if="mountain">
      <v-col>
        <v-card class="elevation-2">
          <v-card-title class="headline">{{ mountain.name }}</v-card-title>
          <v-card-text>
            <p>Height: {{ mountain.height }} м</p>
            <p>Location: {{ mountain.country }}, {{ mountain.region }}</p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <!-- Список Маршрутов -->
    <v-row>
      <v-col>
        <v-card class="elevation-2">
          <v-card-title class="headline">Routes</v-card-title>
          <v-card-text>
            <v-list dense>
              <v-list-item
                  v-for="route in routes"
                  :key="route.id"
              >
                <v-list-item-content>
                  <v-list-item-title>{{ route.name }}</v-list-item-title>
                  <v-list-item-subtitle>{{ route.description }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from "@/api";

export default {
  name: 'MountainDetail',
  data() {
    return {
      mountain: null,
      routes: []
    };
  },
  methods: {
    fetchMountainDetails() {
      const mountainId = this.$route.params.id;
      api.get(`mountains/${mountainId}/`)
          .then(response => {
            this.mountain = response.data;
            this.fetchRoutes(this.mountain.name);
          })
          .catch(error => {
            console.error("There was an error fetching the mountain details:", error);
          });
    },
    fetchRoutes(mountainName) {
      api.get('routes/', {params: {search: mountainName}})
          .then(response => {
            this.routes = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the routes:", error);
          });
    }
  },
  mounted() {
    this.fetchMountainDetails();
  }
};
</script>

