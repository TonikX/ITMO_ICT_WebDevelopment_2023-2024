<script setup>
const props = defineProps({
  card_title: String,
  card_button_title: String,
  bottom_msg: String,
  bottom_button_title: String,
  bottom_button_href: String,
})
</script>

<template>
  <body>
  <v-container style="alignment: center; margin-top: 10%">
    <div class="d-flex align-center flex-column">
    <v-card variant="text" width="400" height="80">
      <v-card-title style="text-align: center; font-size: 30px; color: #ffffff">
        ProductExchange
      </v-card-title>
    </v-card>

    <v-card width="400" color="lime">
      <v-card-title style="font-size: 20px; margin-top: 10px; margin-bottom: 15px; margin-left: 5px;">
        <b>{{ card_title }}</b>
      </v-card-title>
      <slot></slot>
    </v-card>
    <v-card variant="text" width="400" style="margin-top: 60px">
      <p style="margin-left: 0">{{ bottom_msg }}</p>
      <v-btn :to="bottom_button_href" variant="tonal" style="margin-top: 10px">
        {{ bottom_button_title }}
      </v-btn>
    </v-card>
    </div>
  </v-container>
  </body>
</template>

<style>
p {margin-left: 20px}
</style>