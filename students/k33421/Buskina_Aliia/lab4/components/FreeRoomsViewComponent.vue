<template>
  <div class="free-rooms">
    <h2>Free Rooms</h2>
    <form @submit.prevent="getFreeRoomsCount">
      <label for="date">Date:</label>
      <input type="date" v-model="date" required />

      <button type="submit">Get Free Rooms Count</button>
    </form>

    <div v-if="freeRoomsCount !== null">
      <h3>Free Rooms Count</h3>
      <p>Number of free rooms on {{ date }}: {{ freeRoomsCount }}</p>
    </div>

    <div v-else>
      <p>No information available for the specified date.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      date: '',
      freeRoomsCount: null,
    };
  },
  methods: {
    async getFreeRoomsCount() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/api/free_rooms/${this.date}/`);
        this.freeRoomsCount = response.data[0].free_rooms_count;
      } catch (error) {
        console.error('Error getting free rooms count:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.free-rooms {
  max-width: 400px;
  margin: 0 auto;
}
</style>
