import { createRouter, createWebHistory } from 'vue-router'
import Hello from '../components/Hello.vue'
import Warriors from '../views/Warriors.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/hi',
      name: 'home',
      component: Hello
    },
    {
   path: '/warriors',
   component: Warriors
    },
      /*
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
       */
  ]
})

export default router
