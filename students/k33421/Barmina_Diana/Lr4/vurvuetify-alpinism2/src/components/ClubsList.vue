
<template>
  <v-container>

    <v-row align="center" justify="center">
      <v-col
        v-for="club in clubs"
        :key="club"
        cols="4"
      >
        <v-card
          class="mx-auto"
          max-width="500px"
          color="teal-darken-4"
          variant='outlined'
        >
          <v-card-item>
            <div>

              <div class="text-h6 mb-1">
                {{ club.name }}
              </div>
              <div class="text-caption">{{ club.state }}, {{ club.city }}</div>
            </div>
          </v-card-item>

          <v-card-actions>
            <v-btn @click="$router.push(`/clubs/${club.id}`)" variant="tonal">
              подробнее
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import { ref } from 'vue'

export default {
  props: {
    clubs: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      color: ref('indigo')
    }
  }
}
</script>

<style scoped>

</style>
