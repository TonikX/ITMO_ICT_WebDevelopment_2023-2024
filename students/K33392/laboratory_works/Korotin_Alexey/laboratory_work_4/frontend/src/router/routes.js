const routes = [
    {
        path: "/facilities",
        component: () => import("@/layouts/MainLayout.vue"),
        children: [
            {
                path: "",
                component: () => import("@/pages/facilities/AllPage.vue"),
                meta: { requiresAuth: true },
            },
            {
                path: ":id",
                component: () => import("@/pages/facilities/FacilityPage.vue"),
                meta: { requiresAuth: true },
            },
        ],
    },
    {
        path: "/statistics",
        component: () => import("@/layouts/MainLayout.vue"),
        children: [
            {
                path: "",
                component: () => import("@/pages/statistics/StatisticsPage.vue"),
                meta: { requiresAuth: true },
            }
        ]
    },
    {
        path: "/auth",
        component: () => import("@/layouts/AuthLayout.vue"),
        children: [
            {
                name: "Login",
                path: "login",
                component: () => import("@/pages/auth/LoginPage.vue"),
                meta: { requiresAuth: false },
            },
            {
                name: "Register",
                path: "register",
                component: () => import("@/pages/auth/SignUpPage.vue"),
                meta: { requiresAuth: false },
            },
        ],
    },

    // Always leave this as last one,
    // but you can also remove it
    {
        path: "/:catchAll(.*)*",
        component: () => import("pages/ErrorNotFound.vue"),
    },
];

export default routes;
