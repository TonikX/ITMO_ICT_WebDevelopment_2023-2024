<template>
  <div class="cleaning-form">
    <h2>Get Cleaning Info</h2>
    <form @submit.prevent="getCleaningInfo">
      <label for="guestId">Guest ID:</label>
      <input type="number" v-model="guestId" required min="1" />

      <label for="cleaningDate">Cleaning Date:</label>
      <input type="date" v-model="cleaningDate" required />

      <button type="submit">Get Cleaning Info</button>
    </form>

    <div v-if="cleanerInfo">
      <h3>Cleaning Info</h3>
      <p>Cleaner: {{ cleanerInfo.name }} {{ cleanerInfo.surname }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      guestId: null,
      cleaningDate: '',
      cleanerInfo: null,
    };
  },
  methods: {
    async getCleaningInfo() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/api/cleaner/for_guest/${this.guestId}/${this.cleaningDate}`);
        this.cleanerInfo = response.data.cleaner;
      } catch (error) {
        console.error('Error getting cleaning info:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.cleaning-form {
  max-width: 400px;
  margin: 0 auto;
}
</style>
