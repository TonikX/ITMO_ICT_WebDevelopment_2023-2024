import { createRouter, createWebHistory } from 'vue-router'
import AuthView from "@/views/AuthView.vue"
import ProfileView from "@/views/ProfileView.vue"
import PostsView from "@/views/PostsView.vue"
import PostView from "@/views/PostView.vue"
import NewPostView from "@/views/NewPostView.vue"
import NewCommentView from "@/views/NewCommentView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/auth',
      name: 'auth',
      component: AuthView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/posts',
      name: 'posts',
      component: PostsView
    },
    {
      path: '/posts/:id',
      name: 'post',
      component: PostView
    },
    {
      path: '/posts/:id/newcomment',
      name: 'newcomment',
      component: NewCommentView
    },
    {
      path: '/newpost',
      name: 'newpost',
      component: NewPostView
    },
  ]
})

export default router
