<script setup>
import { onMounted, ref } from "vue";
import instance from "@/AxiosInstance";
import router from "@/router/router";
import { TokenStore } from "@/stores/TokenStore";

const Token = TokenStore();
const students = ref([]);
const sexes = ref([]);

function getStudents() {
  instance
    .get(
      `/main/classes/${router.currentRoute.value.params.id}/show_students/`,
      {
        headers: {
          Authorization: `Bearer ${Token.token}`,
        },
      }
    )
    .then((response) => {
      if (response.status === 200) {
        students.value = response.data;
      }
    })
    .catch((error) => console.log(error));

  instance
    .get(
      `/main/classes/${router.currentRoute.value.params.id}/count_boys_and_girls/`,
      {
        headers: {
          Authorization: `Bearer ${Token.token}`,
        },
      }
    )
    .then((response) => {
      if (response.status === 200) {
        sexes.value = response.data;
      }
    })
    .catch((error) => console.log(error));
}

function deleteStudent(id) {
  instance
    .delete(`/main/students/${id}/`, {
      headers: {
        Authorization: `Bearer ${Token.token}`,
      },
    })
    .then((response) => {
      if (response.status === 204) {
        getStudents();
      }
    })
    .catch((error) => console.log(error));
}

onMounted(() => {
  getStudents();
});
</script>

<template>
  <div class="d-flex align-center flex-column ga-10">
    <h2>Учащиеся</h2>
    <v-card
      width="500"
      :title="`${sexes.boys} мальчиков, ${sexes.girls} девочек`"
    >
    </v-card>
    <v-btn
      @click="
        router.push(
          '/classes/' + router.currentRoute.value.params.id + '/statistics'
        )
      "
      >Оценки</v-btn
    >
    <template v-for="student in students" :key="student.id">
      <v-card
        width="400"
        :title="student.name"
        :subtitle="`${student.age} Y.O., ${student.sex}`"
        ><v-card-actions>
          <v-btn @click="router.push('/students/' + student.id)">
            Изменить
          </v-btn>
          <v-btn @click="deleteStudent(student.id)"> Удалить </v-btn>
        </v-card-actions></v-card
      >
    </template>
    <v-btn @click="router.push('/add-student')">Добавить</v-btn>
  </div>
</template>

<style scoped></style>
