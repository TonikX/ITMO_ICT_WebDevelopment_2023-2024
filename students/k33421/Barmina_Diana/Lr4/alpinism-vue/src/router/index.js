import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Mountains from '@/components/Mountains'
import Login from '@/components/Login'
import Registration from '@/components/Registration'
import Clubs from "@/views/Clubs"
import Club from "@/views/Club"
import UserPage from "@/views/UserPage"
import ClimbingsList from "../views/ClimbingsList.vue";
import Climbing from "../views/Climbing.vue";
import MountainsFilters from "../components/MountainsFilters.vue";

Vue.use(Router)

export default new Router({
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
    {
      path: '/mountains/filter/',
      name: 'MountainsFilters',
      component: MountainsFilters
    }

  ]
})
