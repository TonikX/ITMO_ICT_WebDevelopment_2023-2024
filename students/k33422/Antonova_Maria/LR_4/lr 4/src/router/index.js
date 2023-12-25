import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/reg',
      name: 'Registration',
      component: () => import('@/views/RegistrationView.vue')
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/books',
      name: 'Books',
      component: () => import('@/views/BooksView.vue')
    },
    {
      path: '/books/:id',
      name: 'Book',
      component: () => import('@/views/BookView.vue')
    },
    {
      path: '/manager',
      name: 'Manager',
      component: () => import('@/views/ManagerInfoView.vue')
    },
    {
      path: '/edit',
      name: 'EditManager',
      component: () => import('@/views/EditProfileView.vue')
    },
    {
      path: '/taken-books',
      name: 'TakenBooks',
      component: () => import('@/views/TakenBooksView.vue')
    }
  ]
})

export default router

