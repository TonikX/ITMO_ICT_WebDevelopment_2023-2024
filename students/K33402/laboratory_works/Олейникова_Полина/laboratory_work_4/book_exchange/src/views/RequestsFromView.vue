<template>
  <q-page padding>
    <request-info
      v-for="(request, i) in requestsFrom"
      :key="i"
      class="q-mt-md"
      :request="request"
      :update-callback="getRequestsFrom"
    />

    <not-found v-if="requestsFrom.length === 0" />

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
import NotFound from '../components/NotFound.vue'
import RequestInfo from '../components/RequestInfo.vue'

export default {
  components: { NotFound, RequestInfo },

  setup() {
    const requestStore = useRequestsStore()
    const { requestsFrom, isLoading } = storeToRefs(requestStore)

    onMounted(() => getRequestsFrom())

    const getRequestsFrom = () => {
      requestStore.getRequestsFrom()
    }

    return {
      isLoading,
      requestsFrom,
      getRequestsFrom
    }
  }
}
</script>
