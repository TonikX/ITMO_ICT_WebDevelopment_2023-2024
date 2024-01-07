<script>
  import usersStore from "@/stores/user.js";
  import capsulesStore from "@/stores/capsules.js";
  import VaultOpened from "@/components/Main/Vaults/vaultOpened.vue";
  import VaultClosed from "@/components/Main/Vaults/vaultClosed.vue";

  export default {
    name: "profilePage",
    components: {VaultClosed, VaultOpened},
    data(){
      return{
        usState: usersStore(),
        capState: capsulesStore(),
      }
    },
    methods: {
      async getVault(){
        const r = await this.capState.djangoVaults()
      }
    },
  };
</script>

<template>
 <h1>Hello</h1>
</template>

<style scoped>

</style>