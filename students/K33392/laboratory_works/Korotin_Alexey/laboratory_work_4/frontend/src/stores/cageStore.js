import { defineStore } from "pinia";
import { api } from "@/boot/axios";

export const useCageStore = defineStore("cages", {
    state: () => ({
        cages: []
    }),

    actions: {
        async fetchAll() {
            const response = await api.get("/cages/");
            if (response.status === 200) {
                this.cages = response.data;
            }
            return response;
        },

        async create(payload = {facility, row, column, responsible}) {
            const response = await api.post('/cages/', payload);
            if (response.status === 201) {
                await this.fetchAll();
            }

            return response;
        }
    },
});
