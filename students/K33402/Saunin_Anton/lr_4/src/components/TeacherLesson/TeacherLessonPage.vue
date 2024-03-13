<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  lesson: "",
  teacher: "",
});

function getCard() {
  instance
    .get(`/main/teachers-of/${router.currentRoute.value.params.id}/`, {
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
  console.log(rest);
  instance
    .patch(`/main/teachers-of/${router.currentRoute.value.params.id}/`, rest, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        router.push("/teachers-lessons");
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
      <h2>Назначить учителя на предмет</h2>
      <v-text-field label="Предмет" v-model="form.lesson.name"></v-text-field>
      <v-text-field label="Учитель" v-model="form.teacher.name"></v-text-field>
      <v-btn @click="saveCard">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
