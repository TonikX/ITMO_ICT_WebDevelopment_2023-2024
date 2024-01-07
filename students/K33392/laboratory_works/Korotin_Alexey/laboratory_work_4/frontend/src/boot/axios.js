import { boot } from "quasar/wrappers";
import axios from "axios";
import { useAuthStore } from "@/stores/authStore";
import router from "@/router";

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const baseURL = "http://localhost:8000";
const api = axios.create({ baseURL: baseURL });

api.interceptors.request.use((config) => {
    const auth = useAuthStore();
    if (auth.isAuthenticated) {
        config.headers.Authorization = `JWT ${auth.accessToken}`;
    }
    return config;
});

api.interceptors.response.use(
    (r) => r,
    async (error) => {
        const config = error.config;
        const auth = useAuthStore();
        if (error.response.status === 401 && config.retried !== null) {
            auth.refresh();
            config.retried = true;
            return api(error.config);
        }
        if (config.retried) {
            auth.logout();
            const router = router();
            router.push({path: '/auth/login'});
        }



        return error;
    }
);

export default boot(({ app }) => {
    // for use inside Vue files (Options API) through this.$axios and this.$api

    app.config.globalProperties.$axios = axios;
    // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
    //       so you won't necessarily have to import axios in each vue file

    app.config.globalProperties.$api = api;
    // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
    //       so you can easily perform requests against your app's API
});

export { api };
