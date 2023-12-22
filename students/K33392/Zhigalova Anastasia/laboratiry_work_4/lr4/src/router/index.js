import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EnterPatientView from '../views/EnterPatientView.vue'
import RegisterPatientView from '../views/RegisterPatientView.vue'
import EnterDoctortView from '../views/EnterDoctorView.vue'
import RegisterDoctorView from '../views/RegisterDoctorView.vue'
import ProfilePatientView from '../views/ProfilePatientView.vue'
import MainView from '../views/MainView.vue'
import DoctorListView from '../views/DoctorListView.vue'
import MyProfileView from '../views/MyProfileView.vue'
import MyAppointmentsView from '../views/MyAppointmentsView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/enterpatient',
      name: 'enterpatient',
      component: EnterPatientView
    },
    {
      path: '/registerpatient',
      name: 'registerpatient',
      component: RegisterPatientView
    },
    {
      path: '/enterdoctor',
      name: 'enterdoctor',
      component: EnterDoctortView
    },
    {
      path: '/registerdoctor',
      name: 'registerdoctor',
      component: RegisterDoctorView
    },
    {
      path: '/profilepatient',
      name: 'profilepatient',
      component: ProfilePatientView
    },
    {
      path: '/main',
      name: 'main',
      component: MainView
    },
    {
      path: '/doctorslist',
      name: 'doctorslist',
      component: DoctorListView
    },
    {
      path: '/myprofile',
      name: 'myprofile',
      component: MyProfileView
    },
    {
      path: '/appointments',
      name: 'appointments',
      component: MyAppointmentsView
    },
  ]
})

export default router
