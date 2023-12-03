<template>
  <q-page padding>
    <q-card
      v-for="(request, i) in requestsTo"
      :key="i"
      class="q-mt-md"
    >
      <q-card-section>
        <div class="text-h6">{{ request.book_offered.title }}</div>
        <div class="text-subtitle2">{{ request.book_offered.author }}</div>
      </q-card-section>

      <q-card-section>
        <div class="text-h6">Owner</div>
        <div>Name: {{ request.book_offered.owner.first_name }} {{ request.book_offered.owner.last_name }}</div>
        <div>Email: {{ request.book_offered.owner.email }} </div>
        <div>Phone: {{ request.book_offered.owner.phone_number }} </div>
        <div>Location: {{ request.book_offered.owner.location }} </div>

        <div class="text-h6">Dates</div>
        <div>From: {{ date.formatDate(request.from_date, 'YYYY-MM-DD') }} </div>
        <div>To: {{ date.formatDate(request.to_date, 'YYYY-MM-DD') }} </div>

        <div :class="'text-h6 text-' + statuses[request.status].color">{{ statuses[request.status].name }} </div>
      </q-card-section>
    </q-card>


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
import { useRequestsStore } from '../stores/requests'
import { storeToRefs } from 'pinia'
import { date } from 'quasar'

export default {
  setup() {
    const requestStore = useRequestsStore()
    const { requestsTo, isLoading } = storeToRefs(requestStore)

    onMounted(() => getRequestsTo())

    const statuses = {
      'rejected': { name: 'Rejected', color: 'red' },
      'accepted': { name: 'Accepted', color: 'green' },
      'notconsidered': { name: 'Not considered', color: 'grey' }
    }

    const getRequestsTo = () => {
      requestStore.getRequestsTo()
    }


    return {
      statuses,
      date,
      isLoading,
      requestsTo
    }
  }
}
</script>
