<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row align="center" class="mb-3">
          <v-col cols="auto" class="d-flex align-center">
            <h1>Routes</h1>
          </v-col>

          <v-col class="d-flex justify-end">
            <v-btn color="green" @click="openDialogForNewRoute">Add Route</v-btn>
          </v-col>
        </v-row>
        <v-data-table
            :headers="headers"
            :items="routes"
            class="elevation-1"
            :footer-props="{ 'items-per-page-options': [5, 10, 15, -1] }"
        >
          <template #item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>
                <v-expansion-panels>
                  <v-expansion-panel>
                    <v-expansion-panel-content>
                      <div>Difficulty: {{ item.difficulty }}</div>
                      <div>length: {{ item.length }}</div>
                      <div>Peak Height: {{ item.peak_height }}</div>
                      <div>Estimated Time: {{ item.estimated_time }}</div>
                      <div>Description: {{ item.description }}</div>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </td>
              <td>
                <v-btn small color="primary" @click="editRoute(item)">Edit</v-btn>
                <v-btn small color="red" @click="deleteRoute(item.id)">Delete</v-btn>
              </td>
            </tr>
          </template>
        </v-data-table>

        <v-dialog v-model="dialog" max-width="600px">
          <v-card>
            <v-alert v-if="serverError" type="error" dense>
              {{ serverError }}
            </v-alert>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
            <v-form ref="form" v-model="valid">
              <v-card-text>
                <!-- Field for Name -->
                <v-text-field label="Name" v-model="currentRoute.name" required></v-text-field>

                <!-- Dropdown for Mountain -->
                <v-select
                    label="Mountain"
                    :items="mountains.map(mountain => mountain.id)"
                    v-model="currentRoute.mountain"
                    required>
                </v-select>

                <!-- Dropdown for Difficulty -->
                <v-select
                    label="Difficulty"
                    :items="['Easy', 'Moderate', 'Difficult', 'Expert']"
                    v-model="currentRoute.difficulty"
                    required>
                </v-select>

                <!-- Fields for Length, Peak Height, Estimated Time, and Description -->
                <v-text-field label="Length" v-model="currentRoute.length" type="number" required></v-text-field>
                <v-text-field label="Peak Height" v-model="currentRoute.peak_height" type="number"
                              required></v-text-field>
                <v-text-field label="Estimated Time" v-model="currentRoute.estimated_time" type="time"
                              required></v-text-field>
                <v-textarea label="Description" v-model="currentRoute.description" required></v-textarea>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDialog">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="saveRoute">Save</v-btn>
              </v-card-actions>
            </v-form>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from "@/api";

export default {
  data() {
    return {
      routes: [], // Renamed from clubs
      mountains: [],
      dialog: false,
      currentRoute: {}, // Renamed from currentClub
      formTitle: 'New Route',
      valid: false,
      serverError: null,
      headers: [
        {title: 'Name'},
        {title: 'Details', sortable: false},
        {title: 'Actions', sortable: false},
      ],
    };
  },
  mounted() {
    this.fetchRoutes();
    this.fetchMountains();
  },
  methods: {
    async fetchData(endpoint, dataProperty) {
      try {
        const response = await api.get(endpoint);
        this[dataProperty] = response.data;
      } catch (error) {
        console.error(`There was an error fetching data from ${endpoint}:`, error);
      }
    },

    fetchRoutes() {
      this.fetchData('routes/', 'routes');
    },

    fetchMountains() {
      this.fetchData('mountains/', 'mountains');
    },
    openDialogForNewRoute() {
      this.currentRoute = {};
      this.formTitle = 'New Route';
      this.dialog = true;
    },
    editRoute(route) {
      this.currentRoute = Object.assign({}, route);
      this.formTitle = `Edit ${route.name}`;
      this.dialog = true;
    },
    async deleteRoute(routeId) {
      try {
        await api.delete(`routes/${routeId}/`); // Adjust API endpoint
        await this.fetchRoutes();
      } catch (error) {
        this.serverError = error.response.data;
      }
    },
    closeDialog() {
      this.dialog = false;
    },
    async saveRoute() {
      this.serverError = null;
      try {
        if (this.currentRoute.id) {
          await api.patch(`routes/${this.currentRoute.id}/`, this.currentRoute); // Adjust API endpoint
        } else {
          console.log(this.currentRoute)
          await api.post('routes/', this.currentRoute); // Adjust API endpoint
        }
        this.dialog = false;
        await this.fetchRoutes();
      } catch (error) {
        this.serverError = error.response.data;
      }
    },
  },
};
</script>

