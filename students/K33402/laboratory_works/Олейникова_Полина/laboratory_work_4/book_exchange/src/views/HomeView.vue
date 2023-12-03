<template>
  <q-page padding>
    <q-input
      v-model="filter.search"
      filled
      label="Enter author or title"
      @keyup.enter="searchChanged"
      @blur="searchChanged"
    />

    <q-card
      v-for="(book, i) in books.results"
      :key="i"
      class="q-mt-md"
    >
      <q-card-section>
        <div class="text-h6">{{ book.title }}</div>
        <div class="text-subtitle">{{ book.author }}</div>
        <div class="text-subtitle text-grey">
          Owner: {{ book.owner.first_name }} {{ book.owner.last_name }},
          {{ book.owner.location }}
        </div>
      </q-card-section>

      <q-card-section>
        <div class="max-lines-3">
          {{ book.description }}
        </div>
      </q-card-section>

      <q-separator dark />

      <q-card-actions v-if="user && user.username !== book.owner.username">
        <q-btn
          flat
          @click="createRequest(book)"
        >
          Request
        </q-btn>
      </q-card-actions>
    </q-card>

    <div class="flex justify-center q-mt-lg">
      <q-pagination
        v-model="page"
        :max="Math.ceil(books.count / filter.limit)"
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
import { useQuasar } from 'quasar'
import RequestDialog from '../components/RequestDialog.vue'

export default {
  setup() {
    const $q = useQuasar()

    const router = useRouter()
    const route = useRoute()

    const booksStore = useBooksStore()
    const userStore = useUserStore()
    const { books, isLoading } = storeToRefs(booksStore)
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
      await booksStore.getBooks(filter)
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

    const createRequest = book => {
      $q.dialog({ component: RequestDialog, componentProps: { book } })
    }


    return {
      isLoading,
      user,
      books,
      page,
      filter,
      addQuery,
      pageChanged,
      searchChanged,
      createRequest
    }
  }
}
</script>
