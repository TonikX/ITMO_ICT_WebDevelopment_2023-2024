<template>
  <div class="club-container">
    <div class="card" v-for="club in clubs">
      <strong>Имя:</strong> {{ club.name }}<br>
      <strong>Страна:</strong> {{ club.country }}, {{ club.city }}<br>
      <div class="buttoncard">
        <button class="button button" @click="$router.push(`/alp/clubs/${club.id}`)">Details</button> <br><br>
      </div>
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
.button {
  padding: 2px 180px;
}
</style>