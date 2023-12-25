<script>
import api from '@/api'
import Service from '@/components/Service.vue'
import router from '@/router'
export default {
  data() {
    return { services: [] }
  },
  components: {
    Service,
  },
  methods: {
    getServices() {
      api
          .get('clinic/services/')
          .then((resp) => resp.data)
          .then((data) => (this.services = data))
          .catch(() => alert('Failed to fetch services'))
    },
    newService() {
      router.push({ path: '/create-service' })
    },
  },
  beforeMount() {
    this.getServices()
  },
}
</script>

<template>
  <br />
  <button v-on:click="newService">New service</button>
  <ol class="services">
    <Service v-for="service in services" :service="service" :key="service.id" />
  </ol>
</template>