<template>
    <q-card>
        <q-card-section>
            <router-link
                v-if="isSmall"
                class="text-h6 book-link"
                :to="'/books/' + book.id"
            >
                {{ book.title }}
            </router-link>
            <div
                v-else
                class="text-h6"
            >
                {{ book.title }}
            </div>
            <div class="text-subtitle">{{ book.author }}</div>
            <div
                v-if="user && user.username !== book.owner.username"
                class="text-subtitle text-grey"
            >
                Owner: {{ book.owner.first_name }} {{ book.owner.last_name }},
                {{ book.owner.location }}
            </div>
        </q-card-section>

        <q-card-section>
            <div :class="{ 'max-lines-3': isSmall }">
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
        <q-card-actions v-if="user && user.username === book.owner.username">
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
</template>

<script>
import { useUserStore } from '../stores/user'
import { storeToRefs } from 'pinia'
import { useQuasar } from 'quasar'
import RequestDialog from '../components/RequestDialog.vue'
import BookDialog from '../components/BookDialog.vue'
import BookDeleteDialog from '../components/BookDeleteDialog.vue'
import { RouterLink } from 'vue-router'

export default {
    components: { RouterLink },

    props: {
        book: {
            type: Object,
            default: () => ({})
        },
        getBooks: {
            type: Function,
            default: () => { }
        },
        isSmall: {
            type: Boolean,
            default: true
        },
        deleteCallback: {
            type: Function,
            default: () => { }
        }
    },

    setup(props) {
        const $q = useQuasar()

        const userStore = useUserStore()
        const { user } = storeToRefs(userStore)

        const createRequest = book => {
            $q.dialog({ component: RequestDialog, componentProps: { book } })
        }

        const updateBook = book => {
            $q.dialog({
                component: BookDialog,
                componentProps: {
                    book,
                    getBooks: props.getBooks
                }
            })
        }

        const deleteBook = book => {
            $q.dialog({
                component: BookDeleteDialog,
                componentProps: {
                    book,
                    deleteCallback: props.deleteCallback
                }
            })
        }

        return {
            user,
            createRequest,
            updateBook,
            deleteBook
        }
    }
}
</script>

<style scoped>
.book-link {
    text-decoration: none;
    color: inherit !important;
}
</style>