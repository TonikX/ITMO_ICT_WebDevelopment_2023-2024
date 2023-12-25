<script>
import router from '@/router'
import api from '@/api'
export default {
  data() {
    return { postId: this.$route.params.id, content: '' }
  },
  methods: {
    publish() {
      api
        .post('api/post_comments/', {
          content: this.content,
          post: this.postId,
        })
        .then((_) => router.push({ path: `/posts/${this.postId}` }))
        .catch((_) => alert('Failed to create a comment'))
    },
  },
}
</script>

<template>
  <h2>New comment</h2>
  <label for="content">Content</label>
  <br />
  <textarea name="content" cols="30" rows="10" v-model="content"></textarea>
  <br /><br />
  <button v-on:click="publish">Create</button>
</template>

