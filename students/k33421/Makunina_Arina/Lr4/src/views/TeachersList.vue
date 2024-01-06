<template>
        <v-card-actions>
          <v-btn text @click="goBack">Вернуться назад</v-btn>
        </v-card-actions>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6" md="4" v-for="(teacher, index) in teachers" :key="index">
        <v-card class="mb-4 elevation-5">
          <v-card-title>
            <div>
              <div class="text-h5" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                {{ teacher.name }}
              </div>
              <div class="text-subtitle-1">Аудитория: {{ teacher.room__number }}</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn color="error" text @click="deleteTeacher(teacher.id)">
              Удалить
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-divider class="my-5"></v-divider>

    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-form @submit.prevent="addTeacher">
          <v-text-field v-model="newTeacherName" label="ФИО преподавателя" outlined dense></v-text-field>
          <v-btn color="primary" type="submit" block class="my-2">Добавить</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchWrapper } from "@/helpers";
import { useRouter } from 'vue-router'


const router = useRouter()

const baseUrl = import.meta.env.VITE_API_URL;

const teachers = ref([]);
const newTeacherName = ref('');

const goBack = () => {
  router.push('/')
};

const fetchTeachers = async () => {
  const response = await fetchWrapper.get(`${baseUrl}/teachers/`);
  teachers.value = response.teachers;
}

const deleteTeacher = async (id) => {
  await fetchWrapper.delete(`${baseUrl}/teacher/?id=${id}`);
  await fetchTeachers();
}

const addTeacher = async () => {
  await fetchWrapper.post(`${baseUrl}/teacher/`, { name: newTeacherName.value });
  newTeacherName.value = '';
  await fetchTeachers();
}

onMounted(fetchTeachers);
</script>

<style>
</style>
