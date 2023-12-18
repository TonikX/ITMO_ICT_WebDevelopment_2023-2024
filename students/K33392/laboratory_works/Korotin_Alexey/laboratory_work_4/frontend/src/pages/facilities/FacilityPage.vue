<template>
    <q-page class="column bg-primary flex-center" padding>
        <div class="q-mb-sm">
            <q-btn color="secondary" class="text" icon="delete" label="Delete" @click="onDelete" />
        </div>
        <div class="column">
            <FacilityCard v-model="facility" :id="facility.id" :name="facility.name" :longitude="facility._longitude"
                :latitude="facility._latitude" />
        </div>
    </q-page>
</template>
<script>
import { mapState, mapActions } from 'pinia';
import { useFacilityStore } from '@/stores/facilityStore';
import FacilityCard from '@/components/FacilityCard.vue';

export default {
    data() {
        return {
            facility: {
                id: 0,
                name: '',
                _longitude: 0,
                _latitude: 0
            }
        }
    },
    computed: {
        id() {
            return this.$route.params.id;
        },

        ...mapState(useFacilityStore, ['facilities'])
    },

    methods: {
        ...mapActions(useFacilityStore, ['fetchAll', 'delete']),

        async onDelete() {
            await this.delete(this.id);
            this.$router.push('/facilities');
        }
    },

    async beforeMount() {
        await this.fetchAll();
        const id = this.id;
        console.log(id);
        const facility = this.facilities.find((f) => f.id == id);
        console.log(facility);
        this.facility = facility;
    },

    components: { FacilityCard }
}
</script>
<style lang="scss">
@import '@/css/app.scss';
</style>