<template>
    <q-page class="bg-primary text column" padding>
        <div class="q-mb-sm row justify-between">
            <q-btn color="secondary" text-color="primary" label="Back" @click="$router.push({ path: '/staff' })" />
            <q-btn color="secondary" text-color="primary" class="text" icon="delete" label="Delete" @click="onDelete" />
        </div>
        <div class="column flex-center">
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Username</div>
                <div class="item-value">{{ staff.username }}</div>
                <q-popup-edit v-model="staff.username" auto-save v-slot="scope">
                    <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Role</div>
                <div class="item-value">{{ staff.role }}</div>
                <q-popup-edit v-model="staff.role" auto-save>
                    <q-select v-model="staff.role" :options="roleOptions" label="Role" filled>
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-select>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Passport</div>
                <div class="item-value">{{ staff.passport }}</div>
                <q-popup-edit v-model="staff.passport" auto-save v-slot="scope">
                    <q-input v-model="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Salary</div>
                <div class="item-value">{{ staff.salary }}</div>
                <q-popup-edit v-model="staff.salary" auto-save v-slot="scope">
                    <q-input v-model="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Employment contract</div>
                <div class="item-value">{{ staff.employment_contract_id }}</div>
                <q-popup-edit v-model="staff.employment_contract_id" auto-save v-slot="scope">
                    <q-input v-model="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Dismissal agreement</div>
                <div class="item-value">{{ staff.dismissal_agreement_id }}</div>
                <q-popup-edit v-model="staff.dismissal_agreement_id" auto-save v-slot="scope">
                    <q-input v-model="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <q-btn color="secondary" icon="edit" label="Edit" @click="editStaff" flat />
        </div>
    </q-page>
</template>
<script>

import { useStaffStore } from '@/stores/staffStore';
import { mapActions } from 'pinia';

export default {
    data() {
        return {
            staff: {},
            roleOptions: ['Worker', 'Director']
        }
    },
    computed: {
        username() {
            return this.$route.params.username;
        }
    },
    methods: {
        ...mapActions(useStaffStore, ['fetchByUsername']),
        async onDelete() {
            console.log('Deleted');
        },
        async editStaff() {
            console.log('Edited');
        }
    },

    async created() {
        const staff = await this.fetchByUsername(this.username);
        if (staff === undefined) {
            this.$router.push({ path: '/staff' });
        }

        this.staff = staff;
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