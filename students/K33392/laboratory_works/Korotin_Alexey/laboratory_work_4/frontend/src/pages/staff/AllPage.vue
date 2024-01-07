<template>
    <q-page class="bg-primary" padding>
        <div class="row justify-between flex-center">
            <div class="row">
                <div class="text text-h6">Staff</div>
                <svg class="eye-icon cursor-pointer q-ml-md" :class="{ active: !hide }" @click="hide = !hide">
                    <use xlink:href="@/assets/icons.svg#eye"></use>
                </svg>
                <q-select class="pagesize-input text q-ml-xl" v-model="pageSize" :options="perPageOptions" label="Per page"
                    label-color="white" dense standout  flat dark filled color="secondary" />

            </div>
        </div>

        <div class="row">
            <StaffCard v-for="(person, index) in staffPage" v-bind:key="index" :username="person.username"
                :role="person.role" :passport="person.passport" :salary="person.salary" :hide="hide" class="border-hover" />
        </div>
        <div class="column flex-center">
            <q-pagination v-model="page" :max="getPageCount()" direction-links flat color="white" active-color="secondary"
                active-text-color="primary" />
        </div>
    </q-page>
</template>
<script>
import StaffCard from '@/components/StaffCard.vue';
import { useStaffStore } from '@/stores/staffStore';
import { mapState, mapActions, mapWritableState } from 'pinia';
import { ref } from 'vue';

export default {
    data() {
        return {
            modal: false,
            hide: ref(true),
            perPageOptions: [5, 10, 20, 50],
            page: 1
        }
    },
    computed: {
        ...mapState(useStaffStore, ['staff']),
        ...mapWritableState(useStaffStore, ['pageSize']),
        staffPage() {
            return this.getPage(this.page);
        }
    },
    methods: {
        ...mapActions(useStaffStore, ['fetchAll', 'getPage', 'getPageCount'])
    },
    beforeMount() {
        this.fetchAll();
    },
    components: { StaffCard }
}
</script>
<style lang="scss">
@import '@/css/app.scss';
@import '@/css/quasar.variables.scss';

.eye-icon {
    stroke: $text;
    width: 30px;
    height: 30px;
}

.pagesize-input {
    width: 100px;
}

</style>