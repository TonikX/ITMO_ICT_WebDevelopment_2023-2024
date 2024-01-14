<template>
        <v-card-actions>
          <v-btn text @click="goBack">Вернуться назад</v-btn>
        </v-card-actions>
  <v-container>
    <v-row>
      <v-col cols="12" sm="6" md="4" v-for="(group, groupName) in groups" :key="groupName">
        <v-card class="mb-4">
          <v-card-title class="headline">
            Группа: {{ groupName }}
          </v-card-title>
          <v-card-subtitle v-if="group.average_grade">
            Средний балл: {{ group.average_grade }}
          </v-card-subtitle>
          <v-card-actions>
            <v-btn color="primary" block @click="viewStudents(groupName, group.students)">
              Просмотреть студентов
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-dialog v-model="isDialogOpen" max-width="600px">
      <v-card>
        <v-card-title class="headline">Студенты в группе {{ selectedGroupName }}</v-card-title>
        <v-card-text>
          <v-data-table
            :headers="headers"
            :items="selectedStudents"
            :items-per-page="5"
            class="elevation-1"
          ></v-data-table>
        </v-card-text>
        <v-card-actions>
          <v-btn text @click="closeDialog">Закрыть</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { fetchWrapper, router } from '@/helpers';

const baseUrl = import.meta.env.VITE_API_URL;

const groups = ref({});
const isDialogOpen = ref(false);
const selectedGroupName = ref('');
const selectedStudents = ref([]);

const headers = [
  { text: 'ID', value: 'id' },
  { text: 'Имя студента', value: 'name' },
];

const fetchGroups = async () => {
  const response = await fetchWrapper.get(`${baseUrl}/groups/`);
  groups.value = response.groups;
};

const viewStudents = (groupName, students) => {
  selectedGroupName.value = groupName;
  selectedStudents.value = students;
  isDialogOpen.value = true;
};

const closeDialog = () => {
  isDialogOpen.value = false;
};

const goBack = () => {
  router.push('/')
};

onMounted(fetchGroups);
</script>

<style>
</style>
