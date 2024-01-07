import {createRouter, createWebHistory} from 'vue-router'
import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import NewspapersList from "@/components/NewspapersList.vue";
import PrintingHousesList from "@/components/PrintingHousesList.vue";
import PostOfficeList from "@/components/PostOfficeList.vue";


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
    ]
})

export default router
