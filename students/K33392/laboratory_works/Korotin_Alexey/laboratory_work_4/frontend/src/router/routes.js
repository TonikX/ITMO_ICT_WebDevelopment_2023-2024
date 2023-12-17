const routes = [
    {
        path: "/",
        component: () => import("layouts/MainLayout.vue"),
        children: [
            {
                path: "",
                component: () => import("pages/IndexPage.vue"),
                meta: { requiresAuth: true },
            },
        ],
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
