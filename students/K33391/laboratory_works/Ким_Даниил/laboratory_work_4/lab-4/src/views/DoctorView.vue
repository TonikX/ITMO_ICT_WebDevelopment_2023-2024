<script>
import api from '@/api'
export default {
  data() {
    return { doctor: { id: this.$route.params.id, name: '', surname: '', specialization: '', contacts: '' } }
  },
  beforeMount() {
    api
        .get(`clinic/doctors/${this.doctor.id}/`)
        .then((resp) => resp.data)
        .then((data) => (this.doctor = data))
        .catch((_) => alert('Failed to fetch doctor'))
  },
}
</script>

<template>
  <strong>{{ doctor.Name }}</strong> - {{ doctor.Surname }} - {{ doctor.Specialization }} - {{ doctor.Contacts }}
</template>