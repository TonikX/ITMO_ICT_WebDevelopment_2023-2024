<script>
import api from '@/api'
import CommentsView from './CommentsView.vue'
export default {
  data() {
    return { post: { id: this.$route.params.id, title: '', content: '' } }
  },
  methods: {
    fetchPost() {
      api
        .get(`api/posts/${this.post.id}`)
        .then((resp) => resp.data)
        .then((data) => (this.post = data))
        .catch((_) => alert('Failed to fetch post'))
    },
  },
  beforeMount() {
    this.fetchPost()
  },
  components: [CommentsView],
  components: { CommentsView },
}
</script>

<template>
  <h1>{{ post.title }}</h1>
  <textarea name="content" cols="30" rows="10" readonly>{{
    post.content
  }}</textarea>
  <CommentsView :post="post" />
</template>

