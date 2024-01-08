<template>
    <mu-container>
        <mu-container align="left">
            <mu-appbar
                style="width: 98.75vmax; height: 6.2vmax;
        margin-top: -11vh; margin-left: -13.5vh;"
                color="#10df10">
                Admission
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
                        <mu-list-item button @click="goSale_point">
                            <mu-list-item-title>Sale_point</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button @click="goAdmission_point">
                            <mu-list-item-title>Admission_point</mu-list-item-title>
                        </mu-list-item>
                    </mu-list>
                </mu-menu>
                <mu-button large fab slot="right" v-if="!auth" @click="goLogin" class="menu-buttons">LOGIN</mu-button>
                <mu-button large fab slot="right" v-else @click="logout" class="menu-buttons">LOGOUT</mu-button>
            </mu-appbar>
            <mu-paper :z-depth="10" align="center" style="margin: 5vh 0 3vmax 12vmax; width: max-content;">
                <mu-data-table :columns="columns" :sort.sync="sort"
                               @sort-change="handleSortChange" :data="admissions" style="width: max-content">
                    <template slot-scope="scope">
                        <td @click="openEditDialog(scope.row.admission_date, scope.row.admission_quantity, scope.row.admission_price, scope.row.disk)">
                            {{scope.row.admission_date}}
                        </td>
                        <td class="is-center">{{scope.row.admission_quantity}}</td>
                        <td class="is-center">{{scope.row.admission_price}}</td>
                        <td class="is-center">{{scope.row.disk}}</td>
                        <mu-container align="left">
                            <mu-dialog title="Edit" width="500" :open.sync="openEdit">
                                <mu-text-field v-model="editForm.date" type="text" placeholder="Date"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.quantity" type="text"
                                               placeholder="Quantity"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.price" type="text" placeholder="Price"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.disk" type="text"
                                               placeholder="Disk id"></mu-text-field>
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
        <mu-container align="left">
            <mu-button @click="show3 = !show3">New record</mu-button>
            <mu-flex class="mu-transition-row">
                <mu-expand-transition>
                    <mu-container v-show="show3">
                        <mu-form :model="form" :label-position="top" label-width="100">
                            <mu-form-item prop="input" label="Date">
                                <mu-text-field v-model="form.date" placeholder="YYYY-MM-DD"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Quantity">
                                <mu-text-field v-model="form.quantity"></mu-text-field>
                            </mu-form-item>
                            <mu-form-item prop="input" label="Price">
                                <mu-text-field v-model="form.price"></mu-text-field>
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
    import Games from "../components/Games"
    import Sale from "../components/Sale"
    import Sale_point from "../components/Sale_point"
    import Admission_point from "../components/Admission_point"

    export default {
        name: "Admission",
        data() {
            return {
                show3: false,
                admissions: '',
                form: {
                    date: '',
                    quantity: '',
                    price: '',
                    disk: '',
                },
                editForm: {
                    date: '',
                    quantity: '',
                    price: '',
                    disk: '',
                },
                openEdit: false,
                sort: {
                    name: '',
                    order: 'asc'
                },
                columns: [
                    {title: 'Date', name: 'admission_date', width: 200, sortable: true},
                    {title: 'Quantity', name: 'admission_quantity', width: 200, align: 'center', sortable: true},
                    {title: 'Price', name: 'admission_price', width: 200, align: 'center', sortable: true},
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
            $.ajaxSetup({
                headers: {'Authorization': "Token " + sessionStorage.getItem('auth_token')},
            });
            this.loadAdmission()
        },
        methods: {
            openEditDialog(date, quantity, price, disk) {
                this.editForm.date = date;
                this.editForm.quantity = quantity;
                this.editForm.price = price;
                this.editForm.disk = disk;
                this.openEdit = true
            },
            closeEditDialog() {
                this.openEdit = false;
            },
            myadd() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Admission/",
                    type: "POST",
                    data: {
                        admission_date: this.form.date,
                        admission_quantity: parseInt(this.form.quantity),
                        disk: parseInt(this.form.disk),
                        admission_price: parseFloat(this.form.price),
                    },
                    success: (response) => {
                        console.log(response.data);
                        alert("Admission added!");
                        this.loadAdmission();
                        this.form = {
                            date: '',
                            quantity: '',
                            price: '',
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
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Admission/" + id,
                    type: "PUT",
                    data: {
                        admission_date: this.editForm.date,
                        admission_quantity: parseInt(this.editForm.quantity),
                        disk: parseInt(this.editForm.disk),
                        admission_price: parseFloat(this.editForm.price),
                    },
                    success: (response) => {
                        alert("Admission updated!");
                        this.loadAdmission();
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Error")
                    }
                })
            },
            mydelete(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Admission/" + id,
                    type: "DELETE",
                    success: (response) => {
                        alert("Admission deleted!");
                        this.loadAdmission();
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
            goGames() {
                this.$router.push({name: "Games"});
            },
            goSale() {
                this.$router.push({name: "Sale"});
            },
            goSale_point() {
                this.$router.push({name: "Sale_point"});
            },
            goAdmission_point() {
                this.$router.push({name: "Admission_point"});
            },
            loadAdmission() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Admission/",
                    type: "GET",
                    success: (response) => {
                        this.admissions = response.data.data
                    }
                })
            },
            handleSortChange({name, order}) {
                this.admissions = this.admissions.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
                this.admissions = this.admissions.sort((a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
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
