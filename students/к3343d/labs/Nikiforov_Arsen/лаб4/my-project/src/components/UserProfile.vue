
































<template>
  <div>
    <h2>Добро пожаловать в систему управления отелем, {{ username }}!</h2>
    <div class="navigation-links">
      <button @click="showRooms">Комнаты</button>
      <button @click="showClients">Клиенты</button>
      <button @click="showEmployees">Сотрудники</button>
      <button @click="showRoomStatistics">Статистика комнат</button>
      <button @click="showComplexRooms">Комплексная информация о комнатах</button>
      <button @click="showAddReviewForm">Оставить отзыв</button>
      <button @click="showReviewList">Показать отзывы</button>
      <button @click="emitBack">Назад</button>
    </div>

    <component :is="currentComponent" v-if="showTable" />

    <div v-if="showReviewForm">
      <AddReview :roomId="selectedRoomId" @review-added="updateReviews" />
    </div>

    <div v-if="showReviews">
      <h3>Отзывы</h3>
      <ul>
        <li v-for="review in reviews" :key="review.id">
          {{ review.text }} - {{ review.author }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import RoomsTable from './RoomsTable.vue';
import ClientsTable from './ClientsTable.vue';
import EmployeesTable from './EmployeesTable.vue';
import AddReview from './AddReview.vue';
import ReviewService from '@/reviewService'; // Путь к файлу ReviewService

export default {
  computed: {
    username() {
      return this.$store.state.user ? this.$store.state.user.username : 'Guest';
    }
  },
  components: {
    RoomsTable,
    ClientsTable,
    EmployeesTable,
    AddReview
  },
  data() {
    return {
      showTable: false,
      currentComponent: null,
      showReviewForm: false,
      showReviews: false,
      reviews: [],
      selectedRoomId: null
    };
  },
  methods: {
    showAddReviewForm(roomId) {
      this.selectedRoomId = roomId;
      this.showReviewForm = true;
      this.showReviews = false;
    },
    showReviewList() {
      this.showReviewForm = false;
      this.showReviews = true;
      this.fetchReviews();
    },
    emitBack() {
      this.showTable = false;
      this.showReviewForm = false;
      this.showReviews = false;
    },
    fetchReviews() {
      ReviewService.getAllReviews()
        .then(response => {
          this.reviews = response.data;
        })
        .catch(error => {
          console.error('Ошибка при получении отзывов:', error);
        });
    },
    updateReviews() {
      this.fetchReviews();
      this.showReviewForm = false;
      this.showReviews = true;
    },
    goToLeaveFeedback() {
      this.$router.push('/add-review');
    },
    leaveFeedback() {
      this.$router.push('/path-to-feedback-form');
    },
    showComplexRooms() {
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
  },
  created() {
    this.fetchReviews();
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
