<template>
    <div class="col-3 q-pa-sm cursor-pointer">
        <div class="row q-pb-sm">
            <svg class="facility-icon">
                <use xlink:href="@/assets/icons.svg#facility"></use>
            </svg>
        </div>
        <div class="">
            <p class="text">Facility '{{ name }}'</p>
            <p class="text">Longitude: {{ longitude }}, latitude: {{ latitude }}</p>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        id: {
            type: Number,
            requied: true
        },
        name: {
            type: String,
            requied: true
        },
        longitude: {
            type: Number,
            requied: true
        },
        latitude: {
            type: Number,
            requied: true
        }
    }
}
</script>
<style lang="scss" scoped>
@import '@/css/app.scss';

* {
    font-size: 16px;
}

.facility-icon {
    fill: $text;
    width: 75px;
    height: 75px;
}
</style>