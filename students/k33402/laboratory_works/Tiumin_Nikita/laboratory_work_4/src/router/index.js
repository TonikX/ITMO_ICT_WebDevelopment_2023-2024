import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes.js'
import useAuthStore from "../pinia/auth";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
})

router.beforeEach(async (to, from) => {
  let user
  let authStore = useAuthStore()

  user = await authStore.getUser()

  if(to.meta.requiresAuth && !user) {
    return {
      name: 'login'
    }
  }
  if(to.meta.blockedForAuthenticated && user) {
    return {
      name: 'home'
    }
  }
})

export default router
