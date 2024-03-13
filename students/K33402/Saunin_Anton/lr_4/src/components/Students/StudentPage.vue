<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  name: "",
  age: "",
  sex: "",
  student_class: "",
});

function getCard() {
  instance
    .get(`/main/students/${router.currentRoute.value.params.id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        form.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function saveCard() {
  const { id, ...rest } = form.value;
  instance
    .patch(`/main/students/${router.currentRoute.value.params.id}/`, rest, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        router.push(`/classes/${router.currentRoute.value.params.id}/students`);
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getCard();
});
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Учащийся</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-text-field label="Возраст" v-model="form.age"></v-text-field>
      <v-select label="Пол" v-model="form.sex" :items="['f', 'm']"></v-select>
      <v-text-field label="Класс" v-model="form.student_class"></v-text-field>
      <v-btn @click="saveCard">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
