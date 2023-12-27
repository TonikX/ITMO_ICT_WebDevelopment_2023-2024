<template>
    Staff {{ username }}
</template>
<script>
export default {
    data() {
        return {

        }
    },
    computed: {
        username() {
            return this.$route.params.username;
        } 
    }
}
</script>