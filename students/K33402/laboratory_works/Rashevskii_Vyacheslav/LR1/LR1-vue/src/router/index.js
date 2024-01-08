import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Login from '../components/Login'
import Disks from '../components/Disks'
import Games from '../components/Games'
import Sale from '../components/Sale'
import Admission from '../components/Admission'
import Sale_point from '../components/Sale_point'
import Admission_point from '../components/Admission_point'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login/',
      name: 'Login',
      component: Login
    },
    {
      path: '/disks/',
      name: 'Disks',
      component: Disks
    },
    {
      path: '/games/',
      name: 'Games',
      component: Games
    },
    {
      path: '/sale/',
      name: 'Sale',
      component: Sale
    },
    {
      path: '/admission/',
      name: 'Admission',
      component: Admission
    },
    {
      path: '/sale_point/',
      name: 'Sale_point',
      component: Sale_point
    },
    {
      path: '/admission_point/',
      name: 'Admission_point',
      component: Admission_point
    }
  ]
})
