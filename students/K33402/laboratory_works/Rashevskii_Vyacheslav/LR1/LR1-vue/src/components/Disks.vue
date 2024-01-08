<template>
    <mu-container>
        <mu-container align="left">
            <mu-appbar
                style="width: 98.75vmax; height: 6.2vmax;
                margin-top: -11vh; margin-left: -13.5vh;"
                color="#10df10">
                Disks
                <mu-menu slot="left">
                    <mu-button large fab value="menu" class="menu-buttons">
                        <mu-icon value="menu"></mu-icon>
                    </mu-button>
                    <mu-list slot="content">
                        <mu-list-item button @click="goHome">
                            <mu-list-item-title>Home</mu-list-item-title>
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
            <mu-paper :z-depth="10" align="center" style="margin: 5vh 0 3vmax 20vmax; width: max-content;">
                <mu-data-table :columns="columns" :sort.sync="sort"
                               @sort-change="handleSortChange" :data="disks" style="width: max-content">
                    <template slot-scope="scope">
                        <td @click="openEditDialog(scope.row.id, scope.row.prod_date, scope.row.firm)" v-if="auth">
                            {{scope.row.id}}
                        </td>
                        <td v-else>{{scope.row.id}}</td>
                        <td>{{scope.row.prod_date}}</td>
                        <td class="is-center">{{scope.row.firm}}</td>
                        <mu-container align="left">
                            <mu-dialog title="Edit" width="500" :open.sync="openEdit">
                                <mu-text-field v-model="editForm.dateV" type="text" placeholder="Date"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.firmV" type="text" placeholder="Firm"></mu-text-field>
                                <br>
                                <mu-button slot="actions" color="green" @click="myupdate(scope.row.id)">Save
                                </mu-button>
                                <mu-button slot="actions" color="red" @click="mydelete(scope.row.id)">Delete
                                </mu-button>
                                <mu-button slot="actions" color="primary" @click="closeEditDialog">Close</mu-button>
                            </mu-dialog>
                        </mu-container>
                    </template>
                </mu-data-table>
            </mu-paper>
        </mu-container>
        <mu-container align="left" v-if="auth">
            <mu-button @click="show3 = !show3">New record</mu-button>
            <mu-flex class="mu-transition-row">
                <mu-expand-transition>
                    <mu-container v-show="show3">
                        <mu-form :model="form" :label-position="top" label-width="100">
                            <mu-form-item prop="input" label="Date">
                                <mu-text-field v-model="form.dateV" placeholder="YYYY-MM-DD"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Firm">
                                <mu-text-field v-model="form.firmV"></mu-text-field>
                            </mu-form-item>
                        </mu-form>
                        <mu-button color="green" @click="myadd">Add</mu-button>
                    </mu-container>
                </mu-expand-transition>
            </mu-flex>
        </mu-container>
        <mu-container style="height: 5vh"></mu-container>
    </mu-container>
</template>

<script>
    import Home from "../components/Home"
    import Games from "../components/Games"
    import Sale from "../components/Sale"
    import Admission from "../components/Admission"
    import Sale_point from "../components/Sale_point"
    import Admission_point from "../components/Admission_point"

    export default {
        name: "Disks",
        data() {
            return {
                disks: '', //массив
                show3: false,
                form: {
                    dateV: '',
                    firmV: '',
                },
                editForm: {
                    dateV: '',
                    firmV: '',
                },
                openEdit: false,
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Id', name: 'id', width: 200, sortable: true},
                    {title: 'Date', name: 'prod_date', width: 200, sortable: true},
                    {title: 'Firm', name: 'firm', width: 200, align: 'center', sortable: true},
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
            this.loadDisks()
        },
        methods: {
            openEditDialog(id, date, firm) {
                this.editForm.dateV = date;
                this.editForm.firmV = firm;
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
            myadd() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Disks/",
                    type: "POST",
                    data: {
                        prod_date: this.form.dateV,
                        firm: this.form.firmV,
                    },
                    success: (response) => {
                        console.log(response.data);
                        alert("Disk added!");
                        this.loadDisks();
                        this.form = {
                            dateV: '',
                            firmV: '',
                        };
                    },
                    error: (response) => {
                        console.log(response.data);
                        alert("Error!")
                    }
                })
            },
            myupdate(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Disks/" + id,
                    type: "PUT",
                    data: {
                        // id: this.editForm.idV,
                        prod_date: this.editForm.dateV,
                        firm: this.editForm.firmV,
                    },
                    success: (response) => {
                        alert("Disk updated!");
                        this.loadDisks();
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Error")
                    }
                })
            },
            mydelete(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Disks/" + id,
                    type: "DELETE",
                    success: (response) => {
                        alert("Disk deleted!");
                        this.loadDisks();
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Error")
                    }
                })
            },
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
            loadDisks() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Disks/",
                    type: "GET",
                    success: (response) => {
                        this.disks = response.data.data
                    }
                })
            },
            handleSortChange({name, order}) {
                this.disks = this.disks.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
                this.disks = this.disks.sort((a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
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
