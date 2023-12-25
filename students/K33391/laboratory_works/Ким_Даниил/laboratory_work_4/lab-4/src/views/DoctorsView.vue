<script>
import api from '@/api'
import Doctor from '@/components/Doctor.vue'
import router from '@/router'
export default {
  data() {
    return { doctors: [] }
  },
  components: {
    Doctor,
  },
  methods: {
    getDoctors() {
      api
          .get('clinic/doctors/')
          .then((resp) => resp.data)
          .then((data) => (this.doctors = data))
          .catch(() => alert('Failed to fetch doctors'))
    },
    newDoctor() {
      router.push({ path: '/create-doctor' })
    },
  },
  beforeMount() {
    this.getDoctors()
  },
}
</script>

<template>
  <br />
  <button v-on:click="newDoctor">New doctor</button>
  <ol class="doctors">
    <Doctor v-for="doctor in doctors" :doctor="doctor" :key="doctor.id" />
  </ol>
</template>