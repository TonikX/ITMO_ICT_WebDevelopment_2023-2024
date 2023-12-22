<template>
    <q-page class="column bg-primary " padding>
        <div class="q-mb-sm row justify-between">
            <q-btn color="secondary" text-color="primary" label="Back" @click="$router.push({ path: '/facilities' })" />
            <q-btn color="secondary" text-color="primary" class="text" icon="delete" label="Delete" @click="onDelete" />
        </div>
        <div class="column flex-center">
            <q-form @submit.prevent="editFacility" ref="facilityForm">
                <q-input label-color="white" label="Name" placeholder="Facility name" input-class="input-field" type="text"
                    v-model="facility.name"></q-input>
                <q-input label-color="white" label="Longitude" placeholder="Facility longitude" input-class="input-field"
                    type="number" v-model="facility._longitude"></q-input>
                <q-input label-color="white" label="Latitude" placeholder="Facility latitude" input-class="input-field"
                    type="number" v-model="facility._latitude"></q-input>

                <q-btn flat label="Edit" type="submit" color="secondary" v-close-popup />
            </q-form>

        </div>
    </q-page>
</template>
<script>
import { mapState, mapActions } from 'pinia';
import { useFacilityStore } from '@/stores/facilityStore';

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
        ...mapActions(useFacilityStore, ['fetchAll', 'delete', 'edit']),

        async onDelete() {
            await this.delete(this.id);
            this.$router.push('/facilities');
        },
        async editFacility() {
            await this.edit(this.facility, this.id);
            this.$router.push('/facilities');
        }
    },

    async beforeMount() {
        await this.fetchAll();
        const id = this.id;
        const facility = this.facilities.find((f) => f.id == id);
        this.facility = facility;
    },

}
</script>
<style lang="scss">
@import '@/css/app.scss';
</style>