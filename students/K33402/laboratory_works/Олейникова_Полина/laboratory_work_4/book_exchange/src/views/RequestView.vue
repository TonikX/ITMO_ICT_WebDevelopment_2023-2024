<template>
    <q-page padding>
        <request-info
            :request="request"
            :is-small="false"
            :update-callback="getRequest"
        />

        <not-found v-if="!request" />

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
import { useRoute } from 'vue-router'
import { storeToRefs } from 'pinia'
import RequestInfo from '../components/RequestInfo.vue'
import NotFound from '../components/NotFound.vue'

export default {
    components: { NotFound, RequestInfo },

    setup() {
        const route = useRoute()

        const requestsStore = useRequestsStore()
        const { request, isLoading } = storeToRefs(requestsStore)

        onMounted(() => getRequest())

        const getRequest = () => {
            requestsStore.getRequest(route.params.id)
        }

        return {
            isLoading,
            request,
            getRequest
        }
    }
}
</script>
  