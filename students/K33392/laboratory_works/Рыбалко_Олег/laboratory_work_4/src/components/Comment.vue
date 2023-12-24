<script>
export default {
  props: ['comment'],
}
</script>
<template>
  <p>
    {{ comment.content }} by {{ comment.author.username }} at
    {{ comment.created_at }}
  </p>
</template>

