<template>
  <v-menu offset-y>
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-on="on" v-bind="attrs">Меню</v-btn>
    </template>
    <v-list>
      <v-list-item @click="goToPage('/')">Главная страница</v-list-item>
      <v-list-item @click="goToPage('/podcasts')">Подкасты</v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  methods: {
    goToPage(route) {
      this.$router.push(route).catch(err => {
        if (err.name !== 'NavigationDuplicated') {
          throw err;
        }
      });
    },
  },
};
</script>

<style scoped>
</style>
