<template>
    <q-dialog
        ref="dialogRef"
        @hide="onDialogHide"
    >
        <q-card class="q-dialog-plugin">
            <q-card-section>
                <q-input
                    v-model="formfields.title"
                    filled
                    label="Title *"
                    lazy-rules
                    :rules="[val => val && val.length > 0 || 'Required']"
                />
                <q-input
                    v-model="formfields.author"
                    filled
                    label="Author *"
                    lazy-rules
                    :rules="[val => val && val.length > 0 || 'Required']"
                />
                <q-input
                    v-model="formfields.description"
                    filled
                    label="Description *"
                    lazy-rules
                    type="textarea"
                    :rules="[val => val && val.length > 0 || 'Required']"
                />
            </q-card-section>

            <q-card-actions align="right">
                <q-btn
                    color="primary"
                    label="OK"
                    @click="onSubmit"
                />
                <q-btn
                    color="primary"
                    label="Cancel"
                    @click="onCancelClick"
                />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>
  
<script>
import { reactive, onMounted } from 'vue'
import { useDialogPluginComponent } from 'quasar'
import { useBooksStore } from '../stores/books'

export default {
    props: {
        book: {
            type: Object,
            default: () => null
        },
        getBooks: {
            type: Function,
            default: () => { }
        }
    },

    emits: [
        ...useDialogPluginComponent.emits
    ],

    setup(props) {
        const { dialogRef, onDialogHide, onDialogCancel } = useDialogPluginComponent()

        const booksStore = useBooksStore()

        const formfields = reactive({
            'title': null,
            'author': null,
            'description': null
        })

        onMounted(() => {
            if (props.book) {
                formfields.title = props.book.title
                formfields.author = props.book.author
                formfields.description = props.book.description
            }
        })

        const onSubmit = async () => {
            let res = false
            if (props.book) {
                res = await booksStore.updateBook({ ...formfields, id: props.book.id })
            } else {
                res = await booksStore.addBook(formfields)
            }
            if (res) {
                props.getBooks()
                onDialogHide()
            }
        }

        return {
            formfields,
            onSubmit,

            dialogRef,
            onDialogHide,
            onCancelClick: onDialogCancel
        }
    }
}
</script>