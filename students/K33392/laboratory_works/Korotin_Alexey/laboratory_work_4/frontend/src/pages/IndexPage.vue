<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >
    <q-btn @click="apiCall">Hello</q-btn>
  </q-page>
</template>

<script>
export default {
  data() {
    return ({

    });
  },

  methods: {
    apiCall() {
      this.$api.get('/report');
    }
  }
}
</script>
