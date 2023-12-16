<template>
  <v-container>
    <NavbarComponent/>
    <v-row class='mt-6'>
      <UserComponent :user="user"/>
    </v-row>
    <v-row class="ml-3">
      <h2 class="section-title">Избранное</h2>
    </v-row>
    <UserFavouritesComponent :user="user"/>
  </v-container>
</template>

<script>
import NavbarComponent from "@/components/NavbarComponent.vue";
import UserComponent from "@/components/UserComponent.vue";
import UserFavouritesComponent from "@/components/UserFavouritesComponent.vue";
import axios from "axios";

export default {
  name: "UserProfileView",
  components: {
    NavbarComponent,
    UserComponent,
    UserFavouritesComponent,
  },
  data() {
    return {
      user: null,
    };
  },
  mounted() {
    this.fetchUserData();
  },
  methods: {
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
  },
};
</script>

<style scoped>
.section-title {
  font-size: 2em;
  text-align: left;
  margin: 10px 0;
  color: #3c3c3c;
}
</style>
