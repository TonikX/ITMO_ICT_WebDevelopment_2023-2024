<template>
    <q-dialog
        ref="dialogRef"
        @hide="onDialogHide"
    >
        <q-card class="q-dialog-plugin">
            <q-card-section>
                <div class="text-h6">{{ book.title }}</div>
                <div class="text-subtitle2">{{ book.author }}</div>

                <div class="flex justify-center q-mt-lg">
                    <q-date
                        v-model="selectedDates"
                        range
                        :options="dates"
                        mask="YYYY-MM-DD"
                        @navigation="getAvailableDates"
                    />
                </div>
            </q-card-section>

            <q-card-actions align="right">
                <q-btn
                    color="primary"
                    label="OK"
                    :disabled="!selectedDates.from || !selectedDates.to"
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
import { onMounted, ref } from 'vue'
import { useDialogPluginComponent } from 'quasar'
import { useBooksStore } from '../stores/books'
import { useRequestsStore } from '../stores/requests'
import { date } from 'quasar'
import { storeToRefs } from 'pinia'

export default {
    props: {
        book: {
            type: Object,
            default: () => null
        }
    },

    emits: [
        ...useDialogPluginComponent.emits
    ],

    setup(props) {
        const { dialogRef, onDialogHide, onDialogCancel } = useDialogPluginComponent()

        const booksStore = useBooksStore()
        const requestsStore = useRequestsStore()
        const { dates } = storeToRefs(booksStore)

        const selectedDates = ref({ from: null, to: null })
        const showDates = ref(Date.now())

        onMounted(() => {
            getAvailableDates()
        })

        const getAvailableDates = async newDate => {
            if (newDate) {
                showDates.value = date.adjustDate(showDates.value, newDate)
            }
            await booksStore.getAvailableDates({
                date_from: date.formatDate(date.startOfDate(showDates.value, 'month'), 'YYYY-MM-DD'),
                date_to: date.formatDate(date.endOfDate(showDates.value, 'month'), 'YYYY-MM-DD'),
                id: props.book.id
            })
        }

        const onSubmit = async () => {
            if (selectedDates.value.from && selectedDates.value.to) {
                let res = await requestsStore.addRequest({
                    from_date: selectedDates.value.from,
                    to_date: selectedDates.value.to,
                    book_offered: props.book.id
                })
                if (res) {
                    onDialogHide()
                }
            }
        }

        return {
            dates,
            selectedDates,
            getAvailableDates,
            onSubmit,

            dialogRef,
            onDialogHide,
            onCancelClick: onDialogCancel
        }
    }
}
</script>