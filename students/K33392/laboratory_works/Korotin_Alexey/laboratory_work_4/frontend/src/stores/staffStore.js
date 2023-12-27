import { defineStore } from "pinia";
import { api } from "@/boot/axios";

export const useStaffStore = defineStore('staff', {
    state: () => {
        staff: []
    },

    actions: {
        async fetchAll() {
            const response = await api.get('/staff');
            if (response.status === 200) {
                this.staff = response.data;
            }

            return response;
        }
    }
});