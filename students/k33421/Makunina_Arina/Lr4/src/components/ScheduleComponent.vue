<template>
  <v-container>
    <v-row>
      <v-col>
        <h2>Расписание для группы {{ group }} на {{ semester }} семестр</h2>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <v-btn @click="startCreate" color="primary">Добавить запись</v-btn>
      </v-col>
    </v-row>

<v-row v-for="(entries, dayOfWeek) in groupedSchedule" :key="dayOfWeek">
  <v-col v-if="entries && entries.length > 0">
    <h3>{{ dayOfWeek }}</h3>
      <v-table>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left" style="width: 20%;">Время</th>
                <th class="text-left" style="width: 20%;">Аудитория</th>
                <th class="text-left" style="width: 20%;">Предмет</th>
                <th class="text-left" style="width: 20%;">Преподаватель</th>
                <th style="width: 10%;"></th>
                <th style="width: 10%;"></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="entry in groupedSchedule[dayOfWeek]" :key="entry.id">
                <td style="width: 20%;">{{ entry.time_slot.start_time }} - {{ entry.time_slot.end_time }}</td>
                <td style="width: 20%;">{{ entry.room && entry.room.name }}</td>
                <td style="width: 20%;">{{ entry.discipline && entry.discipline.name }}</td>
                <td style="width: 20%;">{{ entry.teacher && entry.teacher.name }}</td>
                <td style="width: 10%;">
                  <v-btn icon @click="startEdit(entry.id)">
                    <v-icon color="blue">mdi-pencil</v-icon>
                  </v-btn>
                </td>
                <td style="width: 10%;">
                  <v-btn icon @click="startDelete(entry.id)">
                    <v-icon color="red">mdi-delete</v-icon>
                  </v-btn>
                </td>
              </tr>
            </tbody>
          </template>
        </v-table>
      </v-col>
    </v-row>

        <v-dialog v-model="showCreateModal" persistent max-width="600">
      <v-card>
        <v-card-title class="headline">Добавление новой записи в расписание</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="confirmCreate">
            <v-container>
                    <v-row>
                      <v-col>
                        <v-select
                          v-model="newEntry.time_slot.id"
                          :items="timeslotsOptions.map(item => item)"
                          label="Время"
                          item-text="display"
                          item-value="id"
                          required
                        ></v-select>
                        <v-select
                          v-model="newEntry.room_id"
                          :items="roomOptions"
                          label="Аудитория"
                          item-text="name"
                          item-value="id"
                          required
                        ></v-select>
                        <v-select
                          v-model="newEntry.discipline_id"
                          :items="disciplineOptions"
                          label="Предмет"
                          item-text="name"
                          item-value="id"
                          required
                        ></v-select>
                        <v-select
                          v-model="newEntry.teacher_id"
                          :items="teacherOptions"
                          label="Преподаватель"
                          item-text="name"
                          item-value="id"
                          required
                        ></v-select>
                      </v-col>
                    </v-row>
                  </v-container>

                  <v-card-actions>
                    <v-btn color="green darken-1" type="submit">Добавить</v-btn>
                    <v-btn color="red darken-1" @click="showCreateModal = false">Отмена</v-btn>
                  </v-card-actions>
                </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog v-model="showDeleteConfirm" persistent max-width="290">
      <v-card>
        <v-card-title class="headline">Подтверждение</v-card-title>
        <v-card-text>Вы действительно хотите удалить этот элемент расписания?</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="showDeleteConfirm = false">Отмена</v-btn>
          <v-btn color="red darken-1" text @click="confirmDelete">Удалить</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

      <v-dialog v-model="showEditModal" persistent max-width="600">
      <v-card>
        <v-card-title class="headline">Редактирование элемента расписания</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="confirmEdit">
            <v-container>
              <v-row>
                <v-col>
                  <v-select
                   v-model="editedEntry.time_slot_id"
                  :items="timeslotsOptions"
                  label="Время"
                  item-text="display"
                  item-value="id"
                  required
                  ></v-select>
                  <v-select
                    v-model="editedEntry.room.name"
                    :items="roomOptions"
                    label="Аудитория"
                    item-text="name"
                   item-value="id"
                    required
                  ></v-select>
                  <v-select v-model="editedEntry.discipline.name" :items="disciplineOptions" label="Предмет" item-text="name"
                   item-value="id" required></v-select>
                  <v-select v-model="editedEntry.teacher.name" :items="teacherOptions" label="Преподаватель" item-text="name"
                   item-value="id" required></v-select>
                </v-col>
              </v-row>
            </v-container>

            <v-card-actions>
              <v-btn color="green darken-1" type="submit">Сохранить</v-btn>
              <v-btn color="red darken-1" @click="showEditModal = false">Отмена</v-btn>
            </v-card-actions>
          </v-form>
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { ref, onMounted } from 'vue';
import { fetchWrapper } from "@/helpers";
import _ from 'lodash';

const baseUrl = `${import.meta.env.VITE_API_URL}`;

