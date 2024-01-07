<template>
  <div class="checkin">
    <h2>Check-in</h2>
    <form @submit.prevent="checkin">
      <label for="guestId">Guest ID:</label>
      <input type="number" v-model="guestId" required />

      <label for="roomNumber">Room Number:</label>
      <input type="number" v-model="roomNumber" required />

      <label for="checkinDate">Check-in Date:</label>
      <input type="date" v-model="checkinDate" required />

      <label for="checkoutDate">Checkout Date:</label>
      <input type="date" v-model="checkoutDate" required />

      <button type="submit">Check-in</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      guestId: null,
      roomNumber: null,
      checkinDate: '',
      checkoutDate: '',
    };
  },
  methods: {
    async checkin() {
      try {
        await this.$http.post('http://127.0.0.1:8000/api/checkin/', {
          guest_id: this.guestId,
          room_number: this.roomNumber,
          checkin_date: this.checkinDate,
          checkout_date: this.checkoutDate,
        });
        alert('Check-in completed successfully!');
      } catch (error) {
        console.error('Error during check-in:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.checkin {
  max-width: 400px;
  margin: 0 auto;
}
</style>
