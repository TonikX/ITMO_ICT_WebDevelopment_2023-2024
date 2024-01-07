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
        },

        async fetchById(id) {
            let cage = this.cages.find(c => c.id == id);
            if (cage === undefined) {
                await this.fetchAll();
                cage = this.cages.find(c => c.id == id);
            }

            return cage;
        },

        async edit(payload = {facility, responsible, row, column}, id) {
            const response = await api.put(`/cages/${id}`, payload);
            if (response.status === 200) {
                const index = this.cages.findIndex(c => c.id == id);
                this.cages[index] = response.data;
            }

            return response;
        },

        async delete(id) {
            const resposne = await api.delete(`/cages/${id}`);
            if (resposne.status === 204){
                this.cages = this.cages.filter(c => c.id != id);
            }

            return resposne;
        }
    },
});
