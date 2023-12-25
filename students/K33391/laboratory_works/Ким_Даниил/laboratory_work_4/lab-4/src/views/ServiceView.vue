<script>
import api from '@/api'
export default {
  data() {
    return { service: { id: this.$route.params.id, title: '', description: '', price: '' } }
  },
  beforeMount() {
    api
        .get(`clinic/services/${this.service.id}/`)
        .then((resp) => resp.data)
        .then((data) => (this.service = data))
        .catch((_) => alert('Failed to fetch service'))
  },
}
</script>

<template>
  <v-card>
    <v-card-title>
      <strong>{{ service.Name }}</strong>
    </v-card-title>
    <v-card-subtitle>{{ service.Description }}</v-card-subtitle>
    <v-card-text>
      Price: {{ service.Price }}
    </v-card-text>
  </v-card>
</template>
