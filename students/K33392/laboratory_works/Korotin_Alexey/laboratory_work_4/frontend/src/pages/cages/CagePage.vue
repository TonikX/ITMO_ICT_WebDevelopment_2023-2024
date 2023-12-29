<template>
    <q-page class="column bg-primary" padding>
        Cage {{ id }}
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
            cage: {}
        }
    },
    computed: {
        ...mapState(useFacilityStore, ['facilities']),
        ...mapState(useStaffStore, ['staff']),
        
        id() {
            return this.$route.params.id;
        }
    },
    methods: {
        ...mapActions()
    }

}
</script>