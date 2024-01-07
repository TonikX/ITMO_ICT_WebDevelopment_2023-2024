import { createRouter, createWebHistory } from 'vue-router';
import EventHome from '@/views/EventHome.vue';
import EventDetail from '@/views/EventDetail.vue';
import UserRegistration from '@/views/UserRegistration.vue';
import UserLogin from '@/views/UserLogin.vue';
import UserPage from '@/views/UserPage.vue';

const routes = [
  {
    path: '/',
    name: 'EventHome',
    component: EventHome,
  },
  {
    path: '/events/:id',
    name: 'event-detail',
    component: EventDetail,
  },
  {
    path: '/registration',
    name: 'registration',
    component: UserRegistration,
  },
  {
    path: '/login',
    name: 'login',
    component: UserLogin,
  },
  {
    path: '/profile',
    name: 'UserPage',
    component: UserPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
