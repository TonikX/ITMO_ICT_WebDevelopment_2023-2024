<template>
  <v-container>
    <NavbarComponent/>

    <v-row>
      <v-col cols="12">

        <v-btn v-if="user" @click="addToFavorites" class="mt-8 mb-4">Добавить в избранное</v-btn>

        <v-card>
          <v-img :src="article.cover_picture" alt="Article Cover" class="mx-auto my-4" max-height="400"></v-img>
          <v-card-title>{{ article.name }}</v-card-title>

          <v-divider></v-divider>

          <v-card-text v-html="article.content"></v-card-text>
          <v-divider></v-divider>

          <v-row>
            <v-col cols="6">
              <v-card-subtitle>Рубрика: {{ article.rubric }}<br>
              Дата выхода: {{ $formatDate(article.release_date) || 'неизвестно' }}</v-card-subtitle>
            </v-col>
          </v-row>
        </v-card>

      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import NavbarComponent from "@/components/NavbarComponent.vue";
import axios from 'axios';

export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  components: {
    NavbarComponent,
  },
  data() {
    return {
      article: {},
      user: null,
    };
  },
  mounted() {
    this.fetchArticle(this.id);
    this.fetchUserData();
  },
  methods: {
    fetchArticle(articleId) {
      axios.get(this.$websiteURL + `/article/${articleId}`)
        .then(response => {
          this.article = response.data;
        })
        .catch(error => {
          console.error('Error fetching article details:', error);
        });
    },
    fetchUserData() {
      const token = localStorage.getItem('token');
      if (token) {
        const headers = {Authorization: `Token ${token}`};
        axios.get(this.$websiteURL + '/auth/users/me/', {headers})
          .then(response => {
            this.user = response.data;
          })
          .catch(error => {
            console.error('Error fetching user data:', error);
          });
      } else {
        console.warn('No token found. User might not be authenticated.');
      }
    },
    addToFavorites() {
      const token = localStorage.getItem('token');
      if (token) {
        const headers = {Authorization: `Token ${token}`};
        const data = {content_object: this.article.id};
        axios.post(this.$websiteURL + `/user/${this.user.id}/favourites/create/`, data, {headers})
          .then(response => {
            alert('Статья добавлена в Избранное!');
            console.log('Article added to favorites:', response.data);
          })
          .catch(error => {
            alert('Статья уже есть в Избранном!');
            console.error('Error adding article to favorites:', error);
          });
      } else {
        console.warn('No token found. User might not be authenticated.');
      }
    },
  },
};
</script>

<style scoped>

</style>
