<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  name: "",
});

function getCard() {
  instance
    .get(`/main/teachers/${router.currentRoute.value.params.id}/`, {
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
    .patch(`/main/teachers/${router.currentRoute.value.params.id}/`, rest, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        router.push("/teachers");
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
      <h2>Учитель</h2>
      <v-text-field label="Имя" v-model="form.name"></v-text-field>
      <v-btn @click="saveCard">Сохранить</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
