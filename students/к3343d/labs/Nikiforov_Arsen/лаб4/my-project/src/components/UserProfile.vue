<template>
  <div>
    <h2>Добро пожаловать в систему управления отелем, {{ username }}!</h2>
    <div class="navigation-links">
      <button @click="showRooms">Комнаты</button>
      <button @click="showClients">Клиенты</button>
      <button @click="showEmployees">Сотрудники</button>
      <button @click="showRoomStatistics">Статистика комнат</button>
      <button @click="showComplexRooms">Комплексная информация о комнатах</button>
      <button @click="emitBack">Назад</button>
    </div>
    <component :is="currentComponent" v-if="showTable" />
  </div>
</template>

<script>
import RoomsTable from './RoomsTable.vue';
import ClientsTable from './ClientsTable.vue';
import EmployeesTable from './EmployeesTable.vue';

export default {
  computed: {
    username() {
      return this.$store.state.user ? this.$store.state.user.username : 'Guest';
    }
  },
  components: {
    RoomsTable,
    ClientsTable,
    EmployeesTable
  },
  data() {
    return {
      showTable: false,
      currentComponent: null
    };
  },
  methods: {
    showComplexRooms() { //сложный запрос
  this.currentComponent = 'ComplexRoomsTable';
  this.showTable = true;
},
    showRoomStatistics() {
    this.currentComponent = 'RoomStatistics';
    this.showTable = true;
    },
    showRooms() {
      this.currentComponent = 'RoomsTable';
      this.showTable = true;
    },
    showClients() {
      this.currentComponent = 'ClientsTable';
      this.showTable = true;
    },
    showEmployees() {
      this.currentComponent = 'EmployeesTable';
      this.showTable = true;
    },
    emitBack() {
      this.showTable = false;
    }
  }
};
</script>

<style scoped>
.navigation-links {
  text-align: center;
  margin-bottom: 20px;
}

.navigation-links button {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.navigation-links button:hover {
  color: #007bff;
  text-decoration: underline;
}
</style>
