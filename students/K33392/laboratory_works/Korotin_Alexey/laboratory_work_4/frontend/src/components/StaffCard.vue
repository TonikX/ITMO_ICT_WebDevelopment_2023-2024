<template>
    <div class="col-2 q-pa-sm q-ma-sm">
        <div class="row q-pb-sm justify-between">
            <svg class="staff-icon cursor-pointer" @click="$router.push({path: `/staff/${username}`})">
                <use xlink:href="@/assets/icons.svg#person"></use>
            </svg>
            <svg class="eye-icon cursor-pointer self-end q-mr-md" role="button" :class="{ active: !hidden }"
                @click="hidden = !hidden">
                <use xlink:href="@/assets/icons.svg#eye"></use>
            </svg>
        </div>
        <div class="">
            <p class="text">Username: <span class="text-secondary">{{ username }}</span></p>
            <p class="text">Role: <span class="text-secondary">{{ role }}</span></p>
            <p class="text">Passport: <span class="text-secondary text-sensitive" :class="{ blur: isHidden }">{{ passport
            }}</span></p>
            <p class="text">Salary: <span class="text-secondary text-sensitive" :class="{ blur: isHidden }">{{ salary
            }} Rub</span></p>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        username: {
            type: String,
            required: true
        },
        passport: {
            type: String,
            required: true
        },
        role: {
            type: String,
            required: true
        },
        salary: {
            type: Number,
            required: true
        },
        hide: {
            type: Boolean,
            required: true
        }
    },
    data() {
        return {
            hidden: true
        }
    },

    computed: {
        isHidden() {
            return this.hidden && this.hide;
        }
    }
}
</script>
<style scoped lang="scss">
@import '@/css/quasar.variables.scss';
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

.eye-icon {
    stroke: $text;
    width: 30px;
    height: 30px;
    transition: stroke 0.3s;
}

.text {
    font-size: 18px;
}

.text-sensitive {
    transition: all 0.3s;
}

.blur {
    filter: blur(0.3rem);
}
</style>