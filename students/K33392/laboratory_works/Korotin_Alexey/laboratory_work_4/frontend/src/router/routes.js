import MainLayout from "@/layouts/MainLayout.vue";
import AuthLayout from "@/layouts/AuthLayout.vue";

const routes = [
    {
        path: "/facilities",
        component: MainLayout,
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
        path: "/cages",
        component: MainLayout,
        children: [
            {
                path: "",
                component: () => import("@/pages/cages/AllPage.vue"),
                meta: { requiresAuth: true },
            },
            {
                path: ":id",
                component: () => import("@/pages/cages/CagePage.vue"),
                meta: { requiresAuth: true },
            },
        ],
    },
    {
        path: "/chicken",
        component: MainLayout,
        children: [
            {
                path: "",
                component: () => import("@/pages/chicken/AllPage.vue"),
                meta: { requiresAuth: true },
            },
            {
                path: ":id",
                component: () => import("@/pages/chicken/ChickenPage.vue"),
                meta: { requiresAuth: true },
            },
        ],
    },
    {
        path: "/staff",
        component: MainLayout,
        children: [
            {
                path: "",
                component: () => import("@/pages/staff/AllPage.vue"),
                meta: { requiresAuth: true },
            },
            {
                path: ":username",
                component: () => import("@/pages/staff/StaffPage.vue"),
                meta: { requiresAuth: true },
            },
        ],
    },
    {
        path: "/statistics",
        component: MainLayout,
        children: [
            {
                path: "",
                component: () => import("@/pages/statistics/StatisticsPage.vue"),
                meta: { requiresAuth: true },
            },
        ],
    },
    {
        path: "/auth",
        component: AuthLayout,
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
