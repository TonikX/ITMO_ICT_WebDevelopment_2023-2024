<template>
  <v-container>
    <!-- Заголовок и описание проекта -->
    <v-row class="my-5">
      <v-col>
        <v-card class="elevation-2" color="deep-purple accent-4" dark>
          <v-card-title class="headline">Welcome to the Climbers' Portal</v-card-title>
          <v-card-text>
            This API-driven platform provides information about various climbing routes and mountains.
            Engage with the climbing community and explore mountains from around the world.
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <!-- Список гор -->
    <v-row>
      <v-col>
        <v-card class="elevation-2" color="indigo">
          <v-card-title class="headline">
            Mountains
            <v-spacer></v-spacer>
            <v-text-field
                v-model="search"
                append-icon="mdi-magnify"
                label="Search mountains"
                single-line
                hide-details
            ></v-text-field>
          </v-card-title>
          <v-card-text>
            <v-list three-line>
              <v-list-item-group v-model="selectedMountain" color="primary">
                <v-list-item
                    v-for="mountain in filteredMountains"
                    :key="mountain.name"
                    @click="selectMountain(mountain)"
                >
                  <v-list-item-content>
                    <v-list-item-title class="headline mb-1">{{ mountain.name }}</v-list-item-title>
                    <v-list-item-subtitle>
                      <v-icon small class="mr-1">mdi-altimeter</v-icon>
                      {{ mountain.height }} m
                      <v-icon small class="mx-2">mdi-map-marker</v-icon>
                      {{ mountain.country }}, {{ mountain.region }}
                    </v-list-item-subtitle>
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-icon>mdi-mountain</v-icon>
                  </v-list-item-action>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from '@/api';

export default {
  name: 'HomePage',
  data() {
    return {
      mountains: [], // For storing the list of mountains
      selectedMountain: null, // For storing the selected mountain
      search: '', // For the search input
    };
  },
  computed: {
    filteredMountains() {
      return this.mountains.filter(mountain => {
        return mountain.name.toLowerCase().includes(this.search.toLowerCase());
      });
    },
  },
  methods: {
    fetchMountains() {
      api.get('mountains/')
          .then(response => {
            this.mountains = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the mountains:", error);
          });
    },
    selectMountain(mountain) {
      this.selectedMountain = mountain;
      this.$router.push({name: 'MountainDetail', params: {id: mountain.id}});
    },
  },
  mounted() {
    this.fetchMountains();
  }
};
</script>
