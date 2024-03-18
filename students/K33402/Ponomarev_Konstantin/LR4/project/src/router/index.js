import {createRouter, createWebHistory} from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: () => import('@/views/LoginView')
    },
    {
      path: '/registration',
      name: 'Registration',
      component: () => import('@/views/RegistrationView')
    },
    {
      path: '/home',
      name: 'Home',
      component: () => import('@/views/HomeView.vue')
    },
    {
      path: '/books',
      name: 'BooksCatalog',
      component: () => import('@/views/BooksCatalogView')
    },
    {
      path: '/books/:id',
      name: 'BooksDetail',
      component: () => import('@/views/BookDetailsView')
    },
    {
      path: '/manager',
      name: 'Manager',
      component: () => import('@/views/ManagerInfoView')
    },
    {
      path: '/edit',
      name: 'EditProfile',
      component: () => import('@/views/EditProfileView')
    },
    {
      path: '/taken-books',
      name: 'TakenBooks',
      component: () => import('@/views/TakenBooksView.vue')
    }
  ]
})
router.beforeEach(async (to) => {
  if (!localStorage.auth_token &&
    to.name !== 'Login' &&
    to.name !== 'Registration'
  ) {
    console.log("redirect to auth")
    return {name: 'Login'}
  }
})

export default router

