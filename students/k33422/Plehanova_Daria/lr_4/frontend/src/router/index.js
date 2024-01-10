import {createRouter, createWebHistory} from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import ClubsTable from "@/components/ClubsTable.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomePage
    },
    {
        path: '/clubs',
        name: 'Clubs',
        component: ClubsTable
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;
