import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
//import router from './router'
import LoginPage from "./components/LoginPage.vue";
import {createRouter, createWebHistory} from "vue-router";
import axios from 'axios';
import RegisterPage from "@/components/RegisterPage.vue";
import IngredientsList from "@/components/IngredientsList.vue";
import HomePage from "@/components/HomePage.vue";
import RecipeList from "@/components/RecipeList.vue";

const app = createApp(App)

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: HomePage },
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage },
    { path: '/ingredients', component: IngredientsList },
    { path: '/recipes', component: RecipeList },
  ]
});

app.use(router)

app.mount('#app')
