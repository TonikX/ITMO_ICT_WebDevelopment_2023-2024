<template>
  <v-app>
    <bar-layout>
      <EditProfile/>
    </bar-layout>
    <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
      <v-row class="mx-3.5">
        <v-col cols="4" class="mx-auto">
          <br><br>

          <div class="edit">
            <h2 style="text-align: center">Редактирование профиля</h2>
            <v-form
              @submit.prevent="saveChanges"
              ref="editForm"
              class="my-2">
              <v-card max-width=800 color="#f7f4ef">
                <v-row>
                  <v-col cols="5" class="mx-auto">
                    <v-text-field
                      label="Имя"
                      v-model="editForm.first_name"
                      name="first_name"/>

                    <v-text-field
                      label="Фамилия"
                      v-model="editForm.last_name"
                      name="last_name"/>

                  </v-col>
                </v-row>
              </v-card>
              <v-btn block type="submit" color="primary" dark>Сохранить</v-btn>
            </v-form>

          </div>
        </v-col>
      </v-row>
    </v-main>
  </v-app>
</template>
<script>
import BarLayout from '@/layouts/BarLayout.vue'
import EditProfile from '@/components/EditProfile.vue'
import axios from 'axios'
import libraryApi from "@/domain/api";

export default {
  name: 'EditProfileView',
  components: {BarLayout, EditProfile},
  data: () => ({
    reader_old: Object,
    editForm: {
      first_name: '',
      last_name: ''
    }
  }),
  created() {
    this.loadReaderData()
  },
  methods: {
    async loadReaderData() {
      const response = await libraryApi.getUser().then(res => res)
      this.reader_old = response.data
      this.editForm.first_name = response.data.first_name
      this.editForm.last_name = response.data.last_name
    },
    async saveChanges() {
      for (const [key, value] of Object.entries(this.editForm)) {
        if (value === '') {
          delete this.editForm[key]
        }
      }
      try {
        await libraryApi.changeUserData(this.editForm)
        await this.$router.push({name: 'Manager'})
      } catch (e) {
        console.error(e.message)
      }
    }
  }
}
</script>
