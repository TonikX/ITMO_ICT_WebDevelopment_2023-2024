<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row align="center" class="mb-4">
          <v-col cols="auto" class="d-flex align-center">
            <h1 class="text-h2 font-weight-bold" style="color: #1976D2;">Routes</h1>
            <!-- Updated font style and color -->
          </v-col>

          <v-col class="d-flex justify-end">
            <v-btn color="green" dark @click="openDialogForNewRoute">Add Route</v-btn>
            <!-- Added dark property for contrast -->
          </v-col>
        </v-row>

        <v-data-table
            :headers="headers"
            :items="routes"
            class="elevation-2"
            :footer-props="{ 'items-per-page-options': [5, 10, 15, -1] }"
            :items-per-page="5"
            dense
        >
          <template #item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>
                <v-expansion-panels popout> <!-- Maintains the popout effect for dynamic interaction -->
                  <v-expansion-panel>
                    <v-expansion-panel-header class="font-weight-medium">View Details</v-expansion-panel-header>
                    <!-- Adds a header for a cleaner look -->
                    <v-expansion-panel-content>
                      <div class="py-3"> <!-- Increased padding for better spacing -->
                        <div class="pb-2">
                          <v-icon small color="orange darken-2" class="mr-2">mdi-checkbox-marked-circle-outline</v-icon>
                          <strong>Difficulty:</strong> {{ item.difficulty }}
                        </div>
                        <div class="pb-2">
                          <v-icon small color="blue darken-2" class="mr-2">mdi-ruler-square</v-icon>
                          <strong>Length:</strong> {{ item.length }} km
                        </div>
                        <div class="pb-2">
                          <v-icon small color="teal darken-2" class="mr-2">mdi-elevation-rise</v-icon>
                          <strong>Peak Height:</strong> {{ item.peak_height }} m
                        </div>
                        <div class="pb-2">
                          <v-icon small color="purple darken-2" class="mr-2">mdi-timer-sand</v-icon>
                          <strong>Estimated Time:</strong> {{ item.estimated_time }}
                        </div>
                        <div class="pb-2">
                          <v-icon small color="green darken-2" class="mr-2">mdi-text</v-icon>
                          <strong>Description:</strong> {{ item.description }}
                        </div>
                      </div>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </td>
              <td>
                <v-btn icon @click="editRoute(item)">
                  <v-icon color="blue">mdi-pencil</v-icon>
                </v-btn> <!-- Use icon button for a more minimalist approach -->
                <v-btn icon @click="deleteRoute(item.id)">
                  <v-icon color="red">mdi-delete</v-icon>
                </v-btn> <!-- Use icon button for consistency -->
              </td>
            </tr>

          </template>
        </v-data-table>

        <v-dialog v-model="dialog" max-width="600px">
          <v-card>
            <v-alert v-if="serverError" type="error" dense class="mb-2">
              {{ serverError }}
            </v-alert>
            <v-card-title class="gradient-background" style="color: white;"> <!-- Gradient background for title -->
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
                    :items="['Easy', 'Difficult', 'Expert']"
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

<style scoped>
.gradient-background {
  background: linear-gradient(45deg, #1976D2, #673AB7); /* Gradient from blue to purple */
}
</style>

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
        await api.delete(`routes/${routeId}/`);
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
          await api.patch(`routes/${this.currentRoute.id}/`, this.currentRoute);
        } else {
          console.log(this.currentRoute)
          await api.post('routes/', this.currentRoute);
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