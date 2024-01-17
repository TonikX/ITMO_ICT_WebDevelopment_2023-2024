import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import axios from 'axios';
import App from './App.vue';
import Home from './views/HomePage.vue';
import Login from './views/LoginPage.vue';
import Register from './views/RegisterPage.vue';
import Profile from './views/ProfilePage.vue';
import Projects from './views/ProjectsPage.vue';
import ProjectsChoose from './views/ProjectsChoosePage.vue';

const app = createApp(App);

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/login', component: Login },
    { path: '/register', component: Register },
    { path: '/profile', component: Profile },
    { path: '/projects', component: Projects},
    { path: '/projects-choose', component: ProjectsChoose},
  ],
});


app.use(router);

axios.defaults.baseURL = 'http://127.0.0.1:8000/';


app.mount('#app');
