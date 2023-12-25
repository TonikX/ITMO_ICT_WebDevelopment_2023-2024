<script>
import router from '@/router'
export default {
  name: 'doctor',
  props: ['doctor'],
  methods: {
    openDoctor() {
      router.push({ path: `/doctors/${this.doctor.ID}/` })
    },
  },
}
</script>

<template>
  <li class="doctor" v-on:click="openDoctor">
    <strong>{{ doctor.Name }} {{ doctor.Surname }}</strong>
  </li>
</template>

<style scoped>
.doctor {
  cursor: pointer;
}
</style>