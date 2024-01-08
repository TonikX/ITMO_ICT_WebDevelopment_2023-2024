<template>
    <mu-container>
        <mu-appbar
            style="width: 100.25vmax; height: 6.2vmax;
            margin-top: -11vh; margin-left: -13.9vh; text-align: left;"
            color="#10df10">Sale_point
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
                    <mu-list-item button @click="goAdmission_point">
                        <mu-list-item-title>Admission_point</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <mu-button large fab slot="right" v-if="!auth" @click="goLogin" class="menu-buttons">LOGIN</mu-button>
            <mu-button large fab slot="right" v-else @click="logout" class="menu-buttons">LOGOUT</mu-button>
        </mu-appbar>
        <mu-paper :z-depth="10" align="center" style="margin: 5vh 0 0 12vmax; width: max-content;">
            <mu-data-table :columns="columns" :sort.sync="sort"
                           @sort-change="handleSortChange" :data="sale_points" style="width: max-content">
                <template slot-scope="scope">
                    <td>{{scope.row.sale_point_name}}</td>
                    <td class="is-center">{{scope.row.sale_point_address}}</td>
                    <td class="is-center">{{scope.row.number_of_stuff}}</td>
                    <td class="is-center">{{scope.row.sale_id}}</td>
                </template>
            </mu-data-table>
        </mu-paper>
        <!--                <mu-col span="4" sm="4" v-if="auth">-->
        <!--                    <ul>-->
        <!--                        <li v-for="sale_point in sale_points">-->
        <!--                            {{sale_point}}-->
        <!--                        </li>-->
        <!--                    </ul>-->
        <!--                </mu-col>-->
    </mu-container>
</template>

<script>
    import Home from "../components/Home"
    import Disks from "../components/Disks"
    import Games from "../components/Games"
    import Sale from "../components/Sale"
    import Admission from "../components/Admission"
    import Admission_point from "../components/Admission_point"

    export default {
        name: "Sale_point",
        data() {
            return {
                sale_points: '', //массив
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Name', name: 'sale_point_name', width: 200, sortable: true},
                    {title: 'Address', name: 'sale_point_address', width: 200, align: 'center', sortable: true},
                    {title: 'Number of stuff', name: 'number_of_stuff', width: 200, align: 'center', sortable: true},
                    {title: 'Sale id', name: 'sale_id', width: 200, align: 'center', sortable: true},
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
            this.loadSale_point()
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
            goAdmission_point() {
                this.$router.push({name: "Admission_point"});
            },
            loadSale_point() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Sale_point/",
                    type: "GET",
                    success: (response) => {
                        this.sale_points = response.data.data
                    }
                })
            },
            handleSortChange({name, order}) {
                this.sale_points = this.sale_points.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
                //сортировка по первой букве
                this.sale_points = this.sale_points.sort((a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
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
