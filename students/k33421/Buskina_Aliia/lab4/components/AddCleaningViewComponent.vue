<template>
  <div class="add-cleaning">
    <h2>Add Cleaning</h2>
    <form @submit.prevent="addCleaning">
      <label for="roomNumber">Room Number:</label>
      <input type="number" v-model="roomNumber" required />

      <label for="cleaningDate">Cleaning Date:</label>
      <input type="date" v-model="cleaningDate" required />

      <button type="submit">Add Cleaning</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      roomNumber: null,
      cleaningDate: '',
    };
  },
  methods: {
    async addCleaning() {
      try {
        await this.$http.post('http://127.0.0.1:8000/api/add_cleaning/', {
          room_number: this.roomNumber,
          cleaning_date: this.cleaningDate,
        });
        alert('Cleaning added successfully!');
      } catch (error) {
        console.error('Error adding cleaning:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.add-cleaning {
  max-width: 400px;
  margin: 0 auto;
}
</style>
