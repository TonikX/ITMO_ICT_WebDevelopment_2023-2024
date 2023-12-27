<template>
    <div class="col-3 q-pa-sm cursor-pointer">
        <div class="row q-pb-sm">
            <svg class="cage-icon">
                <use xlink:href="@/assets/icons.svg#cage"></use>
            </svg>
        </div>
        <div class="">
            <p class="text">Facility {{ facility.name }}</p>
            <p class="text">Row {{ row }}, Column {{ column }}</p>
            <p class="text">Responsible: {{ responsible.username }}</p>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        id: {
            type: Number,
            required: true
        },
        row: {
            type: Number,
            required: true
        },
        column: {
            type: Number,
            required: true
        },
        facility: {
            type: Object,
            required: true
        },
        responsible: {
            type: Object,
            required: true
        }
    },

}
</script>
<style scoped lang="scss">
* {
    font-size: 16px;
}

.cage-icon {
    fill: $text;
    width: 75px;
    height: 75px;
}
</style>