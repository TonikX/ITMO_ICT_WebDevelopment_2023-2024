<template>
  <div class="guests-from-city">
    <h2>Guests From City</h2>
    <form @submit.prevent="getGuestsCount">
      <label for="city">City:</label>
      <input type="text" v-model="city" required />

      <button type="submit">Get Guests Count</button>
    </form>

    <div v-if="guestsCount !== null">
      <h3>Guests Count</h3>
      <p>Number of guests from {{ city }}: {{ guestsCount }}</p>
    </div>

    <div v-else>
      <p>No guests found for the specified city.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      city: '',
      guestsCount: null,
    };
  },
  methods: {
    async getGuestsCount() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/api/guests_from_city/${this.city}/`);
        this.guestsCount = response.data.guests_count;
      } catch (error) {
        console.error('Error getting guests count:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.guests-from-city {
  max-width: 400px;
  margin: 0 auto;
}
</style>
