<template>
  <div class="checkin-list">
    <h2>Check-in List</h2>
    <form @submit.prevent="getCheckinList">
      <label for="roomId">Room ID:</label>
      <input type="number" v-model="roomId" required min="1" />

      <label for="startDate">Start Date:</label>
      <input type="date" v-model="startDate" required />

      <label for="endDate">End Date:</label>
      <input type="date" v-model="endDate" required />

      <button type="submit">Get Check-in List</button>
    </form>

    <div v-if="checkinList.length > 0">
      <h3>Check-in List</h3>

      <ul>
        <li v-for="(checkin, index) in checkinList" :key="index">
          ID: {{ checkin.id }}, Check-in Date: {{ checkin.check_in_date }}, Check-out Date: {{ checkin.check_out_date }}, Guest ID: {{ checkin.guest_id }}
        </li>
      </ul>
    </div>

    <div v-else>
      <p>No check-ins found for the specified room and date range.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      roomId: null,
      startDate: '',
      endDate: '',
      checkinList: [],
    };
  },
  methods: {
    async getCheckinList() {
      try {
        const response = await this.$http.get(`http://127.0.0.1:8000/api/checkin_list/${this.roomId}/${this.startDate}/${this.endDate}/`);
        this.checkinList = response.data;
      } catch (error) {
        console.error('Error getting check-in list:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.checkin-list {
  max-width: 400px;
  margin: 0 auto;
}
</style>
