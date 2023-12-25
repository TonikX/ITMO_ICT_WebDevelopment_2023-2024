<script>
import api from '@/api'
import router from '@/router'
import Comment from '@/components/Comment.vue'
import { RouterLink } from 'vue-router'
export default {
  props: ['post'],
  data() {
    return { post: this.$props.post, comments: [], currentPage: 0, perPage: 2 }
  },
  methods: {
    newComment() {
      router.push({ path: `/posts/${this.post.id}/newcomment` })
    },
    prevPage() {
      if (this.currentPage - 1 >= 0) {
        this.currentPage--
        this.fetchComments()
      }
    },
    nextPage() {
      this.currentPage++
      this.fetchComments()
    },
    fetchComments() {
      console.log('fetching ', this.currentPage)
      api
        .get(`api/post_comments/${this.post.id}`, {
          params: { page: this.currentPage, perPage: this.perPage },
        })
        .then((resp) => resp.data)
        .then((data) => (this.comments = data))
        .catch((_) => alert('Failed to fetch comments'))
    },
  },
  beforeMount() {
    this.currentPage = 0
    this.fetchComments()
  },
  components: [Comment],
  components: { Comment, RouterLink },
}
</script>

<template>
  <h3>Comments</h3>
  <button v-on:click="newComment">New comment</button>
  <Comment v-for="comment in comments" :comment="comment" :key="comment.id" />
  <div class="pagination">
    <button v-on:click="prevPage">&lt; Prev</button>
    <button v-on:click="nextPage">Next &gt;</button>
  </div>
</template>

