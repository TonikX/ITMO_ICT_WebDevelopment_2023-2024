<template>
  <v-container>
    <v-row class="mb-4">
      <v-col cols="12" md="4">
        <v-text-field v-model="search" label="Поиск" @input="fetchArticles" debounce="500"></v-text-field>
      </v-col>

      <v-col v-for="rubric in rubrics" :key="rubric.id" cols="auto">
        <v-btn @click="toggleAndFetch(rubric.id)" :outlined="!rubricFilters.includes(rubric.id)">
          {{ rubric.name }}
        </v-btn>
      </v-col>
    </v-row>

    <v-row>
      <v-col v-for="article in articles" :key="article.id" cols="12" md="6" lg="4">
        <v-card @click="openArticle(article.id)" class="mx-auto">
          <v-img :src="article.cover_picture" height="200"></v-img>
          <v-card-title>{{ article.name }}</v-card-title>
          <v-card-subtitle>{{ article.short_description }}</v-card-subtitle>
          <v-card-subtitle>{{ article.rubric }}</v-card-subtitle>
        </v-card>
      </v-col>
    </v-row>

    <v-row justify="center">
        <v-col cols="4">
          <v-container class="max-width">
            <v-pagination
              v-model="page"
              class="my-4"
              :length=totalPages
               @input="fetchArticles"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      articles: [],
      search: '',
      page: 1,
      totalPages: 1,
      rubrics: [],
      rubricFilters: [],
    };
  },
  mounted() {
    this.fetchRubrics();
    this.fetchArticles();
  },
  methods: {
    fetchArticles() {
      const params = {
        search: this.search,
        page: this.page,
      };

      if (this.rubricFilters.length > 0) {
        console.log(this.rubricFilters)
        params.rubric = this.rubricFilters.join('&rubric=');
        console.log(params.rubric)
      }

      const url_part = this.$websiteURL + '/article';
      const search_part = this.search ? '?&search=' + this.search : '?';
      const page_part = this.page ? '&page=' + this.page : '';
      let rubrics_part = '';
      if (this.rubricFilters && this.rubricFilters.length > 0) {
        rubrics_part = '&rubric=' + this.rubricFilters.join('&rubric=');
      }
      const url = url_part + search_part + page_part + rubrics_part;

      axios.get(url)
        .then(response => {
          this.articles = response.data.results;
          this.totalPages = Math.ceil(response.data.count / this.$totalPages);
        })
        .catch(error => {
          console.error('Error fetching articles:', error);
        });
    },
    openArticle(articleId) {
      this.$router.push({name: 'single-article', params: {id: articleId}});
    },
    fetchRubrics() {
      axios.get(this.$websiteURL + '/rubric')
        .then(response => {
          this.rubrics = response.data.results;
        })
        .catch(error => {
          console.error('Error fetching rubrics:', error);
        });
    },
    toggleRubricFilter(rubricId) {
      const index = this.rubricFilters.indexOf(rubricId);
      if (index === -1) {
        this.rubricFilters.push(rubricId);
      } else {
        this.rubricFilters.splice(index, 1);
      }
    },
    toggleAndFetch(rubricId) {
      this.toggleRubricFilter(rubricId);
      this.fetchArticles();
    },
  },
};
</script>

<style scoped>
</style>
