<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();

const form = ref({
  day: "",
  num_lesson: "",
  student_class: "",
  room: "",
  lesson_teacher: "",
});

const rooms = ref([]);
const classes = ref([]);
const l_t = ref([]);

function create() {
  instance
    .post("/main/schedule/", form.value, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 201) {
        router.push("/schedules");
      }
    })
    .catch((error) => console.log(error));
}

function getRooms() {
  instance
    .get("/main/rooms/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        rooms.value = response.data;
      }
    })
    .catch((error) => console.log(error));

  instance
    .get("/main/classes/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        classes.value = response.data;
      }
    })
    .catch((error) => console.log(error));

  instance
    .get("/main/teachers-of/clear/", {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 200) {
        l_t.value = response.data;
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
      <h2>Добавить расписание</h2>
      <v-select
        label="День недели"
        v-model="form.day"
        :items="['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']"
      ></v-select>
      <v-text-field
        label="Порядковый номер урока"
        v-model="form.num_lesson"
      ></v-text-field>
      <v-select
        label="Аудитория"
        v-model="form.room"
        :items="rooms"
        item-title="num"
        item-value="id"
      ></v-select>
      <v-select
        label="Класс"
        v-model="form.student_class"
        :items="classes"
        :item-title="(item) => item.year + item.letter"
        item-value="id"
      ></v-select>
      <v-select
        label="Учитель и предмет"
        v-model="form.lesson_teacher"
        :items="l_t"
        :item-title="(item) => item.teacher + ' ' + item.lesson"
        item-value="id"
      ></v-select>
      <v-btn @click="create">Создать</v-btn>
    </div>
  </v-app>
</template>
<style scoped></style>
