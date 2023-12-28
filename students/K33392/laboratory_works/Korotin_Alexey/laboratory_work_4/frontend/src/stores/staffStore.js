import { defineStore } from "pinia";
import { api } from "@/boot/axios";

export const useStaffStore = defineStore("staff", {
    state: () => ({
        staff: [],
        pageSize: 5,
    }),
    actions: {
        async fetchAll() {
            const response = await api.get("/staff");
            if (response.status === 200) {
                this.staff = response.data;
            }

            return response;
        },

        getPage(number) {
            return this.staff.slice(this.pageSize * (number - 1), this.pageSize * number);
        },

        getPageCount() {
            const staffSize = this.staff.length;
            return Math.ceil(staffSize / this.pageSize);
        },
    },
});
