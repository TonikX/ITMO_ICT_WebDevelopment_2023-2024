import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/books/my',
      name: 'booksMy',
      component: () => import('../views/MyBooksView.vue')
    },
    {
      path: '/requests/from',
      name: 'requestsFrom',
      component: () => import('../views/RequestsFromView.vue')
    },
    {
      path: '/requests/to',
      name: 'requestsTo',
      component: () => import('../views/RequestsToView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    }
  ]
})

router.beforeEach((to, _, next) => {
  if (to.name !== 'login' && to.name !== 'register' && !localStorage.getItem('Token')) next({ name: 'login' })
  else next()
})

export default router
