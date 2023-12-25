
<template>
  <section>
    <v-app>
      <bar-layout>
        <AllBooks/>
      </bar-layout>
      <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
        <v-row class="mx-3.5">
          <v-col cols="4" class="mx-auto">
            <br><br>
            <div>
              <h2>Выданные книги</h2>
              <v-card elevation="5"
                      outlined
                      class="my-2"
                      v-for="book in takenBooks"
                      :key="book"
              >
                {{ book }}
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-main>
    </v-app>
  </section>
</template>

<script setup>
import {onMounted, ref} from 'vue'
import axios from 'axios'
import AllBooks from '../components/AllBooks.vue'

const takenBooks = ref(null)
onMounted(async () => {
  // const takingBookList
  takenBooks.value = (await axios.get('http://127.0.0.1:8000/library/taking_book/list/')).data
})
</script>

<style scoped>

</style>
