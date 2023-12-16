<template>
  <v-card @click="navigateToSingleObject(contentObject.id)" class="mx-auto">
    <v-img :src="contentObject.cover_picture" height="200"></v-img>
    <v-card-title>{{ contentObject.name }}</v-card-title>
    <v-card-subtitle>{{ contentObject.short_description }}</v-card-subtitle>
    <v-btn icon @click="deleteItem">
      <v-icon color="red">mdi-delete</v-icon>
    </v-btn>
  </v-card>

</template>

<script>
import axios from 'axios';

export default {
  props: {
    user: Object,
    contentObject: Object,
    favouriteId: Number,
  },
  data() {
    return {
      noRedNeeded: false,
      showConfirmDialog: false,
    };
  },
  methods: {
    deleteItem() {
      const isConfirmed = window.confirm('Вы уверены, что хотите удалить объект из Избранного?');
      this.noRedNeeded = true;

      if (isConfirmed) {
        const apiUrl = this.$websiteURL + `/user/${this.user.id}/favourites/${this.favouriteId}`;
        const token = localStorage.getItem('token');
        const headers = {Authorization: `Token ${token}`};

        axios.delete(apiUrl, {headers}).then(() => {
          this.$emit('item-deleted');
          this.showConfirmDialog = false;
        });
      }
    },
    navigateToSingleObject(id) {
      if (!this.noRedNeeded) {
        this.$router.push({name: 'single-article', params: {id}});
      }
      this.noRedNeeded = false;
    },
  },
};
</script>

<style scoped>
</style>
