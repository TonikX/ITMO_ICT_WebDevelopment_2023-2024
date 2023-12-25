import { createRouter, createWebHistory } from "vue-router";
import Warriors from "@/views/Warriors.vue";

const routes = [
  {
    path: "/",
    redirect: "/warriors"
  },
  {
    path: "/warriors",
    name: "Warriors",
    component: Warriors
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
