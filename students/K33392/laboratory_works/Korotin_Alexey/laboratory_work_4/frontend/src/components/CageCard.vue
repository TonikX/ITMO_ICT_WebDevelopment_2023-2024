<template>
    <div class="col-3 q-pa-sm cursor-pointer">
        <div class="row q-pb-sm">
            <svg class="cage-icon">
                <use xlink:href="@/assets/icons.svg#cage"></use>
            </svg>
        </div>
        <div class="">
            <p class="text">Facility <span class="text-secondary">{{ facility.name }}</span></p>
            <p class="text">Row <span class="text-secondary">{{ row }}</span></p>
            <p class="text">Column <span class="text-secondary">{{ column }}</span></p>
            <p class="text">Responsible: <span class="text-secondary">{{ responsible.username }}</span></p>
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
.text {
    font-size: 18px;
}

.cage-icon {
    fill: $text;
    width: 75px;
    height: 75px;
}
</style>