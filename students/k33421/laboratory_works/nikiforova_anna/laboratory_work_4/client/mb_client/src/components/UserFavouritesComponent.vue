<template>
  <div>
    <v-container>

      <v-row v-if="favourites.length > 0">
        <v-col v-for="item in favourites" cols="12" md="6" lg="4">
          <ContentObjectComponent :key="item.id"
                                  :contentObject="item.content_object"
                                  :favouriteId="item.id"
                                  :user="user"
                                  @item-deleted="fetchData"></ContentObjectComponent>
        </v-col>
      </v-row>

      <v-row v-else>
        <v-col>
          <p class="description-text">Пока что здесь ничего нет...</p>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col cols="4">
          <v-container class="max-width">
            <v-pagination
              v-model="currentPage"
              class="my-4"
              :length=totalPages
              @input="fetchData"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>

    </v-container>
  </div>
</template>

<script>
import axios from 'axios';
import ContentObjectComponent from './ContentObjectComponent.vue';
import MenuComponent from "@/components/MenuComponent.vue";

export default {
  components: {
    MenuComponent,
    ContentObjectComponent,
  },
  data() {
    return {
      favourites: [],
      currentPage: 1,
      totalPages: 1,
      user: null,
    };
  },
  methods: {
    fetchUserData() {
      const token = localStorage.getItem('token');
      if (token) {
        const headers = {Authorization: `Token ${token}`};
        axios.get(this.$websiteURL + '/auth/users/me/', {headers})
          .then(response => {
            console.log(response)
            this.user = response.data;
            console.log('User data:', this.user);
            this.fetchData();
          })
          .catch(error => {
            console.error('Error fetching user data:', error);
          });
      } else {
        console.warn('No token found. User might not be authenticated.');
      }
    },
    fetchData() {
      const apiUrl = this.$websiteURL + `/user/${this.user.id}/favourites/?page=${this.currentPage}`;
      const token = localStorage.getItem('token');
      const headers = {Authorization: `Token ${token}`};

      axios.get(apiUrl, {headers}).then((response) => {
        this.totalPages = Math.ceil(response.data.count / this.$totalPages);
        this.favourites = response.data.results;
      });
    },
  },
  mounted() {
    this.fetchUserData();
    this.fetchData();
  },
};
</script>

<style scoped>
.description-text {
  font-size: 1em;
  color: #777;
}
</style>
