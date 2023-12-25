<template>
  <form @submit.prevent="onSubmit">
    <h1>Создание война</h1>
    <input
      v-model="warrior.name"
      class="input"
      type="text"
      placeholder="Имя"
    />
    <input
      v-model="warrior.race"
      class="input"
      type="text"
      placeholder="Расса"
    />
    <button class="btn" type="submit">Создать</button>
  </form>
</template>

<script>
import axios from "axios";

export default {
  name: "WarriorForm",
  data() {
    return {
      warrior: {
        name: "",
        race: "",
      },
    };
  },
  methods: {
    onSubmit() {
      axios.post("http://62.109.28.95:8890/warrior/create1", {
        name: this.warrior.name,
        race: this.warrior.race,
      });
    },
  },
};
</script>

<style scoped>

</style>
