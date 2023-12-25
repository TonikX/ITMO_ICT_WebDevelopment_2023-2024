<template>
  <section>
    <v-app>
      <bar-layout>
        <OneBook/>
      </bar-layout>
      <v-main class="vh-100" style="background-color: hsl(0, 0%, 96%);">
        <v-row class="mx-3.5">
          <v-col cols="5" class="mx-auto">
            <br><br>
            <div>
              <v-card
                v-if="book"
                elevation="2"
                outlined
                class="my-5"
              >
                <v-card-title>
                  <h2>{{ this.book.title }}</h2>
                </v-card-title>

                <v-card-text>
                  <div class="text--primary">
                    <b>Авторы:</b> {{ this.book.author }}<br>
                    <b>Издательство:</b> {{ this.book.publisher }} <br>
                    <b>Библиотечный номер:</b> {{ this.book.id }} <br>
                    <br>
                    <b>Экземпляры книги:</b>
                    <ul>
                      <li v-for="book_instance in this.book.book_instances" v-bind:key="book_instance"
                          v-bind:book_instance="book_instance">

                        <b>Год издания:</b> {{ book_instance.year }}<br>
                        <b>Секция:</b> {{ book_instance.section }}<br>
                        <b>Артикул:</b> {{ book_instance.code }}<br>
                        <v-btn v-if="!book_instance.takenId" color="primary" light
                               @click="onSelectReader(book_instance.id)">Выдать книгу
                        </v-btn>
                        <v-card
                          v-else
                          elevation="2"
                          outlined
                          class="my-2">
                          <v-card-text>
                            <div class="text--primary">Книга сейчас читается</div>
                          </v-card-text>
                          <v-spacer></v-spacer>
                          <v-btn block color="red" light @click="onReturnBook(book_instance)">Вернуть книгу в библиотеку</v-btn>
                        </v-card>
                        <br>
                      </li>
                    </ul>
                  </div>
                </v-card-text>
              </v-card>


            </div>
          </v-col>
        </v-row>
      </v-main>
    </v-app>
  </section>
  <v-dialog v-if="givingBook" :model-value="true" @close="givingBook = null">
    <div style="padding: 20px">
      <v-card>
        <v-list density="compact">
          <v-list-subheader>Читатели</v-list-subheader>
          <select v-model="givingBook.reader" style="outline: 1px solid black">
            <option disabled :value="null">Выберите читателя</option>
            <option
              v-for="r in readers"
              :key="r.id"
              :value="r"
            >
              {{ r.name }}
            </option>
          </select>
        </v-list>
        <v-spacer></v-spacer>
        <div v-if="givingBook.reader">
          <v-btn color="primary" @click="onGivingBook">Выдать</v-btn>
        </div>
      </v-card>
    </div>
  </v-dialog>
</template>


<script>
import BarLayout from '@/layouts/BarLayout.vue'
import OneBook from '@/components/OneBook.vue'
import axios from 'axios'
import {th} from "vuetify/locale";

export default {
  name: 'BookView',
  components: {BarLayout, OneBook},
  data() {
    return {
      book: null,
      readers: null,
      takenBooks: null,
      givingBook: null,
      bookInstancesById: {}
    }
  },
  async created() {
    [this.book, this.takenBooks] = await Promise.all([
      axios.get('http://127.0.0.1:8000/library/books/' + this.$route.params.id).then(r => r.data),
      axios.get('http://127.0.0.1:8000/library/taking_book/list/').then(r => r.data)
    ])
    for (const item of this.book.book_instances) {
      item.takenId = null
      this.bookInstancesById[item.id] = item
    }
    for (const tb of this.takenBooks) {
      if (this.bookInstancesById[tb.book_instance]) {
        this.bookInstancesById[tb.book_instance].takenId = tb.id
      }
    }
  },
  methods: {
    async onReturnBook(book_instance) {
      await axios.delete('http://127.0.0.1:8000/library/taking_book/' + book_instance.takenId)
      book_instance.takenId = null
    },
    async onSelectReader(bookId) {
      if (!this.readers) {
        const response = await axios.get('http://127.0.0.1:8000/library/readers/list/')
        this.readers = response.data
      }
      this.givingBook = {
        bookId,
        reader: null
      }
    },
    async onGivingBook() {
      const date = new Date()
      const pad = (n) => String(n).padStart(2, '0')
      const ymd = `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())}`
      const response = await axios.post('http://127.0.0.1:8000/library/taking_book/', {
        book_instance: this.givingBook.bookId,
        reader: this.givingBook.reader.id,
        data_issue: ymd
      }).then(r => r.data)
      this.bookInstancesById[response.book_instance].takenId = response.id
      this.givingBook = null
    }
  }
}
</script>
