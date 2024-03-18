<template>
  <v-spacer></v-spacer>
  <v-btn v-if="!auth" @click="routeToLogin()" text>
    <span class="mr-2">Вход</span>
  </v-btn>

</template>

<script>
export default {
  name: 'RegistrationBar',
  methods: {
    routeToLogin() {
      this.$router.push({name: 'Login'})
    },
  }
}
</script>
