<script>
import api from '@/api'
import router from '@/router'
import Comment from '@/components/Comment.vue'
import { RouterLink } from 'vue-router'
export default {
  props: ['post'],
  data() {
    return { post: this.$props.post, comments: [] }
  },
  methods: {
    newComment() {
      router.push({ path: `/posts/${this.post.id}/newcomment` })
    },
  },
  beforeMount() {
    api
      .get(`api/post_comments/${this.post.id}`)
      .then((resp) => resp.data)
      .then((data) => (this.comments = data))
      .catch((_) => alert('Failed to fetch comments'))
  },
  components: [Comment],
  components: { Comment, RouterLink },
}
</script>

<template>
  <h3>Comments</h3>
  <button v-on:click="newComment">New comment</button>
  <Comment v-for="comment in comments" :comment="comment" :key="comment.id" />
</template>

