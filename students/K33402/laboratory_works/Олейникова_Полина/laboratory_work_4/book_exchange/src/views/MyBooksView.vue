<template>
  <q-page padding>
    <div class="row">
      <div class="col">
        <q-input
          v-model="filter.search"
          filled
          label="Enter author or title"
          @keyup.enter="searchChanged"
          @blur="searchChanged"
        />
      </div>
      <q-btn
        color="primary"
        class="col col-auto q-ml-md"
        @click="createBook"
      >
        Create new
      </q-btn>
    </div>

    <q-card
      v-for="(book, i) in myBooks.results"
      :key="i"
      class="q-mt-md"
    >
      <q-card-section>
        <div class="text-h6">{{ book.title }}</div>
        <div class="text-subtitle2">{{ book.author }}</div>
      </q-card-section>

      <q-card-section>
        <div class="max-lines-3">
          {{ book.description }}
        </div>
      </q-card-section>

      <q-separator dark />

      <q-card-actions>
        <q-btn
          flat
          @click="deleteBook(book)"
        >
          Delete
        </q-btn>
        <q-btn
          flat
          @click="updateBook(book)"
        >
          Update
        </q-btn>
      </q-card-actions>
    </q-card>

    <div class="flex justify-center q-mt-lg">
      <q-pagination
        v-model="page"
        :max="Math.ceil(myBooks.count / filter.limit)"
        @update:model-value="pageChanged"
      />
    </div>

    <q-inner-loading :showing="isLoading">
      <q-spinner-gears
        size="50px"
        color="primary"
      />
    </q-inner-loading>
  </q-page>
</template>

<script>
import { reactive, ref, watch, onMounted } from 'vue'
import { useBooksStore } from '../stores/books'
import { useUserStore } from '../stores/user'
import { useRouter, useRoute } from 'vue-router'
import { storeToRefs } from 'pinia'
import BookDialog from '../components/BookDialog.vue'
import BookDeleteDialog from '../components/BookDeleteDialog.vue'
import { useQuasar } from 'quasar'

export default {
  setup() {
    const $q = useQuasar()

    const router = useRouter()
    const route = useRoute()

    const booksStore = useBooksStore()
    const userStore = useUserStore()
    const { myBooks, isLoading } = storeToRefs(booksStore)
    const { user } = storeToRefs(userStore)

    const page = ref(1)
    const filter = reactive({
      'limit': 5,
      'offset': 0,
      'search': null
    })

    watch(
      () => route,
      () => { getQuery() },
      { deep: true })

    onMounted(() => getQuery())

    const getBooks = async () => {
      await booksStore.getMyBooks(filter)
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    }

    const getQuery = () => {
      if (route.query.page) {
        page.value = Number(route.query.page)
        filter.offset = (page.value - 1) * filter.limit
      } else {
        page.value = 1
        filter.offset = 0
      }
      filter.search = route.query.search || null
      getBooks()
    }

    const addQuery = () => {
      const query = {}
      query.page = filter.offset / filter.limit + 1
      if (!!filter.search) {
        query.search = filter.search
      }
      router.push({ query })
    }

    const pageChanged = page => {
      filter.offset = (page - 1) * filter.limit
      addQuery()
    }

    const searchChanged = () => {
      page.value = 1
      filter.offset = 0
      addQuery()
    }

    const createBook = () => {
      $q.dialog({ component: BookDialog, componentProps: { getBooks } })
    }

    const updateBook = book => {
      $q.dialog({ component: BookDialog, componentProps: { book, getBooks } })
    }

    const deleteBook = book => {
      $q.dialog({ component: BookDeleteDialog, componentProps: { book, getBooks } })
    }

    return {
      isLoading,
      user,
      myBooks,
      page,
      filter,
      addQuery,
      pageChanged,
      searchChanged,
      createBook,
      updateBook,
      deleteBook
    }
  }
}
</script>
