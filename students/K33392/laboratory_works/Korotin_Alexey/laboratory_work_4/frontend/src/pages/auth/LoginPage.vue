
import { pushScopeId } from 'vue';

import router from '@/router';
<template>
    <q-page>
        <div class="container q-pa-md column flex-center bg-primary">
            <p class="text-h3">Login</p>
            <q-form ref="form" @submit.prevent="tryLogin" class="login-container q-gutter-y-md column">
                <q-input label-color="white" input-class="input-field" type="text" v-model="form.username" label="Login"
                    placeholder="example@example.com" error-message="Please enter a valid email"
                    ></q-input>
                <q-input label-color="white" input-class="input-field" type="password" v-model="form.password"
                    label="Password"></q-input>
                <q-btn text-color="primary" type="submit" color="secondary">Login</q-btn>
                <p class="text-subtitle1">Don't have an account? <router-link to="/auth/register">Sign up</router-link></p>
            </q-form>
        </div>
    </q-page>
</template>
<script>
import { emailValidator } from '@/mixins/email';
import { AuthService } from '@/services/AuthService';
export default {
    mixins: [emailValidator],
    data() {
        return {
            form: {
                username: null,
                password: null
            }
        }
    },

    methods: {
        async tryLogin() {
            const service = new AuthService();
            const response = await service.login(this.form);

            if (response.status === 200) {
                this.$router.push('/');
            }
        }
    }
}
</script>
<style lang="scss">
@import '@/css/quasar.variables.scss';

.container {
    color: $text;
    height: 100vh;
}

.login-container {
    width: 70%;
    max-width: 500px;
}

.input-field {
    font-size: 20px !important;
    color: $text !important;
    appearance: textfield;
}
</style>