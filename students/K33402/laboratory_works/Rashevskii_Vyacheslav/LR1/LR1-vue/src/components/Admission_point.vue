<template>
    <mu-container>
        <mu-appbar
            style="width: 98.7vmax; height: 6.2vmax;
            margin-top: -11vh; margin-left: -12vh; text-align: left;"
            color="#10df10">
            Admission_point
            <mu-menu slot="left" v-if="auth">
                <mu-button large fab value="menu" class="menu-buttons">
                    <mu-icon value="menu"></mu-icon>
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button @click="goHome">
                        <mu-list-item-title>Home</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goDisks">
                        <mu-list-item-title>Disks</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goGames">
                        <mu-list-item-title>Games</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goSale">
                        <mu-list-item-title>Sale</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goAdmission">
                        <mu-list-item-title>Admission</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goSale_point">
                        <mu-list-item-title>Sale_point</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <mu-button large fab slot="right" v-if="!auth" @click="goLogin" class="menu-buttons">LOGIN</mu-button>
            <mu-button large fab slot="right" v-else @click="logout" class="menu-buttons">LOGOUT</mu-button>
        </mu-appbar>
        <mu-paper :z-depth="10" align="center" style="margin: 5vh 0 5vmax 13vmax; width: max-content;">
            <mu-data-table :columns="columns" :sort.sync="sort"
                           @sort-change="handleSortChange" :data="admission_points" style="width: max-content">
                <template slot-scope="scope">
                    <td>{{scope.row.admission_point_name}}</td>
                    <td class="is-center">{{scope.row.admission_point_address}}</td>
                    <td class="is-center">{{scope.row.number_of_stuff}}</td>
                    <td class="is-center">{{scope.row.admission_id}}</td>
                </template>
            </mu-data-table>
        </mu-paper>
    </mu-container>
</template>

<script>
    import Home from "../components/Home"
    import Disks from "../components/Disks"
    import Games from "../components/Games"
    import Sale from "../components/Sale"
    import Admission from "../components/Admission"
    import Sale_point from "../components/Sale_point"

    export default {
        name: "Admission_point",
        data() {
            return {
                admission_points: '', //массив
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Name', name: 'admission_point_name', width: 200, sortable: true},
                    {title: 'Address', name: 'admission_point_address', width: 200, align: 'center', sortable: true},
                    {title: 'Number of stuff', name: 'number_of_stuff', width: 200, align: 'center', sortable: true},
                    {title: 'Admission id', name: 'admission_id', width: 200, align: 'center', sortable: true},
                ],
            }
        },
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        created() {
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadAdmission_point()
        },
        methods: {
            goLogin() {
                this.$router.push({name: "Login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token");
                window.location = "/" //костыль
            },
            goHome() {
                this.$router.push({name: "Home"});
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
            loadAdmission_point() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Admission_point/",
                    type: "GET",
                    success: (response) => {
                        this.admission_points = response.data.data
                    }
                })
            },
            handleSortChange({name, order}) {
                this.admission_points = this.admission_points.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
                this.admission_points = this.admission_points.sort((a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
            },
        }
    }
</script>

<style scoped>
    .menu-buttons {
        box-shadow: 0 0 15px white;
        background-color: #10df10;
        margin-top: 1vh;
    }
</style>
