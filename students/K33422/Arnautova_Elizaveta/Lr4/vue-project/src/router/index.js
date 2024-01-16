import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import Climbers from '../views/Climbers.vue'
import Clubs from '../views/Clubs.vue'
import Club from '../views/Club.vue'

import Mountains from '../views/Mountains.vue'
import NoClimbers from '../components/NoClimbers.vue'
import NewMountain from '../components/NewMountain.vue'

import Ascensions from '../views/Ascensions.vue'
import Ascension from '../views/Ascension.vue'
import AscensionUpdate from '../components/AscensionUpdate.vue'

import Groups from '../views/Groups.vue'
import Group from "@/views/Group.vue";

import Login from '../components/Login.vue'
import UserPage from "../views/UserPage.vue"
import Registration from '../components/Registration.vue'
import GroupUpdate from "@/components/GroupUpdate.vue";



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/userpage/',
      name: 'UserPage',
      component: UserPage
    },
    {
      path: '/registration/',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/login/',
      name: 'Login',
      component: Login
    },

    {
      path: '/alp/climbers/',
      name: 'Climbers',
      component: Climbers
    },
    {
      path: '/alp/clubs/',
      name: 'Clubs',
      component: Clubs
    },
    {
      path: '/alp/clubs/:club_id/',
      name: 'Club',
      component: Club
    },

    {
      path: '/alp/mountains/',
      name: 'Mountains',
      component: Mountains
    },

    {
      path: '/alp/ascensions/',
      name: 'Ascensions',
      component: Ascensions
    },
    {
      path: '/alp/ascensions/:ascension_id/',
      name: 'Ascension',
      component: Ascension
    },
    {
      path: '/alp/ascensions/update/:ascension_id/',
      name: 'AscensionUpdate',
      component: AscensionUpdate
    },

    {
      path: '/alp/groups/',
      name: 'Groups',
      component: Groups
    },
      {
      path: '/alp/groups/:group_id/',
      name: 'Group',
      component: Group
    },
    {
      path: '/alp/groups/update/:group_id/',
      name: 'GroupUpdate',
      component: GroupUpdate
    },

    {
      path: '/mountains/noclimbers/',
      name: 'NoClimbers',
      component: NoClimbers
    },
    {
      path: '/alp/mountains/new',
      name: 'NewMountain',
      component: NewMountain
    },

  ]
})

export default router
