<script setup>
import { ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  letter: "",
  year: "",
});

function add() {
  instance
    .post("/main/classes/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        router.push("/classes");
      }
    })
    .catch((error) => console.log(error));
}
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Класс</h2>
      <v-text-field label="Год" v-model="form.year"></v-text-field>
      <v-text-field label="Буква" v-model="form.letter"></v-text-field>
      <v-btn @click="add">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
