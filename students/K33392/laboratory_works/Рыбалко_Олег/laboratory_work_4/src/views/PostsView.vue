<script>
import api from '@/api'
import Post from '@/components/Post.vue'
import router from '@/router'
export default {
  data() {
    return { posts: [] }
  },
  components: {
    Post,
  },
  methods: {
    getPosts() {
      api
        .get('api/posts/')
        .then((resp) => resp.data)
        .then((data) => (this.posts = data))
        .catch(() => alert('Failed to fetch posts'))
    },
    newPost() {
      router.push({ path: '/newpost' })
    },
  },
  beforeMount() {
    this.getPosts()
  },
}
</script>

<template>
  <br />
  <button v-on:click="newPost">New post</button>
  <ol class="posts">
    <Post v-for="post in posts" :post="post" :key="post.id" />
  </ol>
</template>

