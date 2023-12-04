<template>
    <q-dialog
        ref="dialogRef"
        @hide="onDialogHide"
    >
        <q-card class="q-dialog-plugin">
            <q-card-section>
                Are you sure you want to delete the book?
            </q-card-section>

            <q-card-actions align="right">
                <q-btn
                    color="primary"
                    label="Delete"
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
import { useDialogPluginComponent } from 'quasar'
import { useBooksStore } from '../stores/books'

export default {
    props: {
        book: {
            type: Object,
            default: () => null
        },
        deleteCallback: {
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


        const onSubmit = async () => {
            const res = await booksStore.removeBook(props.book.id)
            if (res) {
                props.deleteCallback()
                onDialogHide()
            }
        }

        return {
            onSubmit,

            dialogRef,
            onDialogHide,
            onCancelClick: onDialogCancel
        }
    }
}
</script>