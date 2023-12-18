<template>
    <q-page class="bg-primary" padding>
        <q-dialog v-model="modal">
            <q-card class="bg-primary">
                <q-card-section>
                    <div class="text text-h6">Create facility</div>
                </q-card-section>

                <q-separator />
                <q-form @submit.prevent="createFacility" ref="facilityForm">
                    <q-card-section style="max-height: 50vh" class="scroll">
                        <q-input label-color="white" label="Name" placeholder="Facility name" input-class="input-field"
                            type="text" v-model="form.name"></q-input>
                        <q-input label-color="white" label="Longitude" placeholder="Facility longitude" input-class="input-field"
                            type="number" v-model="form._longitude"></q-input>
                        <q-input label-color="white" label="Latitude" placeholder="Facility latitude" input-class="input-field"
                            type="number" v-model="form._latitude"></q-input>

                    </q-card-section>

                    <q-separator />

                    <q-card-actions align="right">
                        <q-btn flat label="Create" type="submit" color="secondary" v-close-popup />
                        <q-btn flat label="Close" color="secondary" v-close-popup  @click="clearForm"/>
                    </q-card-actions>
                </q-form>
            </q-card>
        </q-dialog>
        <div class="row justify-between flex-center">
            <div class="text text-h6 q-mt-xs">All facilities</div>
            <div>
                <q-btn color="secondary" icon="add" label="Add" @click="modal = true;" />
            </div>
        </div>

        <div class="row q-mt-xl">
            <FacilityCard v-for="facility in facilities" v-bind:key="facility.id" :id="facility.id" :name="facility.name"
                :latitude="facility._latitude" :longitude="facility._longitude"  @click="push(facility.id)" />
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
            modal: false,
            form: {
                name: '',
                _longitude: 0,
                _latitude: 0
            }
        }
    },

    computed: {
        ...mapState(useFacilityStore, ['facilities'])
    },

    methods: {
        ...mapActions(useFacilityStore, ['fetchAll', 'create']),

        clearForm() {
            this.$refs.facilityForm.reset();
        },

        push(id) {
            this.$router.push(`/facilities/${id}`);
        },

        async createFacility() {
            const response = await this.create(this.form);
            this.$refs.facilityForm.reset();
        }
    },

    async mounted() {
        this.fetchAll();
    },

    components: { FacilityCard }
}
</script>

<style scoped lang="scss">
@import '@/css/app.scss';
</style>