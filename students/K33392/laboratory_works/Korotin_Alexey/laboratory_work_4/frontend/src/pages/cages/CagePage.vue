<template>
    <q-page class="column bg-primary" padding>
        <div class="q-mb-sm row justify-between">
            <q-btn color="secondary" text-color="primary" label="Back" @click="$router.push({ path: '/cages' })" />
            <q-btn color="secondary" text-color="primary" class="text" icon="delete" label="Delete" @click="onDelete" />
        </div>

        <div class="column flex-center">
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Facility</div>
                <div class="item-value">{{ cage.facility.name }}</div>
                <q-popup-edit v-model="cage.facility.name" auto-save>
                    <q-select v-model="cage.facility.name" :options="availableFacilities" label="Facility" filled>
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-select>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Row</div>
                <div class="item-value">{{ cage.row }}</div>
                <q-popup-edit v-model="cage.row" auto-save v-slot="scope">
                    <q-input v-model="scope.value" dense autofocus counter type="number" @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Column</div>
                <div class="item-value">{{ cage.column }}</div>
                <q-popup-edit v-model="cage.row" auto-save v-slot="scope">
                    <q-input v-model="scope.value" dense autofocus counter type="number" @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Responsible</div>
                <div class="item-value">{{ cage.responsible.username }}</div>
                <q-popup-edit v-model="cage.responsible.username" auto-save>
                    <q-select v-model="cage.responsible.username" :options="availableStaff" label="Responsible" filled>
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-select>
                </q-popup-edit>
            </div>
            <q-btn color="secondary" icon="edit" label="Edit" @click="editCage" flat />
        </div>
    </q-page>
</template>
<script>

import { useFacilityStore } from '@/stores/facilityStore';
import { useCageStore } from '@/stores/cageStore';
import { useStaffStore } from '@/stores/staffStore';

import { mapActions, mapState } from 'pinia';

export default {
    data() {
        return {
            cage: {
                responsible: '',
                facility: ''
            }
        }
    },
    computed: {
        ...mapState(useFacilityStore, ['facilities']),
        ...mapState(useStaffStore, ['staff']),

        id() {
            return this.$route.params.id;
        },

        availableStaff() {
            return this.staff.map(s => s.username);
        },

        availableFacilities() {
            return this.facilities.map(f => f.name);
        }
    },
    methods: {
        ...mapActions(useCageStore, ['fetchById']),

        async onDelete() {
            console.log('Deleted');
        },

        async editCage() {
            console.log('Edited');
        }
    },

    async mounted() {
        const cage = await this.fetchById(this.id);
        this.cage = cage;
    }

}
</script>
<style scoped lang="scss">
@import '@/css/app.scss';

.form-item {
    width: 50vw;
    max-width: 350px;
    font-size: 20px;
}
</style>