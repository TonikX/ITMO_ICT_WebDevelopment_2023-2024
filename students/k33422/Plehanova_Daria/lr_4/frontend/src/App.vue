<template>
  <v-app>
    <SiteNavbar/>
    <v-main>
      <router-view></router-view>
    </v-main>
    <SiteFooter/>
  </v-app>
</template>

<script>
import SiteNavbar from './components/SiteNavbar.vue'
import SiteFooter from './components/SiteFooter.vue'

export default {
  name: 'App',
  components: {
    SiteNavbar,
    SiteFooter,
  }
}
</script>
