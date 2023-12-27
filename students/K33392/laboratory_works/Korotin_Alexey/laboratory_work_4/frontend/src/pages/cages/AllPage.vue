<template>
    <q-page class="bg-primary" padding>
        <div class="column">
            <q-select label-color="primary" bg-color="secondary" v-model="facility" :options="options" label="Facility"
                filled dropdown-icon="img:src/assets/icons.svg#facility" options-dense />
        </div>
        <h6 class="text">Cages</h6>
        <div class="row">
            <CageCard v-for="cage in filteredCages" v-bind:key="cage.id" :id="cage.id" :row="cage.row" :column="cage.column"
                :responsible="cage.responsible" :facility="cage.facility" class="border-hover"></CageCard>
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

    async beforeMount() {
        await this.fetchAll();
        this.filteredCages = this.cages;
    },

    components: { CageCard }
}
</script>
<style scoped lang="scss">
@import '@/css/app.scss';
</style>