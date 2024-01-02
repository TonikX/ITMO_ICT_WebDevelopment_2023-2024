<template>
    <q-page class="bg-primary" padding>
        <h6 class="page-heading">Staff statistics</h6>
        <section class="row">
            <StaffStatisticsBadge v-for="stat in statistics" v-bind:key="stat.id" :username="stat.username"
                :monthlyRate="stat.average_eggs" class="border-hover"/>
        </section>
    </q-page>
</template>
<script>
import { api } from '@/boot/axios';
import StaffStatisticsBadge from '@/components/StaffStatisticsBadge.vue';

export default {
    data() {
        return {
            statistics: []
        }
    },

    methods: {
        async getStats() {

        }
    },

    async mounted() {
        const response = await api.get('/staff/statistics');
        this.statistics = response.data;
    },

    components: { StaffStatisticsBadge }
}
</script>
<style scoped lang="scss">
.page-heading {
    color: $text;

}
</style>