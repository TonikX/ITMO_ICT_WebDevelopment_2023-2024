import { defineStore } from "pinia";
import { api } from "@/boot/axios";

export const useCageStore = defineStore("cages", {
    state: () => {
        cages: [];
    },

    actions: {
        async fetchAll() {
            const response = await api.get("/cages");
            if (response.status === 200) {
                this.cages = response.data;
            }
            return response;
        },
    },
});
