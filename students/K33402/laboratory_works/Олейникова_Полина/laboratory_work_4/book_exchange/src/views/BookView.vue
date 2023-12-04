<template>
    <q-page padding>
        <book-info
            v-if="book"
            :book="book"
            :is-small="false"
            :get-books="getBook"
            :delete-callback="goToBooks"
        />

        <not-found v-if="!book" />

        <q-inner-loading :showing="isLoading">
            <q-spinner-gears
                size="50px"
                color="primary"
            />
        </q-inner-loading>
    </q-page>
</template>
  
<script>
import { onMounted } from 'vue'
import { useBooksStore } from '../stores/books'
import { useRoute, useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'
import BookInfo from '../components/BookInfo.vue'
import NotFound from '../components/NotFound.vue'

export default {
    components: { NotFound, BookInfo },

    setup() {
        const route = useRoute()
        const router = useRouter()

        const booksStore = useBooksStore()
        const { book, isLoading } = storeToRefs(booksStore)

        onMounted(() => getBook())

        const getBook = () => {
            booksStore.getBook(route.params.id)
        }

        const goToBooks = () => {
            router.push({ path: '/books/my' })
        }

        return {
            isLoading,
            book,
            getBook,
            goToBooks
        }
    }
}
</script>
  