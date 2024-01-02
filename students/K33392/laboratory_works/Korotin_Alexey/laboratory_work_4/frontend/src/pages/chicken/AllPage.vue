<template>
    <q-page class="bg-primary" padding>
        <q-dialog v-model="modal">
            <q-card class="bg-primary">
                <q-card-section>
                    <div class="text text-h6">Register new chicken</div>
                </q-card-section>
                <q-separator />
                <q-form @submit.prevent="createChicken" ref="form">
                    <q-card-section style="max-height: 50vh" class="scroll">
                        <q-input class="q-mb-sm" v-model="form.weight" type="number" label="Weight" dark />

                        <q-input dark label="Birth date" filled v-model="form.birth_date" mask="date" :rules="['date']">
                            <template v-slot:append>
                                <q-icon name="event" class="cursor-pointer">
                                    <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                                        <q-date v-model="form.birth_date" :options="birthDateConstraint" dark minimal>
                                            <div class="row items-center justify-end">
                                                <q-btn v-close-popup label="Close" color="primary" flat />
                                            </div>
                                        </q-date>
                                    </q-popup-proxy>
                                </q-icon>
                            </template>
                        </q-input>

                        <q-input class="q-mb-sm" v-model="form.monthly_egg_rate" type="number" label="Monthly egg rate"
                            dark />
                        <q-select v-model="form.cage" :options="availableCages" label="Cage" dark label-color="white"
                            filled />

                    </q-card-section>

                    <q-separator />

                    <q-card-actions align="right">
                        <q-btn flat label="Create" type="submit" color="secondary" v-close-popup />
                        <q-btn flat label="Close" color="secondary" v-close-popup @click="clearForm" />
                    </q-card-actions>
                </q-form>
            </q-card>
        </q-dialog>
        <div class="row justify-between flex-center">
            <div class="text text-h6 q-mt-xs">All chicken</div>
            <div>
                <q-btn color="secondary" text-color="primary" icon="add" label="Add" @click="modal = true;" />
            </div>
        </div>

        <div class="row q-mt-xl">
            <ChickenCardVue v-for="c in chicken" v-bind:key="c.id" :id="c.id" :weight="c.weight" :birthDate="c.birth_date"
                :eggRate="c.monthly_egg_rate" :cage="c.cage" class="border-hover q-mr-sm" />
        </div>
    </q-page>
</template>
<script>
import ChickenCardVue from "@/components/ChickenCard.vue";
import { useChickenStore } from "@/stores/chickenStore";
import { useCageStore } from "@/stores/cageStore";
import { mapState, mapActions } from "pinia";

export default {
    data() {
        return {
            modal: false,
            form: {
                birth_date: '',
                weight: '',
                cage: ''
            }
        }
    },

    computed: {
        ...mapState(useChickenStore, ['chicken']),
        ...mapState(useCageStore, ['cages']),

        availableCages() {
            return this.cages.map(c => c.id);
        }
    },

    methods: {
        ...mapActions(useChickenStore, ['fetchAll', 'create']),

        birthDateConstraint(date) {
            return Date.parse(date) <= Date.now();
        },

        async createChicken() {
            const payload = new Object(this.form);
            payload.birth_date = payload.birth_date.replaceAll('/', '-'); // Desired date format YYYY-MM-DD
            payload.breed = 1;
            const response = await this.create(this.form);
        }
    },

    components: { ChickenCardVue },

    async mounted() {
        this.fetchAll();
    }
}
</script>