export default {
  data() {
    return {
      group: null,
      semester: null,
      schedule: [],
      showDeleteConfirm: false,
      scheduleIdToDelete: null,
      showEditModal: false,
      showCreateModal: false,
      newEntry: {
        time_slot_id: null,
        room_id: null,
        discipline_id: null,
        teacher_id: null,
      },
      scheduleIdToEdit: null,
      editedEntry: {
        time_slot_id: null,
        room_id: null,
        discipline_id: null,
        teacher_id: null,
      },
      timeslotsOptions: [],
      roomOptions: [],
      disciplineOptions: [],
      teacherOptions: [],
      availableRooms: [],
    };
  },

computed: {
orderedDaysOfWeek() {
  const daysMapping = {
    'Monday': 'Понедельник',
    'Tuesday': 'Вторник',
    'Wednesday': 'Среда',
    'Thursday': 'Четверг',
    'Friday': 'Пятница',
    'Saturday': 'Суббота',
  };

  const orderedDays = _.orderBy(
    _.uniq(this.schedule.map(entry => daysMapping[entry.time_slot.day_of_week_display])),
    day => Object.keys(daysMapping).indexOf(day)
  );

  console.log('Ordered Days:', orderedDays);

  return orderedDays;
},

groupedSchedule() {
  const grouped = _.groupBy(this.schedule, 'time_slot.day_of_week_display');

  console.log('Grouped Schedule:', grouped);

  return grouped;
},
},


async mounted() {
  this.group = this.$route.query.group;
  this.semester = this.$route.query.semester;

  try {
    await this.fetchSchedule();

    await this.fetchTimeSlotOptions();
    await this.fetchRoomOptions();
    await this.fetchDisciplineOptions();
    await this.fetchTeacherOptions();
  } catch (error) {
    console.error('Error fetching data:', error);
  }
},
  methods: {
    async fetchSchedule() {
      try {
        const data = await fetchWrapper.get(`${baseUrl}/schedule/?group=${this.group}&semester=${this.semester}`);
        console.log('Fetched Schedule Data:', data);
        this.schedule = data.schedule;
      } catch (error) {
        console.error('Error fetching schedule:', error);
        throw error; // Rethrow the error to propagate it up the call stack
      }
    },
    async fetchTimeSlotOptions() {
      try {
        const data = await fetchWrapper.get(`${baseUrl}/time_slots/`);
        console.log('Time Slots Data:', data);
        this.timeslotsOptions = data.time_slots.map(slot => ({
          id: slot.id,
          display: `${slot.day_of_week_display} ${slot.start_time} - ${slot.end_time}`,
        }));
      } catch (error) {
        console.error('Error fetching time slots:', error);
      }
    },
    async fetchRoomOptions() {
  try {
    const data = await fetchWrapper.get(`${baseUrl}/rooms/`);
    this.roomOptions = data.available_rooms.map(room => ({
      id: room.id,
      name: room.number,
    }));
  } catch (error) {
    console.error('Error fetching room options:', error);
  }
},

async fetchDisciplineOptions() {
  try {
    const data = await fetchWrapper.get(`${baseUrl}/disciplines/`);
    this.disciplineOptions = data.map(discipline => ({
      id: discipline.id,
      name: discipline.name,
    }));
  } catch (error) {
    console.error('Error fetching discipline options:', error);
  }
},

async fetchTeacherOptions() {
  try {
    const data = await fetchWrapper.get(`${baseUrl}/teachers/`);
    this.teacherOptions = data.teachers.map(teacher => ({
      id: teacher.id,
      name: teacher.name,
    }));
  } catch (error) {
    console.error('Error fetching teacher options:', error);
  }
},

    startCreate() {
      this.showCreateModal = true;
      this.newEntry = {
        time_slot: null,
        room_id: null,
        discipline_id: null,
        teacher_id: null,
      };
    },
    startDelete(scheduleId) {
      this.scheduleIdToDelete = scheduleId;
      this.showDeleteConfirm = true;
    },
    async confirmDelete() {
      await this.deleteSchedule(this.scheduleIdToDelete);
      this.showDeleteConfirm = false;
      this.scheduleIdToDelete = null;
    },
async confirmCreate() {
  try {
    const response = await fetchWrapper.post(`${baseUrl}/schedule/`, {
      semester: this.semester,
      group_name: this.group,
      time_slot_id: this.newEntry.time_slot_id,
      room_id: this.newEntry.room_id,
      discipline_id: this.newEntry.discipline_id,
      teacher_id: this.newEntry.teacher_id,
    });

    if (response.status === 'success') {
      await this.fetchSchedule();
    } else {
      console.error('Failed to create schedule entry:', response);
    }
  } catch (error) {
    console.error('Error creating schedule entry:', error);
  }

  this.showCreateModal = false;
},
    async deleteSchedule(scheduleId) {
      try {
        await fetchWrapper.delete(`${baseUrl}/schedule/?id=${scheduleId}`);
        this.fetchSchedule();
      } catch (error) {
        console.error('Error deleting schedule entry:', error);
      }
    },
startEdit(scheduleId) {
  this.scheduleIdToEdit = scheduleId;
  const existingEntry = this.schedule.find(entry => entry.id === scheduleId);
  if (existingEntry) {
    this.editedEntry = {
      time_slot_id: existingEntry.time_slot.id,
      room_id: existingEntry.room.id,
      discipline_id: existingEntry.discipline.id,
      teacher_id: existingEntry.teacher.id,
    };
  }
  this.showEditModal = true;
},
async confirmEdit() {
  try {
    // Send an update request to the server
    const response = await fetchWrapper.put(`${baseUrl}/schedule/${this.scheduleIdToEdit}`, {
      time_slot_id: this.editedEntry.time_slot_id,
      room_id: this.editedEntry.room_id,
      discipline_id: this.editedEntry.discipline_id,
      teacher_id: this.editedEntry.teacher_id,
    });

    if (response.status === 'success') {
      // Fetch and refresh the schedule list after editing
      await this.fetchSchedule();
    } else {
      console.error('Failed to edit schedule entry:', response);
    }
  } catch (error) {
    console.error('Error editing schedule entry:', error);
  }

  // Close the edit dialog
  this.showEditModal = false;
  this.scheduleIdToEdit = null;
},


  },
};
</script>

<style scoped>
</style>
