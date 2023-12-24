import Hello from "@/components/Hello.vue";
import Warriors from "@/views/Warriors.vue";
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import GroupList from "@/components/GroupList.vue";
import Group from "@/components/Group.vue";
import TutorList from "@/components/TutorList.vue";
import {createRouter, createWebHistory} from "vue-router";

const routes = [  // массив с роутами
   // отдельный роут:   
   {
      path: '/hi', // конкретный url-адрес
      component: Hello // Ссылка на компонент
   },
   {
      path: '/warriors',
      component: Warriors
   },
   {
      path: '/login',
      component: Login
   },
      {
      path: '/register',
      component: Register
   },
   {
      path: '/group/',
      component: GroupList
   },
   {
      path: '/group/:groupid?',
      component: Group
   },
   {
      path: '/tutor/',
      component: TutorList
   }
]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router // экспортируем сконфигурированный роутер