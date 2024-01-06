### UserProfile
Компонент `UserProfile` представляет собой пользовательский интерфейс для системы управления отелем. Он отображает различные опции навигации для пользователя, включая просмотр комнат, клиентов, сотрудников и статистику по комнатам.

#### Шаблон (Template)
- Компонент включает кнопки для навигации по различным разделам системы.
- Предоставляет возможность оставить отзыв и просмотреть существующие отзывы.
- Динамически отображает компоненты в зависимости от выбранного действия пользователя.

#### Скрипт (Script)
- **Импорты**: Импортирует необходимые дочерние компоненты и сервисы.
- **Компоненты**: Включает `RoomsTable`, `ClientsTable`, `EmployeesTable`, `AddReview`, `RoomStatistics`, `ComplexRoomsTable`.
- **Data**: Содержит переменные для управления отображаемым компонентом и состояниями отзывов.
- **Методы**:
  - `showAddReviewForm`: Активирует форму добавления отзыва.
  - `showReviewList`: Отображает список отзывов.
  - `emitBack`: Функция для возврата к предыдущему виду.
  - `fetchReviews`: Получает список отзывов с сервера.
  - `updateReviews`: Обновляет список отзывов.
  - `showComplexRooms`, `showRoomStatistics`, `showRooms`, `showClients`, `showEmployees`: Методы для отображения соответствующих компонентов.

#### Стили (Styles)
- `.navigation-links`: Стилизация для навигационных ссылок.
- `button`: Определение стилей для кнопок, включая состояние при наведении.

#### Код компонента
```html
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
import RoomStatistics from './RoomStatistics.vue';
import ComplexRoomsTable from './ComplexRoomsTable.vue'

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
    AddReview,
    RoomStatistics,
    ComplexRoomsTable,
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
      this.$router.push('');
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
```
- Данный компонент используется для предоставления пользователю интерфейса управления различными аспектами отеля.

