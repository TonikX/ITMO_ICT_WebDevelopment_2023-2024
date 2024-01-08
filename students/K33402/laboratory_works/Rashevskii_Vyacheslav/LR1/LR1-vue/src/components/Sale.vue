<template>
    <mu-container>
        <mu-container align="left">
            <mu-appbar
                style="width: 98.75vmax; height: 6.2vmax;
                margin-top: -11vh; margin-left: -13.5vh;"
                color="#10df10">
                Sale
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
                        <mu-list-item button @click="goGames">
                            <mu-list-item-title>Games</mu-list-item-title>
                        </mu-list-item>
                        <mu-list-item button @click="goAdmission">
                            <mu-list-item-title>Admission</mu-list-item-title>
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
                               @sort-change="handleSortChange" :data="sales" style="width: max-content;">
                    <template slot-scope="scope">
                        <td @click="openEditDialog(scope.row.sale_date, scope.row.sale_quantity, scope.row.sale_price, scope.row.disk)">
                            {{scope.row.sale_date}}
                        </td>
                        <td class="is-center">{{scope.row.sale_quantity}}</td>
                        <td class="is-center">{{scope.row.sale_price}}</td>
                        <td class="is-center">{{scope.row.disk}}</td>
                        <mu-container align="left">
                            <mu-dialog title="Edit" width="500" :open.sync="openEdit">
                                <mu-text-field v-model="editForm.date" type="text" placeholder="Date"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.quantity" type="text" placeholder="Quantity"></mu-text-field>
                                <br>
                                <mu-text-field v-model="editForm.price" type="text" placeholder="Price"></mu-text-field>
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
    import Admission from "../components/Admission"
    import Sale_point from "../components/Sale_point"
    import Admission_point from "../components/Admission_point"

    export default {
        name: "Sale",
        data() {
            return {
                show3: false,
                sales: '', //массив
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
                    {title: 'Date', name: 'sale_date', width: 200, sortable: true},
                    {title: 'Quantity', name: 'sale_quantity', width: 200, align: 'center', sortable: true},
                    {title: 'Price', name: 'sale_price', width: 200, align: 'center', sortable: true},
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
            this.loadSale()
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
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Sale/",
                    type: "POST",
                    data: {
                        sale_date: this.form.date,
                        sale_quantity: parseInt(this.form.quantity),
                        sale_price: parseFloat(this.form.price),
                        disk: parseInt(this.form.disk),
                    },
                    success: (response) => {
                        console.log(response.data);
                        alert("Sale added!");
                        this.loadSale();
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
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Sale/" + id,
                    type: "PUT",
                    data: {
                        sale_date: this.editForm.date,
                        sale_quantity: parseInt(this.editForm.quantity),
                        sale_price: parseFloat(this.editForm.price),
                        disk: parseInt(this.editForm.disk),
                    },
                    success: (response) => {
                        alert("Sale updated!");
                        this.loadSale();
                        this.closeEditDialog()
                    },
                    error: (response) => {
                        alert("Error")
                    }
                })
            },
            mydelete(id) {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Sale/" + id,
                    type: "DELETE",
                    success: (response) => {
                        alert("Sale deleted!");
                        this.loadSale();
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
            goAdmission() {
                this.$router.push({name: "Admission"});
            },
            goSale_point() {
                this.$router.push({name: "Sale_point"});
            },
            goAdmission_point() {
                this.$router.push({name: "Admission_point"});
            },
            loadSale() {
                $.ajax({
                    url: "http://127.0.0.1:8000/api/v1/LR1_secondApp/Sale/",
                    type: "GET",
                    success: (response) => {
                        this.sales = response.data.data
                    }
                })
            },
            handleSortChange({name, order}) {
                this.sales = this.sales.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name]);
                this.sales = this.sales.sort((a, b) => order === 'asc' ? a[name].localeCompare(b[name]) : b[name].localeCompare(a[name]));
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
