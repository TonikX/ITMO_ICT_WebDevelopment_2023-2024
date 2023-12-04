<template>
  <q-page padding>
    <request-info
      v-for="(request, i) in requestsTo"
      :key="i"
      class="q-mt-md"
      :request="request"
      :update-callback="getRequestsTo"
    />

    <not-found v-if="requestsTo.length === 0" />

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
    const { requestsTo, isLoading } = storeToRefs(requestStore)

    onMounted(() => getRequestsTo())

    const getRequestsTo = () => {
      requestStore.getRequestsTo()
    }

    return {
      isLoading,
      requestsTo,
      getRequestsTo
    }
  }
}
</script>
