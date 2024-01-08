import Hello from "@/components/Hello.vue";
import Salons from "@/views/Salons.vue";
import OwnerRegistration from "@/views/OwnerRegistration.vue";
import Welcome from "@/components/Welcome.vue";

import SalonList from "@/components/SalonList.vue";

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/hi',
      name: 'hello_world',
      component: Hello
    },
    {
      path: '/salons',
      name: 'salon_list',
      component: Salons
    },
    {
      path: '/owner_sign_up',
      name: 'owner_sign_up',
      component: OwnerRegistration
    },
    {
      path: '/start',
      name: 'start',
      component: Welcome
    },

    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ]
})

export default router
