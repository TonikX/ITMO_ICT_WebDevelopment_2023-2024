<template>
    <q-page class="column bg-primary " padding>
        <div class="q-mb-sm row justify-between">
            <q-btn color="secondary" text-color="primary" label="Back" @click="$router.push({ path: '/facilities' })" />
            <q-btn color="secondary" text-color="primary" class="text" icon="delete" label="Delete" @click="onDelete" />
        </div>
        <div class="column flex-center">
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Name</div>
                <div class="item-value">{{ facility.name }}</div>
                <q-popup-edit v-model="facility.name" auto-save v-slot="scope">
                    <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Longitude</div>
                <div class="item-value">{{ facility._longitude }} deg</div>
                <q-popup-edit v-model="facility._longitude" auto-save v-slot="scope">
                    <q-input type="number" v-model="scope.value" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Latitude</div>
                <div class="item-value">{{ facility._latitude }} deg</div>
                <q-popup-edit v-model="facility._latitude" auto-save v-slot="scope">
                    <q-input type="number" v-model="scope.value" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <q-btn color="secondary" icon="edit" label="Edit" @click="editFacility" flat />
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

.form-item {
    width: 50vw;
    max-width: 350px;
    font-size: 20px;
}

.item-label {
    color: $secondary;
}

.item-value {
    text-decoration: underline;
    text-underline-offset: 0.5rem;
    cursor: pointer;
}
</style>