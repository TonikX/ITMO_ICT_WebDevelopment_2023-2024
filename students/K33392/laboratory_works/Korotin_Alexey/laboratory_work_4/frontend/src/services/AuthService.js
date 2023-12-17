import { useAuthStore } from "@/stores/authStore";
import { api } from "@/boot/axios";

export class AuthService {
    constructor() {
        this.authStore = useAuthStore();
    }

    async login({username, password}) {
        const payload = {
            username: username,
            password: password
        };

        const response = await api.post('/auth/jwt/create', payload);
        if (response.status === 200) {
            this.authStore.accessToken = response.data.access;
            this.authStore.refreshToken = response.data.refresh;
        }

        return response;
    }
}