<script>
import router from '@/router'
import api from '@/api'
import { useAuthStore } from '@/store/auth'
export default {
  data() {
    this.authStore = useAuthStore()
    return {
      title: '',
      content: '',
    }
  },
  methods: {
    publish() {
      api
        .post('api/posts/', {
          title: this.title,
          content: this.content,
          author: this.authStore.userData.username,
        })
        .then((_) => router.push({ path: '/posts' }))
        .catch((_) => alert('Failed to create a post'))
    },
  },
}
</script>

<template>
  <h2>New post</h2>
  <label for="title">Title</label>
  <br />
  <input type="text" name="title" v-model="title" />
  <br /><br />
  <label for="content">Content</label>
  <br />
  <textarea name="content" cols="30" rows="10" v-model="content"></textarea>
  <br /><br />
  <button v-on:click="publish">Create</button>
</template>

