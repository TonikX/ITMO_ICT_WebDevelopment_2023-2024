<template>
    <div class="row  q-pa-sm q-ma-sm">
        <div class="row q-pb-sm justify-between">
            <svg class="staff-icon cursor-pointer" @click="$router.push({ path: `/staff/${props.username}` })">
                <use xlink:href="@/assets/icons.svg#person"></use>
            </svg>
        </div>
        <div class="">
            <p class="text">Username: <span class="text-secondary">{{ username }}</span></p>
            <p class="text">Monthly egg rate: <span class="text-secondary">{{ monthlyRate }}</span></p>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {

        }
    },

    props: {
        username: {
            type: String,
            required: true
        },
        monthlyRate: {
            type: String,
            required: true
        }
    }
}
</script>
<style scoped lang="scss">
@import '@/css/app.scss';

.staff-icon {
    fill: $text;
    width: 75px;
    height: 75px;
    transition: opacity 0.3s;
}

.staff-icon:hover {
    fill: $secondary;
}

.text {
    font-size: 18px;
}
</style>