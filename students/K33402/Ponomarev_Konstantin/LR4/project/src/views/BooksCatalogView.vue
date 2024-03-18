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
              <h2>Каталог</h2>
              <v-card elevation="5" outlined class="my-2" v-for="book in books" v-bind:key="book" v-bind:book="book">
                <a @click.prevent="navigateToBookDetails(book.id)">{{ book.name }}</a>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-main>
    </v-app>
  </section>
</template>

<script>
import BarLayout from '@/layouts/BarLayout.vue'
import AllBooks from '@/components/AllBooks.vue'
import axios from 'axios'
import libraryApi from "@/domain/api";

export default {
  name: 'BooksCatalogView',
  data() {
    return {
      books: ''
    }
  },
  created() {
    this.loadBooks()
  },
  components: {BarLayout, AllBooks},

  methods: {
    async loadBooks() {
      const response = await libraryApi.getAllBooks().then(res => res)
      this.books = response.data
    },
    navigateToBookDetails(bookID) {

      this.$router.push({name: 'BooksDetail', params: {id: bookID}})
    },
  }
}
</script>
