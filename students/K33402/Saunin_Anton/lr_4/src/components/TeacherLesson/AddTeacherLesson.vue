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

const lessons = ref([]);
const teachers = ref([]);

function add() {
  instance
    .post("/main/teachers-of/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        router.push("/teachers-lessons");
      }
    })
    .catch((error) => console.log(error));
}

function getRooms() {
  instance
    .get("/main/teachers/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        teachers.value = response.data;
      }
    })
    .catch((error) => console.log(error));

  instance
    .get("/main/lessons/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        lessons.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getRooms();
});
</script>

<template>
  <v-app>
    <div class="w-50 mx-auto">
      <h2>Назначить учителя на предмет</h2>
      <v-select
        label="Предмет"
        v-model="form.lesson"
        :items="lessons"
        item-title="name"
        item-value="id"
      ></v-select>
      <v-select
        label="Учитель"
        v-model="form.teacher"
        :items="teachers"
        item-title="name"
        item-value="id"
      ></v-select>
      <v-btn @click="add">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
