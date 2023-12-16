<template>
    <v-container>
      <v-col v-for="podcast in podcasts" :key="podcast.id" cols="12">
        <v-card @click="navigateToSinglePodcast(podcast.id)">
          <div class="d-flex flex-no-wrap justify-space-between align-center">
            <div>
              <v-card-title class="text-h5">{{ podcast.name }}</v-card-title>
              <v-card-subtitle>Последняя дата обновления: {{ podcast.date_of_last_issue_release }}<br>
              Количество выпусков: {{ podcast.issues_count }}</v-card-subtitle>
              <v-card-text>{{ podcast.description }}</v-card-text>
            </div>
            <v-avatar class="ma-3" size="150" rounded="0">
              <v-img :src="podcast.cover_picture"></v-img>
            </v-avatar>
          </div>
        </v-card>
      </v-col>
    </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      podcasts: [],
    };
  },
  mounted() {
    this.fetchPodcasts();
  },
  methods: {
    fetchPodcasts() {
      const apiUrl = this.$websiteURL + '/podcast';
      axios.get(apiUrl)
        .then(response => {
          this.podcasts = response.data;
        })
        .catch(error => {
          console.error('Error fetching podcasts:', error);
        });
    },
    navigateToSinglePodcast(podcastId) {
      this.$router.push({ name: 'single-podcast', params: { id: podcastId } });
    },
  },
};
</script>

<style scoped>
/* Add your custom styles here */
</style>
