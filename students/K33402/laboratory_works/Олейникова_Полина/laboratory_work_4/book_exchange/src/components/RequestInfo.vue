<template>
    <q-card v-if="request">
        <q-card-section>
            <router-link
                v-if="isSmall"
                class="text-h6 book-link"
                :to="'/requests/' + request.id"
            >
                {{ request.book_offered.title }}
            </router-link>
            <div
                v-else
                class="text-h6"
            >
                {{ request.book_offered.title }}
            </div>
            <div class="text-subtitle2">{{ request.book_offered.author }}</div>
            <div v-if="!isSmall">{{ request.book_offered.description }}</div>
        </q-card-section>

        <q-card-section>
            <template v-if="user && user.username !== request.book_offered.owner.username">
                <div class="text-h6">Owner</div>
                <div>Name: {{ request.book_offered.owner.first_name }} {{ request.book_offered.owner.last_name }}</div>
                <div>Email: {{ request.book_offered.owner.email }} </div>
                <div>Phone: {{ request.book_offered.owner.phone_number }} </div>
                <div>Location: {{ request.book_offered.owner.location }} </div>
            </template>
            <template v-if="user && user.username === request.book_offered.owner.username">
                <div class="text-h6">User</div>
                <div>Name: {{ request.to_user.first_name }} {{ request.to_user.last_name }}</div>
                <div>Email: {{ request.to_user.email }} </div>
                <div>Phone: {{ request.to_user.phone_number }} </div>
                <div>Location: {{ request.to_user.location }} </div>
            </template>

            <div class="text-h6">Dates</div>
            <div>From: {{ date.formatDate(request.from_date, 'YYYY-MM-DD') }} </div>
            <div>To: {{ date.formatDate(request.to_date, 'YYYY-MM-DD') }} </div>

            <div :class="'text-h6 text-' + statuses[request.status].color">{{ statuses[request.status].name }} </div>
        </q-card-section>

        <q-separator dark />

        <q-card-actions
            v-if="user && user.username === request.book_offered.owner.username && request.status == 'notconsidered'"
        >
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
</template>

<script>
import { useUserStore } from '../stores/user'
import { useRequestsStore } from '../stores/requests'
import { storeToRefs } from 'pinia'
import { RouterLink } from 'vue-router'
import { date } from 'quasar'

export default {
    components: { RouterLink },

    props: {
        request: {
            type: Object,
            default: () => ({})
        },
        updateCallback: {
            type: Function,
            default: () => ({})
        },
        isSmall: {
            type: Boolean,
            default: true
        }
    },

    setup(props) {
        const requestStore = useRequestsStore()
        const userStore = useUserStore()
        const { user } = storeToRefs(userStore)

        const statuses = {
            'rejected': { name: 'Rejected', color: 'red' },
            'accepted': { name: 'Accepted', color: 'green' },
            'notconsidered': { name: 'Not considered', color: 'grey' }
        }

        const updateRequest = async filter => {
            await requestStore.updateRequest(filter)
            props.updateCallback()
        }

        return {
            user,
            statuses,
            date,
            updateRequest
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