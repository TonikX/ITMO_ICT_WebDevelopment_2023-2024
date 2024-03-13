<template>
  <v-app>
    <NavbarComponent/>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import NavbarComponent from './components/NavbarComponent.vue'

export default {
  name: 'App',
  components: {
    NavbarComponent,
  }
}
</script>