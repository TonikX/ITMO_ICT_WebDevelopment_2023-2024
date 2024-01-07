<template>
  <div class="related-guests-list">
    <h2>Related Guests List</h2>
    <form @submit.prevent="getRelatedGuestsList">
      <label for="guestId">Guest ID:</label>
      <input type="number" v-model="guestId" required />

      <label for="startDate">Start Date:</label>
      <input type="date" v-model="startDate" required />

      <label for="endDate">End Date:</label>
      <input type="date" v-model="endDate" required />

      <button type="submit">Get Related Guests</button>
    </form>

    <div v-if="relatedGuestsList.length > 0">
      <h3>Related Guests</h3>
      <ul>
        <li v-for="(guestData, index) in relatedGuestsList" :key="index">
          <p>Date: {{ guestData.date }}</p>
          <ul>
            <li v-for="(guest, idx) in guestData.guests" :key="idx">
              Guest {{ guest.id }}: {{ guest.name }} {{ guest.surname }} from {{ guest.hometown }}
            </li>
          </ul>
        </li>
      </ul>
    </div>

    <div v-else>
      <p>No related guests found for the specified period.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      guestId: null,
      startDate: '',
      endDate: '',
      relatedGuestsList: [],
    };
  },
  methods: {
    async getRelatedGuestsList() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/api/related_guests/${this.guestId}/${this.startDate}/${this.endDate}/`);
        this.relatedGuestsList = response.data;
      } catch (error) {
        console.error('Error getting related guests list:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.related-guests-list {
  max-width: 600px;
  margin: 0 auto;
}
</style>
