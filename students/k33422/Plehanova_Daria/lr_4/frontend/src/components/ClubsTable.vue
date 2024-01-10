<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row align="center" class="mb-3">
          <!-- Clubs Header -->
          <v-col cols="auto" class="d-flex align-center">
            <h1>Clubs</h1>
          </v-col>

          <!-- Add Button -->
          <v-col class="d-flex justify-end">
            <v-btn color="green" @click="openDialogForNewClub">Add Club</v-btn>
          </v-col>
        </v-row>
        <v-data-table
            :headers="headers"
            :items="clubs"
            class="elevation-1"
            :footer-props="{ 'items-per-page-options': [5, 10, 15, -1] }"
        >
          <template #item="{ item }">
            <tr>
              <td>{{ item.name }}</td>
              <td>
                <v-icon small>mdi-map-marker</v-icon>
                {{ item.country }}, {{ item.city }}
              </td>
              <td>
                <v-expansion-panels>
                  <v-expansion-panel>
                    <v-expansion-panel-content>
                      <div>Contact: {{ item.contact_person }}</div>
                      <div>Email: {{ item.email }}</div>
                      <div>Phone: {{ item.phone }}</div>
                      <div>Web-Site: <a :href="item.website" target="_blank">{{ item.website }}</a></div>
                      <div>Date Of Creation: {{ item.created_at }}</div>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </td>
              <td>
                <v-btn small color="primary" @click="editClub(item)">Edit</v-btn>
                <v-btn small color="red" @click="deleteClub(item.id)">Delete</v-btn>
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
                <v-text-field label="Name" v-model="currentClub.name" required></v-text-field>
                <v-text-field label="Country" v-model="currentClub.country" required></v-text-field>
                <v-text-field label="City" v-model="currentClub.city" required></v-text-field>
                <v-text-field label="Contact Person" v-model="currentClub.contact_person" required></v-text-field>
                <v-text-field label="Email" v-model="currentClub.email" required></v-text-field>
                <v-text-field label="Phone" v-model="currentClub.phone" required></v-text-field>
                <v-text-field label="Website" v-model="currentClub.website"></v-text-field>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="closeDialog">Cancel</v-btn>
                <v-btn color="blue darken-1" text @click="saveClub">Save</v-btn>
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
      clubs: [],
      dialog: false,
      currentClub: {},
      formTitle: 'New Club',
      valid: false,
      serverError: null,
      headers: [
        {title: 'Name'},
        {title: 'Location'},
        {title: 'Details', sortable: false},
        {title: 'Action', sortable: false}
      ],
    };
  },
  mounted() {
    this.fetchClubs();
  },
  methods: {
    async fetchClubs() {
      api.get('clubs/')
          .then(response => {
            this.clubs = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the clubs:", error);
          });
    },
    openDialogForNewClub() {
      this.currentClub = {};
      this.formTitle = 'New Club';
      this.dialog = true;
    },

    editClub(club) {
      this.currentClub = Object.assign({}, club);
      this.formTitle = `Edit ${club.name}`;
      this.dialog = true;
    },
    async deleteClub(clubId) {
      try {
        await api.delete(`clubs/${clubId}/`);
        await this.fetchClubs();
      } catch (error) {
        this.serverError = error.response.data;
      }
    },

    closeDialog() {
      this.dialog = false;
    },

    async saveClub() {
      this.serverError = null;
      try {
        if (this.currentClub.id) {
          // Update existing club
          await api.patch(`clubs/${this.currentClub.id}/`, this.currentClub);
        } else {
          // Create new club
          await api.post('clubs/', this.currentClub);
        }
        this.dialog = false;
        await this.fetchClubs();
      } catch (error) {
        this.serverError = error.response.data; // Handle error
      }
    },
  },
};
</script>
