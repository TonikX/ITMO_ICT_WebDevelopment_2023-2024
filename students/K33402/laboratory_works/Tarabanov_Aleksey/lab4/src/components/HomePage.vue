<template>
  <div>
    <h1>Hello :)</h1>
    <div style="text-align: center;">
      <router-link to="/login" style="margin-right: 10px;">Log in</router-link>|
      <router-link to="/register"> Sign up</router-link>
    </div>

  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>

h1 {
  color: #3bbcb8;
  font-size: 5em;
  margin-bottom: 20px;
  text-align: center;
}

</style>