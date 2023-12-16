import Vue from 'vue';
import VueRouter from 'vue-router';
import MainPageView from '@/views/MainPageView.vue';
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import UserProfileView from "@/views/UserProfileView.vue";
import SingleArticleView from "@/views/SingleArticleView.vue";
import PodcastsView from "@/views/PodcastsView.vue";
import SinglePodcastView from "@/views/SinglePodcastView.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'MainPageView',
    component: MainPageView,
  },
  {
    path: '/podcasts',
    name: 'PodcastsView',
    component: PodcastsView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserProfileView,
    meta: {requiresAuth: true},
  },
  {
    path: '/article/:id',
    name: 'single-article',
    component: SingleArticleView,
    props: true,
  },
  {
    path: '/podcast/:id',
    name: 'single-podcast',
    component: SinglePodcastView,
    props: true,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(route => route.meta.requiresAuth)) {
    const isAuthenticated = !!localStorage.getItem('token');

    if (!isAuthenticated) {
      next({name: 'login'});
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
