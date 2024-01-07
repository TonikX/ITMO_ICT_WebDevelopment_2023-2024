<template>
  <div class="checkout">
    <h2>Checkout</h2>
    <form @submit.prevent="checkout">
      <label for="checkinId">Check-in ID:</label>
      <input type="number" v-model="checkinId" required />

      <button type="submit">Checkout</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      checkinId: null,
    };
  },
  methods: {
    async checkout() {
      try {
        await this.$http.post('http://127.0.0.1:8000/api/checkout/', {
          checkin_id: this.checkinId,
        });
        alert('Checkout completed successfully!');
      } catch (error) {
        console.error('Error during checkout:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.checkout {
  max-width: 400px;
  margin: 0 auto;
}
</style>
