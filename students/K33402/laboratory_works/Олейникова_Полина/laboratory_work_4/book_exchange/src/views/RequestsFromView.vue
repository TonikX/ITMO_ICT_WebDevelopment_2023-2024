<template>
  <q-page padding>
    <q-card
      v-for="(request, i) in requestsFrom"
      :key="i"
      class="q-mt-md"
    >
      <q-card-section>
        <div class="text-h6">{{ request.book_offered.title }}</div>
        <div class="text-subtitle2">{{ request.book_offered.author }}</div>
      </q-card-section>

      <q-card-section>
        <div class="text-h6">User</div>
        <div>Name: {{ request.to_user.first_name }} {{ request.to_user.last_name }}</div>
        <div>Email: {{ request.to_user.email }} </div>
        <div>Phone: {{ request.to_user.phone_number }} </div>
        <div>Location: {{ request.to_user.location }} </div>

        <div class="text-h6">Dates</div>
        <div>From: {{ date.formatDate(request.from_date, 'YYYY-MM-DD') }} </div>
        <div>To: {{ date.formatDate(request.to_date, 'YYYY-MM-DD') }} </div>

        <div :class="'text-h6 text-' + statuses[request.status].color">{{ statuses[request.status].name }} </div>
      </q-card-section>

      <q-separator dark />

      <q-card-actions v-if="request.status == 'notconsidered'">
        <q-btn-dropdown
          color="primary"
          label="Change status"
        >
          <q-list>
            <q-item
              v-close-popup
              clickable
              @click="updateRequest({ id: request.id, status: 'accepted' })"
            >
              <q-item-section>
                <q-item-label>accepted</q-item-label>
              </q-item-section>
            </q-item>

            <q-item
              v-close-popup
              clickable
              @click="updateRequest({ id: request.id, status: 'rejected' })"
            >
              <q-item-section>
                <q-item-label>rejected</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
      </q-card-actions>
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
import { useUserStore } from '../stores/user'
import { storeToRefs } from 'pinia'
import { date } from 'quasar'

export default {
  setup() {
    const requestStore = useRequestsStore()
    const userStore = useUserStore()
    const { requestsFrom, isLoading } = storeToRefs(requestStore)
    const { user } = storeToRefs(userStore)

    onMounted(() => getRequestsFrom())

    const statuses = {
      'rejected': { name: 'Rejected', color: 'red' },
      'accepted': { name: 'Accepted', color: 'green' },
      'notconsidered': { name: 'Not considered', color: 'grey' }
    }

    const getRequestsFrom = () => {
      requestStore.getRequestsFrom()
    }

    const updateRequest = async filter => {
      await requestStore.updateRequest(filter)
      getRequestsFrom()
    }

    return {
      statuses,
      date,
      isLoading,
      user,
      requestsFrom,
      updateRequest
    }
  }
}
</script>
