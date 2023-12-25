<template>
  <form @submit.prevent>
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
    <button class="btn" @click="createWarrior">Cоздать</button>
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
        race: ""
      }
    };
  },
  methods: {
    createWarrior() {
      axios.post("http://localhost:3000/api/warriors/create", this.warrior)
  .then(response => {
    this.$emit('warriorAdded');
    this.warrior.name = "";
    this.warrior.race = "";
  })
  .catch(error => console.error(error));

    }
  }
};
</script>

<style scoped>
/* Стили для компонента WarriorForm.vue */
</style>
