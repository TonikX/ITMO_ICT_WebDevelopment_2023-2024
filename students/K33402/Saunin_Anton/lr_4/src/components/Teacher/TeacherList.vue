<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const teachers = ref([]);

function getTeachers() {
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
}

function deleteTeacher(id) {
  instance
    .delete(`/main/teachers/${id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 204) {
        getTeachers();
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getTeachers();
});
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Учителя</h2>
    <template v-for="teacher in teachers" :key="teacher.id">
      <v-card width="400" :title="teacher.name"
        ><v-card-actions>
          <v-btn @click="router.push('/teachers/' + teacher.id)">
            Изменить
          </v-btn>
          <v-btn @click="deleteTeacher(teacher.id)"> Удалить </v-btn>
        </v-card-actions></v-card
      >
    </template>
    <v-btn @click="router.push('/add-teacher')">Добавить</v-btn>
  </div>
</template>

<style scoped></style>
