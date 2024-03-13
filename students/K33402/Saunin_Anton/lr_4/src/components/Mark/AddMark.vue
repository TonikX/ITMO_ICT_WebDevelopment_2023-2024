<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  student: "",
  schedule: "",
  mark: "",
});

const students = ref([]);

function add() {
  form.value.schedule = router.currentRoute.value.params.id;

  instance
    .post("/main/marks/", form.value, {
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

function getRooms() {
  instance
    .get("/main/students/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        students.value = response.data;
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
      <h2>Добавить оценку</h2>
      <v-select
        label="Студент"
        v-model="form.student"
        :items="students"
        item-title="name"
        item-value="id"
      ></v-select>
      <v-text-field label="Оценка" v-model="form.mark"></v-text-field>
      <v-btn @click="add">Создать</v-btn>
    </div>
  </v-app>
</template>

<style scoped></style>
