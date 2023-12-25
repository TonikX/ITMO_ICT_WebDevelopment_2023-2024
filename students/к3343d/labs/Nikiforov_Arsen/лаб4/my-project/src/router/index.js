import { createRouter, createWebHistory } from 'vue-router'; // Используйте createRouter и createWebHistory
import RegistrationPage from '../components/RegistrationPage.vue';
import LoginPage from '../components/LoginPage.vue';
import UserProfile from '../components/UserProfile.vue';

const routes = [
  { path: '/registration', component: RegistrationPage },
  { path: '/login', component: LoginPage },
  { path: '/user-profile', component: UserProfile },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
