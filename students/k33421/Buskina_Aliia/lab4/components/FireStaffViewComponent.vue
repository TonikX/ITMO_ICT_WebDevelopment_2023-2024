<template>
  <div class="fire-staff">
    <h2>Fire Staff</h2>
    <form @submit.prevent="fireStaff">
      <label for="staffId">Staff ID:</label>
      <input type="number" v-model="staffId" required />

      <button type="submit">Fire Staff</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      staffId: null,
    };
  },
  methods: {
    async fireStaff() {
      try {
        await this.$http.post('http://127.0.0.1:8000/api/fire_staff/', {
          staff_id: this.staffId,
        });
        alert('Staff fired successfully!');
      } catch (error) {
        console.error('Error firing staff:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.fire-staff {
  max-width: 400px;
  margin: 0 auto;
}
</style>
