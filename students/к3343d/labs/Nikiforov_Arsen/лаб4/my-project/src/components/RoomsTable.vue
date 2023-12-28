<template> 
  <div>
    <h2>Список комнат</h2>
    <label for="room_type">Room Type:</label>
    <select v-model="filterType">
      <option value="">--Select a Type--</option>
      <option value="single">Single</option>
      <option value="double">Double</option>
      <option value="suite">Suite</option>
    </select>

    <label for="room_status">Room Status:</label>
    <select v-model="filterStatus">
      <option value="">--Select a Status--</option>
      <option value="available">Available</option>
      <option value="occupied">Occupied</option>
      <option value="cleaning">Cleaning</option>
    </select>

    

    <table>
      <thead>
        <tr>
          <th>Room Type</th>
          <th>Floor Number</th>
          <th>Status</th>
          <th>Cost</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="room in filteredRooms" :key="room.id">
          <td>{{ room.room_type }}</td>
          <td>{{ room.floor.number }}</td>
          <td>{{ room.status }}</td>
          <td>{{ room.cost }}</td>
          <td>
            <button v-if="room.status === 'available'" @click="bookRoom(room.id)">
              Book
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      rooms: [],
      filterType: '',
      filterStatus: ''
    };
  },
  computed: {
    filteredRooms() {
      return this.rooms.filter(room => {
        return (!this.filterType || room.room_type === this.filterType) &&
               (!this.filterStatus || room.status === this.filterStatus);
      });
    }
  },
  created() {
    this.fetchRooms();
  },
  methods: {
    fetchRooms() {
      axios.get('/hotel_api/api/rooms/')
        .then(response => {
          this.rooms = response.data;
        })
        .catch(error => {
          console.error('Error loading rooms:', error);
        });
    },
    applyFilter() {
      this.fetchRooms();
    },
    bookRoom(roomId) {
      axios.post(`/hotel_api/api/book_room/${roomId}`)
        .then(() => {
          this.fetchRooms(); // обновить после брони
        })
        .catch(error => {
          console.error('Error booking room:', error);
        });
    }
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

td {
  background-color: #fff;
}

tr:hover {
  background-color: #f5f5f5;
}
</style>
