<script>
import router from '@/router'
export default {
  name: 'service',
  props: ['service'],
  methods: {
    openService() {
      router.push({ path: `/services/${this.service.ID}/` })
    },
  },
}
</script>

<template>
  <li class="service" v-on:click="openService">
    <strong>{{ service.Name }}</strong>
  </li>
</template>

<style scoped>
.service {
  cursor: pointer;
}
</style>