<template>
  <div>
    <v-container>
      <v-row>
        <NavbarComponent/>
      </v-row>
      <v-row>
        <v-col cols="12">
          <div class="d-flex flex-no-wrap justify-space-between align-center">
            <div>
              <v-card-title class="text-h5">{{ podcast.name }}</v-card-title>
              <v-card-subtitle>
                Последняя дата обновления: {{ $formatDate(podcast.date_of_last_issue_release) }}<br/>
                Количество выпусков: {{ podcast.issues_count }}
              </v-card-subtitle>
              <v-card-text>{{ podcast.description }}</v-card-text>

              <v-list>
                <v-list-item-group v-if="podcast.podcast_links.length > 0">
                  <v-list-item v-for="link in podcast.podcast_links" :key="link.platform.id">
                    <a :href="link.external_reference_link" target="_blank">{{ link.platform.name }}</a>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </div>

            <v-avatar class="ma-3" size="300" rounded="0">
              <v-img :src="podcast.cover_picture"></v-img>
            </v-avatar>
          </div>

          <v-divider></v-divider>
          <v-container class="mt-4">
            <v-row>
              <v-col>
                <h2 class="section-title">Выпуски</h2>
              </v-col>
              <v-col cols="6" md="4">
                <v-select v-model="order" :items="orderOptions" label="Сортировать по номеру выпуска"></v-select>
              </v-col>
            </v-row>

            <PodcastIssueComponent :podcastId="id" :issues="sortedIssues"></PodcastIssueComponent>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
import PodcastIssueComponent from "@/components/PodcastIssueComponent.vue";
import NavbarComponent from "@/components/NavbarComponent.vue";

export default {
  props: {
    id: Number,
  },
  components: {
    NavbarComponent,
    PodcastIssueComponent,
  },
  data() {
    return {
      podcast: {},
      order: 'по возрастанию',
      orderOptions: ['по возрастанию', 'по убыванию'],
      sortedIssues: [],
    };
  },
  mounted() {
    this.fetchPodcastDetails();
    this.fetchPodcastIssues();
  },
  watch: {
    sortBy: 'fetchPodcastDetails',
    order: 'fetchPodcastIssues',
  },
  methods: {
    fetchPodcastDetails() {
      const apiUrl = this.$websiteURL + `/podcast/${this.id}`;

      axios.get(apiUrl)
        .then(response => {
          this.podcast = response.data;
        })
        .catch(error => {
          console.error('Error fetching podcast details:', error);
        });
    },
    fetchPodcastIssues() {
      const apiUrl = this.$websiteURL + `/podcast/${this.id}/issues?ordering=${this.order === 'по убыванию' ? '-' : ''}n_issue`;

      axios.get(apiUrl)
        .then(response => {
          this.sortedIssues = response.data;
        })
        .catch(error => {
          console.error('Error fetching podcast issues:', error);
        });
    },
  },
};
</script>


<style scoped>
.section-title {
  font-size: 2em;
  text-align: left;
  margin: 10px;
  color: #3c3c3c;
}
</style>

