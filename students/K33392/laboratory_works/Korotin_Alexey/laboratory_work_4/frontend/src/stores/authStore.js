import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
    state: () => ({
        accessToken: null,
        refreshToken: null
    }),
    
    getters: {
        isAuthenticated: (state) => !!state.accessToken
    }
});
