<template>
  <v-container>
    <v-row>
      <v-col v-for="item in items" :key="item.id" cols="12" md="6">
        <v-card @click="openExternalLink(item.external_reference_link)" class="mx-auto" width="500" height="300">
          <v-img :src="item.cover_picture" height="200" ></v-img>
          <v-card-title>{{ item.name }}</v-card-title>
          <v-card-subtitle v-if="item.short_description">{{ item.short_description }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    this.fetchWhatWeDoData();
  },
  methods: {
    fetchWhatWeDoData() {
      axios.get(this.$websiteURL + '/whatwedo')
        .then(response => {
          this.items = response.data.results;
        })
        .catch(error => {
          console.error('Error fetching What We Do data:', error);
        });
    },
    openExternalLink(link) {
      if (link) {
        window.open(link, '_blank');
      }
    },
  },
};
</script>

<style scoped>
/* Add custom styles if needed */
</style>
