import { defineStore } from "pinia";
import { djangoApi } from "@/api";

const capsulesStore = defineStore("capsules", {
    state: () => ({
        capsules: [],
    }),

    actions: {
        async loadCapsules() {
            const response = await djangoApi.getAllCapsules();
            this.capsules = response.data;
            console.log(response)
            return response;
        },
    },
});

export default capsulesStore;