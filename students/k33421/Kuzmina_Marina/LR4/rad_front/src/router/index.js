import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import Profile from '../components/Profile.vue'
import BookDetail from '../components/BookDetail.vue';

Vue.use(VueRouter)

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/profile', component: Profile },
  { path: '/books/:id', component: BookDetail, name: 'book-detail' },
]

const router = new VueRouter({
  routes
})

export default router


