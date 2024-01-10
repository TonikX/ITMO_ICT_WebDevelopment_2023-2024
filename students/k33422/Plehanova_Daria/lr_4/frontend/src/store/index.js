// store/index.js
import {createStore} from 'vuex';
import api from '@/api';

const store = createStore({
    state: {
        token: localStorage.getItem('token') || '',
        user: null,
        authStatus: '',
        authError: null
    },
    mutations: {
        setToken(state, token) {
            state.token = token;
        },
        setUser(state, userData) {
            state.user = userData;
        },
        setAuthStatus(state, status) {
            state.authStatus = status;
        },
        setAuthError(state, error) {
            state.authError = error;
        }
    },
    actions: {
        async login({commit}, userCredentials) {
            commit('setAuthStatus', 'loading');
            try {
                const response = await api.post('auth/token/login/', userCredentials);
                const token = response.data.auth_token;
                localStorage.setItem('token', token);
                api.defaults.headers.common['Authorization'] = `Token ${token}`;
                commit('setToken', token);
                commit('setAuthStatus', 'success');
                commit('setAuthError', null);

                const userResponse = await api.get('auth/users/me/');
                commit('setUser', userResponse.data);
            } catch (error) {
                let errorMessage = 'Unknown error';
                if (error.response && error.response.data && error.response.data.non_field_errors) {
                    errorMessage = error.response.data.non_field_errors[0];
                }
                commit('setAuthError', errorMessage);
                commit('setAuthStatus', 'error');
                localStorage.removeItem('token');
            }
        },
        async register({commit, dispatch}, userData) {
            commit('setAuthStatus', 'loading');
            try {
                await api.post('auth/users/', userData);
                dispatch('login', {email: userData.email, password: userData.password});
                commit('setAuthStatus', 'success');
                commit('setAuthError', null);
            } catch (error) {
                let errorMessage = 'Unknown error';
                if (error.response && error.response.data) {
                    if (error.response.data.email && error.response.data.email.length > 0) {
                        errorMessage = error.response.data.email[0];
                    }
                }
                commit('setAuthError', errorMessage);
                commit('setAuthStatus', 'error');
            }
        },
        async logout({commit}) {
            try {
                await api.post('auth/token/logout/');

                localStorage.removeItem('token');
                delete api.defaults.headers.common['Authorization'];
                commit('setToken', '');
                commit('setUser', null);
                commit('setAuthStatus', '');
                commit('setAuthError', null);
            } catch (error) {
                console.error('Ошибка при выходе:', error);
            }
        }
    },
    getters: {
        isAuthenticated: state => !!state.token,
        user: state => state.user,
        authStatus: state => state.authStatus,
        authError: state => state.authError
    }
});

export default store;