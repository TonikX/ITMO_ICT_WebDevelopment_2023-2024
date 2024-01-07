<template>
    <div class="col-3 q-pa-sm">
        <div class="row q-pb-sm">
            <svg class="chicken-icon cursor-pointer" @click="$router.push({ path: `/chicken/${id}` })">
                <use xlink:href="@/assets/icons.svg#chicken"></use>
            </svg>
        </div>
        <div class="">
            <p class="text inline">Weigth: <span class="text-secondary">{{ weight }}</span></p>
            <p class="text inline">Birth: <span class="text-secondary">{{ birthDate }}</span></p>
            <p class="text inline">Monthly egg rate: <span class="text-secondary">{{ eggRate }}</span></p>
            <p class="text cursor-pointer text-href" @click="$router.push({ path: `/cages/${cage.id}` })">Cage: 
                <span class="text-secondary">{{ cage.row }}, {{ cage.column }}</span>
            </p>
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
        weight: {
            type: Number,
            required: true
        },
        birthDate: {
            type: Date,
            required: true
        },
        eggRate: {
            type: Number,
            required: true
        },
        cage: {
            type: Object,
            required: true,
            default: () => ({
                facility: {}
            })
        }

    }
}
</script>
<style scoped lang="scss">
.text {
    font-size: 18px;
}

.text-href {
    transition: color 0.3s;
}

.text-href:hover {
    color: $secondary;
}

.chicken-icon {
    fill: $text;
    width: 75px;
    height: 75px;
    transition: all 0.3s;
}

.chicken-icon:hover {
    fill: $secondary;
}
</style>
