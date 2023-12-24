<script>
import router from '@/router'
export default {
  name: 'post',
  props: ['post'],
  methods: {
    openPost() {
      router.push({ path: `/posts/${this.post.id}` })
    },
  },
}
</script>

<template>
  <li class="post" v-on:click="openPost">
    <h3>{{ post.title }}</h3>
    <p>by {{ post.author.username }} at {{ post.created_at }}</p>
  </li>
</template>

<style scoped>
.post {
  cursor: pointer;
}
</style>

