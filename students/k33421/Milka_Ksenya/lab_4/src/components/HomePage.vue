<template>
  <v-container fluid>
    <v-row justify="center">
      <v-col cols="12" md="10">
        <v-card class="elevation-10" dark>
          <v-card-title class="display-1 text-center py-5">
            Портал Альпинистов: Ваш путеводитель по вершинам всех стран!
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-list three-line subheader>
              <v-subheader class="text-h5 py-3">
                Доступные Вершины
              </v-subheader>
              <v-list-item-group v-model="selectedMountain" color="secondary">
                <v-list-item
                    v-for="peak in filteredMountains"
                    :key="peak.name"
                    class="my-2"
                >
                  <v-list-item-content @click="selectMountain(peak)">
                    <v-list-item-title class="headline mb-1">{{ peak.name }}</v-list-item-title>
                    <v-list-item-subtitle>
                      <v-icon small class="mr-1">mdi-altimeter</v-icon>
                      {{ peak.height }} м
                      <v-icon small class="mx-2">mdi-map-marker</v-icon>
                      {{ peak.country }}, {{ peak.region }}
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
      mountains: [],
      selectedMountain: null,
      search: '',
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