<template>
    <q-page class="bg-primary" padding>
        <div class="q-mb-sm row justify-between">
            <q-btn color="secondary" text-color="primary" label="Back" @click="$router.push({ path: '/chicken' })" />
            <q-btn color="secondary" text-color="primary" class="text" icon="delete" label="Delete" @click="onDelete" />
        </div>
        <div class="column flex-center">
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Weight</div>
                <div class="item-value">{{ chicken.weight }}</div>
                <q-popup-edit v-model="chicken.weight" auto-save>
                    <q-input v-model="chicken.weight" dense autofocus counter type="number">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Birth date</div>
                <div class="item-value">{{ chicken.birth_date }}</div>
                <q-popup-edit v-model="chicken.birth_date" auto-save dark>
                    <q-date v-model="chicken.birth_date" :options="birthDateConstraint" dark minimal>
                        <div class="row items-center justify-end">
                            <q-btn v-close-popup label="Close" color="primary" flat />
                        </div>
                    </q-date>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Egg rate</div>
                <div class="item-value">{{ chicken.monthly_egg_rate }}</div>
                <q-popup-edit v-model="chicken.monthly_egg_rate" auto-save>
                    <q-input v-model="chicken.monthly_egg_rate" dense autofocus counter type="number">
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-input>
                </q-popup-edit>
            </div>
            <div class="form-item text row justify-between fit q-mb-md">
                <div class="item-label">Cage</div>
                <div class="item-value">{{ chicken.cage.id }}</div>
                <q-popup-edit v-model="chicken.cage" auto-save>
                    <q-select v-model="chicken.cage" :options="availableCages" label="Responsible" filled>
                        <template v-slot:prepend>
                            <q-icon name="edit" />
                        </template>
                    </q-select>
                </q-popup-edit>
            </div>
            <q-btn color="secondary" icon="edit" label="Edit" @click="onEdit" flat />
        </div>

    </q-page>
</template>
<script>
import { useChickenStore } from '@/stores/chickenStore';
import { mapActions, mapState } from 'pinia';
import { useCageStore } from '@/stores/cageStore';
export default {
    data() {
        return {
            chicken: {
                cage: {}
            }
        }
    },

    computed: {
        ...mapState(useCageStore, ['cages']),

        id() {
            return this.$route.params.id;
        },

        availableCages() {
            return this.cages.map(c => c.id);
        }
    },

    methods: {
        ...mapActions(useChickenStore, ['fetchById', 'delete', 'edit']),
        async onDelete() {
            const response = await this.delete(this.id);
            if (response.status === 204) {
                this.$router.push({ path: '/chicken' });
            }
        },

        async onEdit() {
            const payload = new Object(this.chicken);
            payload.birth_date = payload.birth_date.replaceAll('/', '-');
            payload.cage = payload.cage.id;
            const response = await this.edit(this.chicken, this.id);

            if (response.status === 200) {
                this.$router.push({ path: '/chicken' })
            }
        },

        birthDateConstraint(date) {
            return Date.parse(date) <= Date.now();
        },
    },

    async mounted() {
        const chicken = await this.fetchById(this.id);
        if (chicken === undefined) {
            this.$router.push({ path: '/chicken' })
        }
        this.chicken = chicken;
    }
}
</script>
<style scoped lang="scss">
.form-item {
    width: 50vw;
    max-width: 350px;
    font-size: 20px;
}
</style>