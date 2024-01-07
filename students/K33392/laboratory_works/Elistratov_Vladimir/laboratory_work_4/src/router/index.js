import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/vaulttec",
            name: "main",
            component: import("../views/TimeVault.vue"),
        },
        {
            path: "/test",
            name: "djangoTest",
            component: import("../views/test.vue")
        },
        {
            path: "/vaulttec/profile/:userId",
            name: "profile",
            component: () =>import("../views/TimeVaultProfile.vue"),
            props: true,
        },
    ],
});

// экспортируем сконфигурированный роутер
export default router;