<template>
    <mu-container>
        <mu-container align="left">
            <mu-appbar
                style="width: 98.75vmax; height: 6.2vmax;
                margin-top: -11vh; margin-left: -13.5vh;"
                color="#10df10">
                Games
                <mu-menu slot="left">
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
                <mu-button large fab slot="right" v-if="!auth" @click="goLogin" class="menu-buttons">LOGIN
                </mu-button>
                <mu-button large fab slot="right" v-else @click="logout" class="menu-buttons">LOGOUT</mu-button>
            </mu-appbar>
            <mu-paper :z-depth="10" align="center" style="margin: 5vh 0 3vmax 12vmax; width: max-content;">
                <mu-data-table :columns="columns" :sort.sync="sort"
                               @sort-change="handleSortChange" :data="games" style="width: max-content;">
                    <template slot-scope="scope">
                        <td @click="openEditDialog(scope.row.name, scope.row.type, scope.row.author, scope.row.disk)" v-if="auth">
                            {{scope.row.name}}
                        </td>
                        <td v-else>{{scope.row.name}}</td>
                        <td class="is-center">{{scope.row.type}}</td>
                        <td class="is-center">{{scope.row.author}}</td>
                        <td class="is-center">{{scope.row.disk}}</td>
                        <mu-container align="left" v-if="auth">
                            <mu-dialog title="Edit" width="500" :open.sync="openEdit">
                                <mu-text-field v-model="editForm.name" type="text"
                                               placeholder="Name"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.type" type="text"placeholder="Type"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.author" type="text" placeholder="Author"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.disk" type="text" placeholder="Disk id"></mu-text-field>
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
                            <mu-form-item prop="input" label="Name">
                                <mu-text-field v-model="form.name"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Type">
                                <mu-text-field v-model="form.type"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Author">
                                <mu-text-field v-model="form.author"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Disk id">
                                <mu-text-field v-model="form.disk"></mu-text-field>
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
    import Disks from "../components/Disks"
    import Sale from "../components/Sale"
    import Admission from "../components/Admission"
    import Sale_point from "../components/Sale_point"
    import Admission_point from "../components/Admission_point"

    export default {
        name: "Games",
        data() {
            return {
                show3: false,
                games: '', //массив
                form: {
                    name: '',
                    type: '',
                    author: '',
                    disk: '',
                },
                editForm: {
                    name: '',
                    type: '',
                    author: '',
                    disk: '',
                },
                openEdit: false,
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Name', name: 'name', width: 200, sortable: true},
                    {title: 'Type', name: 'type', width: 200, align: 'center', sortable: true},
                    {title: 'Author', name: 'author', width: 200, align: 'center', sortable: true},
                    {title: 'Disk id', name: 'disk', width: 200, align: 'center', sortable: true},
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
            this.loadGames()
        },
        methods: {
            openEditDialog(name, type, author, disk) {
                this.editForm.name = name;
                this.editForm.type = type;
                this.editForm.author = author;
                this.editForm.disk = disk;
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
            myadd() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Games/",
                    type: "POST",
                    data: {

                        name: this.form.name,
                        type: this.form.type,
                        author: this.form.author,
                        disk: parseInt(this.form.disk),
                    },
                    success: (response) => {
                        console.log(response.data);
                        alert("Game added!");
                        this.loadGames();
                        this.form = {
                            name: '',
                            type: '',
                            author: '',
                            disk: '',
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
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Games/" + id,
                    type: "PUT",
                    data: {
                        name: this.editForm.name,
                        type: this.editForm.type,
                        author: this.editForm.author,
                        disk: parseInt(this.editForm.disk),
                    },
                    success: (response) => {
                        alert("Game updated!");
                        this.loadGames();
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Error")
                    }
                })
            },
            mydelete(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Games/" + id,
                    type: "DELETE",
                    success: (response) => {
                        alert("Game deleted!");
                        this.loadGames();
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
            goDisks() {
                this.$router.push({name: "Disks"});
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
            loadGames() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Games/",
                    type: "GET",
                    success: (response) => {
                        this.games = response.data.data
                    }
                })
            },
            handleSortChange({name, order}) {
                this.games = this.games.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
                this.games = this.games.sort((a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
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
