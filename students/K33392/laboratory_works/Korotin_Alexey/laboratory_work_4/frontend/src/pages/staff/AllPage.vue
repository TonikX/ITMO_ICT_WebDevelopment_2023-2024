<template>
    <q-page class="bg-primary" padding>
        <q-dialog v-model="modal">
            <q-card class="bg-primary">
                <q-card-section>
                    <div class="text text-h6">Create facility</div>
                </q-card-section>

                <q-separator />
                <q-form>
                    <q-card-section style="max-height: 50vh" class="scroll">
                        <q-input label-color="white" label="Name" placeholder="Facility name" input-class="input-field"
                            type="text"></q-input>
                        <q-input label-color="white" label="Longitude" placeholder="Facility longitude"
                            input-class="input-field" type="number"></q-input>
                        <q-input label-color="white" label="Latitude" placeholder="Facility latitude"
                            input-class="input-field" type="number"></q-input>

                    </q-card-section>

                    <q-separator />

                    <q-card-actions align="right">
                        <q-btn flat label="Create" type="submit" color="secondary" v-close-popup />
                        <q-btn flat label="Close" color="secondary" v-close-popup />
                    </q-card-actions>
                </q-form>
            </q-card>
        </q-dialog>

        <div class="row justify-between flex-center">
            <div class="row">
                <div class="text text-h6">Staff</div>
                <svg class="eye-icon cursor-pointer q-ml-md" :class="{ active: !hide }" @click="hide = !hide">
                    <use xlink:href="@/assets/icons.svg#eye"></use>
                </svg>
            </div>
            <div>
                <q-btn color="secondary" text-color="primary" icon="add" label="Add" @click="modal = true;" />
            </div>
        </div>

        <div class="row">
            <StaffCard v-for="(person, index) in staff" v-bind:key="index" :username="person.username" :role="person.role"
                :passport="person.passport" :salary="person.salary" :hide="hide" class="border-hover" />
        </div>
    </q-page>
</template>
<script>
import StaffCard from '@/components/StaffCard.vue';
import { useStaffStore } from '@/stores/staffStore';
import { mapState, mapActions } from 'pinia';
import { ref } from 'vue';

export default {
    data() {
        return {
            modal: false,
            hide: ref(true)
        }
    },
    computed: {
        ...mapState(useStaffStore, ['staff'])
    },
    methods: {
        ...mapActions(useStaffStore, ['fetchAll'])
    },
    mounted() {
        this.fetchAll();
    },
    components: { StaffCard }
}
</script>
<style scoped lang="scss">
@import '@/css/app.scss';

.eye-icon {
    stroke: $text;
    width: 30px;
    height: 30px;
}
</style>