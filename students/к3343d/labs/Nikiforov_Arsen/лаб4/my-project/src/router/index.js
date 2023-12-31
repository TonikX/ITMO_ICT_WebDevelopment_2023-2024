import { createRouter, createWebHistory } from 'vue-router';
import RegistrationPage from '../components/RegistrationPage.vue';
import LoginPage from '../components/LoginPage.vue';
import UserProfile from '../components/UserProfile.vue';
import ClientsTable from '../components/ClientsTable.vue';
import EmployeesTable from '../components/EmployeesTable.vue';
import RoomStatistics from '../components/RoomStatistics.vue';
import ComplexRoomsTable from '../components/ComplexRoomsTable.vue';
import RoomsTable from '../components/RoomsTable.vue';
import RoomReviewsList from '../components/RoomReviewsList.vue';
import LeaveFeedback from '../components/LeaveFeedback.vue';
import AddReview from '../components/AddReview.vue';
const routes = [
  { path: '/registration', component: RegistrationPage },
  { path: '/login', component: LoginPage },
  { path: '/user-profile', component: UserProfile },
  { path: '/clients', component: ClientsTable },
  { path: '/employees', component: EmployeesTable },
  { path: '/room-statistics', component: RoomStatistics },
  { path: '/complex-rooms', component: ComplexRoomsTable },
  { path: '/rooms-table', component: RoomsTable },
  {
    path: '/room/:roomId/reviews',
    name: 'RoomReviewsList',
    component: RoomReviewsList,
    props: true
  },
  {
    path: '/room/:roomId/leave-feedback',
    name: 'LeaveFeedback',
    component: LeaveFeedback,
    props: true
  },

  {
    path: '/room/:roomId/add-review',
    name: 'AddReview',
    component: AddReview,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
