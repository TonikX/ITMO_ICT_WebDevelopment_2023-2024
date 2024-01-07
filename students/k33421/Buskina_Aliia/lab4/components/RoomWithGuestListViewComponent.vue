<template>
  <div class="room-with-guest-list">
    <h2>Room With Guest List</h2>
    <ul>
      <li v-for="(roomData, index) in roomWithGuestList" :key="index">
        Room {{ roomData.room_id }}: Guest {{ roomData.guest_id }} ({{ roomData.guest_name }} {{ roomData.guest_surname }})
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      roomWithGuestList: [],
    };
  },
  created() {
    this.getRoomWithGuestList();
  },
  methods: {
    async getRoomWithGuestList() {
      try {
        const response = await this.$http.get('http://127.0.0.1:8000/api/room_with_guest_list/');
        this.roomWithGuestList = response.data;
      } catch (error) {
        console.error('Error getting room with guest list:', error.message || error);
      }
    },
  },
};
</script>

<style scoped>
.room-with-guest-list {
  max-width: 600px;
  margin: 0 auto;
}
</style>
