<template>
  <v-sheet>
    <v-dialog width="500">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" color="purple-lighten-1" text="Изменить"> </v-btn>
      </template>

      <template v-slot:default="{ isActive }">
        <v-card title="Изменить статус успешности">
            <template v-slot:append>
              <v-btn icon="$close" variant="text" @click="isActive.value = false"></v-btn>
            </template>

            <v-divider></v-divider><br>
            <v-checkbox
              v-model="succeed"
              false-value="0"
              true-value="1"
              label="Понравилось"></v-checkbox>

            <div class="pa-4 text-center">
              <v-btn
                class="text-none"
                color="purple-lighten-2"
                min-width="92"
                rounded
                variant="outlined"
                @click="updateParticipating"
                width="300"
              >
                Изменить
              </v-btn>
            </div>

        </v-card>
      </template>
    </v-dialog>
  </v-sheet>
</template>

<script>
import axios from "axios";
import { ref } from 'vue'

export default {
  name: "ParticipatingUpdate",
  props: {
    climbing: {
      required: true
    }
  },
  data () {
    return {
      succeed: '',
      dialog: ref(true),
    }
  },
  methods: {
    async updateParticipating() {
      try {
        const response = await axios.put(`http://localhost:8000/alp/userpage/participatings/${this.climbing.id}/update/`,
          {id: this.climbing.id,
               alpinist_id: this.climbing.alpinist_id,
               climbing_id: this.climbing.climbing_id,
               succeed: this.succeed,
               admin_confirmation: this.climbing.admin_confirmation},
          {headers: {Authorization: 'Token ' + sessionStorage.getItem('token')}}
        ).then(() => {
          // Обновление данных прошло успешно
          location.reload(); // перезагрузить страницу
        })

      } catch (error) {
        console.log(error);
      }
    }
  },
}
</script>


<style scoped>

</style>
