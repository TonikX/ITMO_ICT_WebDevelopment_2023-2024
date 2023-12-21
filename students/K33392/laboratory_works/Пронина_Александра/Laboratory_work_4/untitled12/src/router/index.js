// Роутер
import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/HomePage.vue';
import LogIn from '@/components/LogIn.vue';
import Catalog from '@/views/CatalogPage.vue';
import CartPage from '@/views/CartPage.vue';
import ReviewPage from '@/views/ReviewPage.vue';
import FavoritesPage from '@/views/FavoritesPage.vue';
import BookList from '@/components/BookList.vue';
import ReGister from "@/components/ReGister";

const routes = [
    { path: '/auth/token/login/', name: 'LogIn', component: LogIn },
    { path: '/register', name: 'ReGister', component: ReGister },
    { path: '/', name: 'HomePage', component: Home },
    { path: '/catalog', name: 'CatalogPage', component: Catalog },
    { path: '/cart', name: 'CartPage', component: CartPage },
    { path: '/reviews', name: 'ReviewPage', component: ReviewPage },
    { path: '/favorites', name: 'FavoritesPage', component: FavoritesPage },
    { path: '/books', name: 'BookList', component: BookList },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
