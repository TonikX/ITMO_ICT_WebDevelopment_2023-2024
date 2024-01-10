import {createRouter, createWebHistory} from 'vue-router';
import HomePage from '@/components/HomePage.vue';
import ClubsTable from "@/components/ClubsTable.vue";
import RoutesTable from "@/components/RoutesTable.vue";

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
    },
    {
        path: '/routes',
        name: 'Routes',
        component: RoutesTable
    }
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;
