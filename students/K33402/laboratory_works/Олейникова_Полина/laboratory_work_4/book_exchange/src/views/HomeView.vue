<template>
  <q-page padding>
    <q-input
      v-model="filter.search"
      filled
      label="Enter author or title"
      @keyup.enter="searchChanged"
      @blur="searchChanged"
    />

    <book-info
      v-for="(book, i) in books.results"
      :key="i"
      :book="book"
      :get-books="getBooks"
      :delete-callback="getBooks"
      class="q-mt-md"
    />

    <div class="flex justify-center q-mt-lg">
      <q-pagination
        v-model="page"
        :max="Math.ceil(books.count / filter.limit)"
        @update:model-value="pageChanged"
      />
    </div>

    <not-found v-if="books.count === 0" />

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
import { useRouter, useRoute } from 'vue-router'
import { storeToRefs } from 'pinia'
import BookInfo from '../components/BookInfo.vue'
import NotFound from '../components/NotFound.vue'

export default {
  components: { BookInfo, NotFound },

  setup() {
    const router = useRouter()
    const route = useRoute()

    const booksStore = useBooksStore()
    const { books, isLoading } = storeToRefs(booksStore)

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

    const getBooks = async (isScroll = false) => {
      await booksStore.getBooks(filter)
      if (isScroll) {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        })
      }
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
      getBooks(true)
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

    return {
      isLoading,
      books,
      page,
      filter,
      addQuery,
      pageChanged,
      searchChanged,
      getBooks
    }
  }
}
</script>
