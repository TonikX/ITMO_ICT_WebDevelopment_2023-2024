import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import axios from 'axios';
import App from './App.vue';
import Home from './views/HomePage.vue';
import Login from './views/LoginPage.vue';
import Register from './views/RegisterPage.vue';
import Profile from './views/ProfilePage.vue';
import Shop from './views/ShopPage.vue';
import Locations from './views/LocationsPage.vue';
import OtherZoos from './views/OtherZoosPage.vue';
import Animals from './views/AnimalsPage.vue';

const app = createApp(App);

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/profile', component: Profile },
    { path: '/shop', component: Shop },
    { path: '/locations', component: Locations },
    { path: '/other-zoos', component: OtherZoos}, 
    { path: '/animals', component: Animals},
  ],
});


app.use(router);

axios.defaults.baseURL = 'http://127.0.0.1:8000/';


app.mount('#app');
