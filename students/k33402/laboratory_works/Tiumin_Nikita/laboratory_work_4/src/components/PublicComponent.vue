<template>
  <router-view/>
</template>

<script>
export default {
  name: "PublicComponent"
}
</script>

<style>
.form-container {
  margin-top: 10%;
  max-width: 30%;
}
.form-container__buttons {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.form-container__buttons__submit_button {
  background-color: var(--header-color);
  color: var(--bg-color);
}
</style>