import { defineStore } from "pinia";
import { api } from "@/boot/axios";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        accessToken: null,
        refreshToken: null,
    }),

    getters: {
        isAuthenticated: (state) => !!state.accessToken,
    },
    actions: {
        async login(payload = { username, password }) {
            const response = await api.post("/auth/jwt/create", payload);
            if (response.status === 200) {
                this.accessToken = response.data.access;
                this.refreshToken = response.data.refresh;
            }

            return response;
        },

        async signUp(
            payload = {
                username,
                password,
                re_password,
                passport,
                role,
                salary,
                employment_contract_id
            }
        ) {
            const response = await api.post('/auth/users/', payload); 
            return response;
        },

        logout() {
            this.accessToken = null;
            this.refreshToken = null;
        },
    },
});
