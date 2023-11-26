<script setup>
const props = defineProps({
  place: String,
})
</script>


<template>
<v-app-bar :elevation="0" color="lime">
  <v-app-bar-title style="margin-left: 50px">ProductExchange</v-app-bar-title>
  <template v-slot:append>
      <v-btn icon="mdi-account" style="margin-right: 20px" to="/account" v-if="place == 'main'">
      </v-btn>
      <v-btn icon="mdi-home" style="margin-right: 20px" to="/" v-if="place == 'account'">
      </v-btn>
  </template>
</v-app-bar>
</template>

