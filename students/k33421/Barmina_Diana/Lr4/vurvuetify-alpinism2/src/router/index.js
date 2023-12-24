//import Vue from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import Mountains from '../components/Mountains.vue'
import Login from '../components/Login.vue'
import Registration from '../components/Registration.vue'
import Clubs from "../views/Clubs.vue"
import Club from "../views/Club.vue"
import UserPage from "../views/UserPage.vue"
import ClimbingsList from "../views/ClimbingsList.vue";
import Climbing from "../views/Climbing.vue";


//Vue.use(Router)

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/mountains/',
      name: 'Mountains',
      component: Mountains
    },
    {
      path: '/login/',
      name: 'Login',
      component: Login
    },
    {
      path: '/registration/',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/clubs/',
      name: 'Clubs',
      component: Clubs
    },
    {
      path: '/clubs/:club_id/',
      name: 'Club',
      component: Club
    },
    {
      path: '/userpage/',
      name: 'UserPage',
      component: UserPage
    },
    {
      path: '/climbings/',
      name: 'ClimbingsList',
      component: ClimbingsList
    },
    {
      path: '/climbings/:climbing_id/',
      name: 'Climbing',
      component: Climbing
    },

  ]
})

export default router;

