import { createRouter, createWebHistory } from 'vue-router';
import Auth from '@/views/Auth.vue';
import { useAuthStore } from '@/store';
import Unauth from '@/views/Unauth.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/auth', component: Auth, name: 'login' },
    {
      path: '/',
      component: () => import('@/layouts/default/Default.vue'),
      children: [
        { path: '', name: 'Home', component: () => import('@/views/Home.vue') },
        {
          path: 'student-cabinet',
          name: 'student-cabinet',
          component: () => import('@/views/StudentCabinet.vue'),
          meta: { requiresAuth: true, allowedRoles: ['student'] },
        },
        { path: '/unauth', component: Unauth, name: 'unauth' },
      ],
    },
  ],
});


router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();

  console.log('Before Each - Authenticated:', authStore.isAuthenticated);
  console.log('Before Each - Role:', authStore.role);

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    console.log('Redirecting to /auth');
    next('/auth');
  } else if (to.meta.allowedRoles && !to.meta.allowedRoles.includes(authStore.role)) {
    console.log('Redirecting to /unauth');
    next('/unauth');
  } else {
    console.log('Proceeding to the route');
    next();
  }
});



export default router;
