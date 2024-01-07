<template>
    <div class="container q-pa-md column flex-center bg-primary">
        <p class="text-h3">Sign up</p>
        <q-form ref="form" @submit.prevent="trySignUp" class="login-container q-gutter-y-md column">
            <q-input label-color="white" input-class="input-field" type="text" v-model="form.username" label="Login"
                placeholder="example@example.com" error-message="Please enter a valid email"
                :rules="[val => isValidEmail(val) || 'Invalid email address']" />
            <q-input label-color="white" input-class="input-field" v-model="form.passport" label="Passport"
                placeholder="1234567890" mask="#### ######" />
            <q-input label-color="white" input-class="input-field" v-model="form.salary" type="number" label="Salary"
                placeholder="10000" />
            <q-input label-color="white" input-class="input-field" type="password" v-model="form.password" label="Password"
                error-message="Should be at least 6 characters" :rules="[() => isValidPassword]" />
            <q-input label-color="white" input-class="input-field" type="password" v-model="form.re_password"
                label="Repeat password" error-message="Passwords don't match" :rules="[() => passwordsMatch]" />
            <q-input label-color="white" input-class="input-field" v-model="form.employment_contract_id"
                label="Employment contract number" placeholder="1" type="number" />
            <div class="">
                <q-radio v-model="form.role" val="W" checked-icon="task_alt" unchecked-icon="panorama_fish_eye"
                    label="Worker" color="white" keep-color />
                <q-radio v-model="form.role" val="D" checked-icon="task_alt" unchecked-icon="panorama_fish_eye"
                    label="Director" color="white" keep-color />
            </div>
            <q-btn text-color="primary" type="submit" color="secondary">Sign up</q-btn>
            <p class="text-subtitle1">Alreay have an account? <router-link to="/auth/login">Log in</router-link></p>
        </q-form>
    </div>
</template>
<script>
import { emailValidator } from '@/mixins/email';
import { mapActions, mapState } from 'pinia';
import { Notify } from 'quasar';
import { useAuthStore } from '@/stores/authStore';

export default {

    mixins: [emailValidator],

    data() {
        return {
            form: {
                username: '',
                passport: '',
                role: 'W',
                employment_contract_id: 0,
                salary: 0,
                password: '',
                re_password: ''
            }
        }
    },

    computed: {
        passwordsMatch() { return this.form.password === this.form.re_password; },
        isValidPassword() { return this.form.password.length >= 8; }
    },

    methods: {
        ...mapActions(useAuthStore, ['signUp', 'login']),

        async trySignUp() {
            const response = await this.signUp(this.form);

            if (response.status === 201) {
                const response = await this.login(this.form);

                if (response.status === 200) {
                    this.$router.push('/facilities');
                }
            }
        }
    },
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
    font-size: 20px;
    color: $text;
}
</style>