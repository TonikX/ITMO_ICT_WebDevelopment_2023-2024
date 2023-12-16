<template>
  <v-container>
    <v-col v-for="issue in issues" :key="issue.id" cols="12">
      <v-card>
        <div class="d-flex flex-no-wrap justify-space-between align-center">
          <div>
            <v-card-title class="text-h5">{{ issue.name }}</v-card-title>
            <v-card-subtitle>Номер выпуска: {{ issue.n_issue }}<br>
              Дата выхода: {{ $formatDate(issue.release_date) }}</v-card-subtitle>
            <v-card-text>{{ issue.short_description }}</v-card-text>
            <audio controls class="ml-3">
              <source :src="issue.audio_file" type="audio/mpeg">
              Your browser does not support the audio tag.
            </audio>
          </div>
          <v-avatar class="ma-3" size="150" rounded="1">
            <v-img :src="issue.cover_picture"></v-img>
          </v-avatar>
        </div>
      </v-card>
    </v-col>
  </v-container>
</template>

<script>
export default {
  props: {
    podcastId: Number,
    issues: Object,
  },
};
</script>
