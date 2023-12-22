<template>
  <div class="club-container">
    <div v-for="club in clubs"> <!-- v-for - директива для отображения списка элементов на основе массива. -->
      <div><strong>Имя:</strong> {{ club.name }}</div>
      <div><strong>Страна:</strong> {{ club.state }}, {{ club.city }}</div>
      <div>
        <button @click="$router.push(`/clubs/${club.id}`)">Details</button>
      </div>
      <br/>
    </div>
  </div>

</template>

<script>
export default {
  props: {
    clubs: {
      type: Array,
      required: true
    }
  }
}
</script>

<style scoped>

</style>
