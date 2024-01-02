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
            return this.staff.slice(
                this.pageSize * (number - 1),
                this.pageSize * number
            );
        },

        getPageCount() {
            const staffSize = this.staff.length;
            return Math.ceil(staffSize / this.pageSize);
        },

        async fetchByUsername(username) {
            let person = this.staff.find((s) => s.username === username);
            if (person === undefined) {
                await this.fetchAll();
                person = this.staff.find((s) => s.username === username);
            }
            return person;
        },

        async delete(username) {
            const staff = await this.fetchByUsername(username);
            const response = await api.delete(`/staff/${staff.id}`);
            if (response.status === 204) {
                this.staff = this.staff.filter((s) => s.username !== username);
            }

            return response;
        },

        async edit(
            payload = {
                id,
                username,
                role,
                passport,
                salary,
                employment_contract_id,
                dismissal_agreement_id,
            },
            id
        ) {
            const response = await api.put(`/staff/${id}`, payload);
            if (response.status === 200) {
                const index = this.staff.findIndex((s) => s.id == id);
                this.staff[index] = response.data;
            }

            return response;
        },
    },
});
