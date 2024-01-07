import { defineStore } from "pinia";
import { useCageStore } from "./cageStore";
import { api } from "@/boot/axios";

const embedCages = async (chicken) => {
    const cageStore = useCageStore();
    await chicken.forEach(async (c) => c.cage = await cageStore.fetchById(c.cage));

    return chicken;
}

export const useChickenStore = defineStore('chicken', {
    state: () => ({
        chicken: []
    }),

    actions: {
        async fetchAll() {
            const response = await api.get('/chickens');
            if (response.status === 200) {
                this.chicken = await embedCages(response.data);
            }
            return response;
        },

        async fetchById(id) {
            let chicken = this.chicken.find(c => c.id == id);
            if (chicken === undefined) {
                await this.fetchAll();
                chicken = this.chicken.find(c => c.id == id);
            }

            return chicken;
        },

        async create(payload = {weight, birth_date, monthly_egg_rate, cage}) {
            const response = await api.post('/chickens/', payload);

            if (response.status === 201) {
                await this.fetchAll();
            }

            return response;
        },

        async delete(id) {
            const response = await api.delete(`/chickens/${id}`);
            if (response.status === 204) {
                this.chicken = this.chicken.filter(c => c.id != id);
            }

            return response;
        },

        async edit(payload = {weight, birth_date, monthly_egg_rate, cage}, id) {
            const response = await api.put(`/chickens/${id}`, payload);
            if (response.status === 200) {
                const index = this.chicken.findIndex(c => c.id == id);
                this.chicken[index] = response.data;
            }

            return response;
        }
    }
})