import axios from "axios";

const api = axios.create({
    BaseURL: 'http://localhost:8000/',
    headers: {
        'Content-Type': 'application/json',
    }
});

api.interceptors.request.use(
    config => {
        const token = localStorage.getItem('token');

        if (token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        return config;

    },
    error => {
        return Promise.reject(error);
    }
)

export default api;