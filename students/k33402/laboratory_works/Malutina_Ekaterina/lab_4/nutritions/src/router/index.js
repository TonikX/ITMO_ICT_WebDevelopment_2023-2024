import HomePage from '../components/HomePage.vue';
import LoginPage from '../components/LoginPage.vue';
import RegisterPage from '../components/RegisterPage.vue';
import UserProfile from '../components/UserProfile.vue';
import {createRouter, createWebHistory} from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/login',
    component: LoginPage
  },
  {
    path: '/register',
    component: RegisterPage
  },
  {
    path: '/profile',
    component: UserProfile
  },
  {
    path: '/ingredients',
    component: () => import("@/components/IngredientsList.vue")
  },
  {
    path: '/recipes',
    component: () => import("@/components/RecipeList.vue")
  }
];

const router  = createRouter({
  history: createWebHistory(''),
  routes
});

export default router;
