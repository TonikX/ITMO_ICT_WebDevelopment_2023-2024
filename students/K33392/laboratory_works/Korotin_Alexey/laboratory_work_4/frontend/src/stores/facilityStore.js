import { defineStore } from "pinia";
import { api } from "@/boot/axios";

export const useFacilityStore = defineStore("facility", {
    state: () => ({
        facilities: [],
    }),

    actions: {
        async fetchAll() {
            const response = await api.get("/facilities/");
            this.facilities = response.data;
            return response;
        },

        async create(payload = { name, _longitude, _latitude }) {
            const response = await api.post("/facilities/", payload);
            this.facilities.push(response.data);
            return response;
        },

        async delete(id) {
            const response = await api.delete(`/facilities/${id}`);
            this.facilities = this.facilities.filter((f) => f.id != id);
            return response;
        }
    },
});
