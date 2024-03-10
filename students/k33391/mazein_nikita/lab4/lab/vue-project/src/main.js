import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import App from './App.vue';
import Login from './components/Login.vue';
import Register from './components/Register.vue';
import Profile from './components/Profile.vue';
import Home from './views/Home.vue';
import Brokers from './views/Brokers.vue';
import Producers from './views/Producers.vue';
import Products from './views/Products.vue';
import Cosignments from './views/Cosignments.vue'

axios.defaults.baseURL = 'http://127.0.0.1:8000/';

const app = createApp(App);
app.config.globalProperties.isAuthenticated = false;

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/profile', component: Profile, meta: { requiresAuth: true } },
    { path: '/', component: Home },
    { path: '/brokers', component: Brokers, meta: { requiresAuth: true } },
    { path: '/producers', component: Producers, meta: { requiresAuth: true } },
    { path: '/products', component: Products, meta: { requiresAuth: true } },
    { path: '/cosignments', component: Cosignments, meta: { requiresAuth: true } },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!localStorage.getItem('access_token')) {
      next({
        path: '/login',
        query: { redirect: to.fullPath },
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

app.use(router);

app.mount('#app');