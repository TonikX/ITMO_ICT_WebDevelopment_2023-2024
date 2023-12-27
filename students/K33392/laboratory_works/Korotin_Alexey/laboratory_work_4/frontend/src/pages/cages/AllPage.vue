<template>
    <q-page class="bg-primary" padding>
        <q-dialog v-model="modal">
            <q-card class="bg-primary">
                <q-card-section>
                    <div class="text text-h6">Create cage</div>
                </q-card-section>

                <q-separator />
                <q-form >
                    <q-card-section style="max-height: 50vh" class="scroll">
                        <q-input label-color="white" label="Name" placeholder="Facility name" input-class="input-field"
                            type="text" ></q-input>
                        <q-input label-color="white" label="Longitude" placeholder="Facility longitude" input-class="input-field"
                            type="number" ></q-input>
                        <q-input label-color="white" label="Latitude" placeholder="Facility latitude" input-class="input-field"
                            type="number"></q-input>

                    </q-card-section>

                    <q-separator />

                    <q-card-actions align="right">
                        <q-btn flat label="Create" type="submit" color="secondary" v-close-popup />
                        <q-btn flat label="Close" color="secondary" v-close-popup  />
                    </q-card-actions>
                </q-form>
            </q-card>
        </q-dialog>
        <div class="column">
            <q-select label-color="primary" bg-color="secondary" v-model="facility" :options="options" label="Facility"
                filled dropdown-icon="img:src/assets/icons.svg#facility" options-dense />
        </div>
        <div class="row justify-between flex-center q-mt-xl">
            <div class="text text-h6 ">Cages</div>
            <div>
                <q-btn color="secondary" text-color="primary" icon="add" label="Add" @click="modal = true;" />
            </div>
        </div>
        <div class="row">
            <CageCard v-for="cage in filteredCages" v-bind:key="cage.id" :id="cage.id" :row="cage.row" :column="cage.column"
                :responsible="cage.responsible" :facility="cage.facility" class="border-hover"
                @click="$router.push({ path: `/cages/${cage.id}` })"></CageCard>
        </div>
    </q-page>
</template>
<script>

import { useFacilityStore } from '@/stores/facilityStore';
import { useCageStore } from '@/stores/cageStore';
import { mapState, mapActions } from 'pinia';
import CageCard from '@/components/CageCard.vue';
export default {
    data() {
        return {
            modal: false,
            facility: 'Any',
        }
    },

    computed: {
        ...mapState(useFacilityStore, ['facilities']),
        ...mapState(useCageStore, ['cages']),

        options() {
            const options = this.facilities.map((f) => f.name);
            options.push('Any');
            return options;
        },

        filteredCages() {
            if (this.facility === 'Any') {
                return this.cages;
            }
            return this.cages.filter((c) => c.facility.name == this.facility);
        }
    },
    methods: {
        ...mapActions(useCageStore, ['fetchAll'])
    },

    async mounted() {
        await this.fetchAll();
    },

    components: { CageCard }
}
</script>
<style scoped lang="scss">
@import '@/css/app.scss';
</style>