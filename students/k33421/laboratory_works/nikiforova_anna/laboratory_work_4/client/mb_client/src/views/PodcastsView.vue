<template>
  <v-container>
    <NavbarComponent />
    <h2 class="section-title">Подкасты</h2>
    <PodcastsComponent />
  </v-container>
</template>

<script>
import NavbarComponent from "@/components/NavbarComponent.vue";
import PodcastsComponent from "@/components/PodcastsComponent.vue";

export default {
  name: "PodcastsView",
  components: {
    NavbarComponent,
    PodcastsComponent,
  },
}
</script>

<style scoped>
.section-title {
  font-size: 2em;
  text-align: left;
  margin: 30px 0;
  color: #3c3c3c;
}
</style>
