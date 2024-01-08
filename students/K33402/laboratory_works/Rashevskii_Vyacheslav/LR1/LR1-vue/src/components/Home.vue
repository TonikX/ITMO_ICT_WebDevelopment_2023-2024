<template>
    <mu-container>
        <mu-appbar
            style="width: 100.25vmax; height: 6.2vmax; margin-top: -11vh; margin-left: -13.9vh; text-align: left" color="#10df10">
            Home
            <mu-menu slot="left">
                <mu-button large fab value="menu" class="menu-buttons">
                    <mu-icon value="menu"></mu-icon>
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button @click="goDisks">
                        <mu-list-item-title>Disks</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goGames">
                        <mu-list-item-title>Games</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goSale" v-if="auth">
                        <mu-list-item-title>Sale</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goAdmission" v-if="auth">
                        <mu-list-item-title>Admission</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goSale_point" v-if="auth">
                        <mu-list-item-title>Sale_point</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goAdmission_point" v-if="auth">
                        <mu-list-item-title>Admission_point</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <mu-button large fab slot="right" v-if="!auth" @click="goLogin" class="menu-buttons">LOGIN</mu-button>
            <mu-button large fab slot="right" v-else @click="logout" class="menu-buttons">LOGOUT</mu-button>
        </mu-appbar>
        <mu-container style="font-size: 24px">
            <br>
            Registered users can view all tables and edit the following: Disks, Games, Sale, Login.
            <br>
            Not registered users can only view tables: Disks, Games.
            <br><br><br>
            Зарегистрированные пользователи могут просматривать все таблицы и редактировать следующие: Disks, Games,
            Sale, Admission.
            <br>
            Не зарегистрированные пользователи могут только просматривать таблицы: Disks, Games.
        </mu-container>
    </mu-container>
</template>

<script>
    export default {
        name: "Home",
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "Login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token");
                window.location = "/" //костыль
            },
            goDisks() {
                this.$router.push({name: "Disks"});
            },
            goGames() {
                this.$router.push({name: "Games"});
            },
            goSale() {
                this.$router.push({name: "Sale"});
            },
            goAdmission() {
                this.$router.push({name: "Admission"});
            },
            goSale_point() {
                this.$router.push({name: "Sale_point"});
            },
            goAdmission_point() {
                this.$router.push({name: "Admission_point"});
            },
        },
    }
</script>

<style scoped>
    .menu-buttons {
        box-shadow: 0 0 15px white;
        background-color: #10df10;
        margin-top: 1vh;
    }
</style>
