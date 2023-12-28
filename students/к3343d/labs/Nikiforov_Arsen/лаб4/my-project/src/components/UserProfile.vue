<template>
  <div>
    <h2>Добро пожаловать в систему управления отелем, {{ username }}!</h2>
    <div class="navigation-links">
      <button @click="showRooms">Комнаты</button>
      <router-link to="/clients">Клиенты</router-link>
      <router-link to="/employees">Сотрудники</router-link>
      <button @click="emitBack">Назад</button>
    </div>
    <RoomsTable v-if="showRoomsTable" />
  </div>
</template>

<script>
import RoomsTable from './RoomsTable.vue';

export default {
  computed: {
    username() {
      return this.$store.state.user ? this.$store.state.user.username : 'Guest';
    }
  },
  components: {
    RoomsTable
  },
  data() {
    return {
      showRoomsTable: false
    };
  },
  methods: {
    showRooms() {
      this.showRoomsTable = true;
    },
    emitBack() {
      this.$emit('go-back');
    }
  }
};
</script>


<style scoped>
.navigation-links {
  text-align: center;
  margin-bottom: 20px;
}

.navigation-links a, .navigation-links button {
  margin: 0 10px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.navigation-links a:hover, .navigation-links button:hover {
  color: #007bff;
  text-decoration: underline;
}
</style>
