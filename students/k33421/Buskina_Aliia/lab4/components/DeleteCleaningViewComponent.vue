<template>
  <div class="delete-cleaning">
    <h2>Delete Cleaning</h2>
    <form @submit.prevent="deleteCleaning">
      <label for="cleaningId">Cleaning ID:</label>
      <input type="number" v-model="cleaningId" required />

      <button type="submit">Delete Cleaning</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cleaningId: null,
    };
  },
  methods: {
    async deleteCleaning() {
      try {
        await this.$http.post('http://127.0.0.1:8000/api/delete_cleaning/', {
          cleaning_id: this.cleaningId,
        });
        alert('Cleaning deleted successfully!');
      } catch (error) {
        console.error('Error deleting cleaning:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.delete-cleaning {
  max-width: 400px;
  margin: 0 auto;
}
</style>
