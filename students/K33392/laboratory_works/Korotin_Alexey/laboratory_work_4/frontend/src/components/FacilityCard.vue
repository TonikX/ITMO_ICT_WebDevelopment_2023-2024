<template>
    <div class="border-hover col-3 q-pa-sm cursor-pointer">
        <p class="text">Facility '{{ name }}'</p>
        <p class="text">Longitude: {{ longitude }}, latitude: {{ latitude }}</p>
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
</style>