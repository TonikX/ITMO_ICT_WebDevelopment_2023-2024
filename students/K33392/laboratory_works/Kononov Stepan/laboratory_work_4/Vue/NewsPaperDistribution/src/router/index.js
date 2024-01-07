import {createRouter, createWebHistory} from 'vue-router'
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import NewspapersList from "@/views/NewspapersList.vue";
import PrintingHousesList from "@/views/PrintingHousesList.vue";
import PostOfficeList from "@/views/PostOfficeList.vue";
import PrintRuns from "@/views/PrintRuns.vue";
import PostArrivals from "@/views/PostArrivals.vue";
import Profile from "@/views/Profile.vue";


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: Login
        },
        {
            path: '/register',
            name: 'register',
            component: Register
        },
        {
            path: '/newspapers',
            name: 'newspapers',
            component: NewspapersList
        },
        {
            path: '/printing_house',
            name: 'printing_house',
            component: PrintingHousesList
        },
        {
            path: '/post_offices',
            name: 'post_offices',
            component: PostOfficeList
        },
        {
            path: '/print_runs',
            name: 'print_runs',
            component: PrintRuns
        },
        {
            path: '/post_arrivals',
            name: 'post_arrivals',
            component: PostArrivals
        },
        {
            path: '/profile',
            name: 'profile',
            component: Profile
        },
    ]
})

export default router
