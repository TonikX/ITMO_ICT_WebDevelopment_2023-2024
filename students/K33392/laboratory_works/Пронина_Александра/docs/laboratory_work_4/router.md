    import { createRouter, createWebHistory } from 'vue-router'
    
    import store from '../store'
    
    import Home from '../views/Home.vue'
    
    import Product from '../views/Product.vue'
    import Category from '../views/Category.vue'
    import Search from '../views/Search.vue'
    import Cart from '../views/Cart.vue'
    import SignUp from '../views/SignUp.vue'
    import LogIn from '../views/LogIn.vue'
    import MyAccount from '../views/MyAccount.vue'
    import Checkout from '../views/Checkout.vue'
    import Success from '../views/Success.vue'
    
    // Определение маршрутов
    const routes = [
      {
        path: '/',
        name: 'Home',
        component: Home
      },
      {
        path: '/about',
        name: 'About',
        // Код разделения уровня маршрута
        // Это генерирует отдельный фрагмент кода (about.[hash].js), который загружается по требованию при посещении маршрута.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
      },
      // ... (для других маршрутов)
    ]
    
    // Создание экземпляра маршрутизатора
    const router = createRouter({
      history: createWebHistory(process.env.BASE_URL),
      routes
    })
    
    // Глобальный хук (beforeEach), выполняемый перед каждой навигацией
    router.beforeEach((to, from, next) => {
      // Проверка, требуется ли аутентификация для данного маршрута
      if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        // Если требуется аутентификация и пользователь не аутентифицирован, перенаправление на страницу входа с сохранением пути
        next({ name: 'LogIn', query: { to: to.path } });
      } else {
        // Если аутентификация не требуется или пользователь аутентифицирован, продолжение навигации
        next()
      }
    })
    
    export default router
