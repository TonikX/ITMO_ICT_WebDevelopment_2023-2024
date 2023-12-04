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

    <book-info
      v-for="(book, i) in myBooks.results"
      :key="i"
      :book="book"
      :get-books="getBooks"
      :delete-callback="getBooks"
      class="q-mt-md"
    />
    
    <not-found v-if="myBooks.count === 0" />

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
import { useRouter, useRoute } from 'vue-router'
import { storeToRefs } from 'pinia'
import BookDialog from '../components/BookDialog.vue'
import { useQuasar } from 'quasar'
import BookInfo from '../components/BookInfo.vue'
import NotFound from '../components/NotFound.vue'

export default {
  components: { BookInfo, NotFound },

  setup() {
    const $q = useQuasar()

    const router = useRouter()
    const route = useRoute()

    const booksStore = useBooksStore()
    const { myBooks, isLoading } = storeToRefs(booksStore)

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
      await booksStore.getMyBooks(filter)
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

    const createBook = () => {
      $q.dialog({ component: BookDialog, componentProps: { getBooks } })
    }

    return {
      isLoading,
      myBooks,
      page,
      filter,
      getBooks,
      addQuery,
      pageChanged,
      searchChanged,
      createBook
    }
  }
}
</script>
