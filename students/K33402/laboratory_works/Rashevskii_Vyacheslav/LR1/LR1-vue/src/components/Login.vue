<template>
    <div>
        <input v-model="login" type="text" placeholder="Email or login"/>
        <input v-model="password" type="password" placeholder="Password"/>
        <button @click="setLogin">Login</button>
    </div>
</template>

<script>
    import $ from 'jquery'

    export default {
        name: "Login",
        data() {
            return {
                login: '',
                password: '',
            }
        },
        methods: {
            setLogin() {
                $.ajax({
                    url: "http://127.0.0.1:8000/auth/token/login/",
                    type: "POST",
                    data: {
                        username: this.login,
                        password: this.password,
                    },
                    success: (response) => {
                        alert("Success!")
                        sessionStorage.setItem("auth_token", response.data.attributes.auth_token)
                        this.$router.push({name: "Home"})
                    },
                    error: (response) => {
                        if (response.status === 400) {
                            alert("Login or password is incorrect")
                        }
                    },
                })
            },
        }
    }
</script>

<style scoped>

</style>
