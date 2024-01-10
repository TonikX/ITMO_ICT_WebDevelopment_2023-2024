# Роутер

### Импорты
```
import { createRouter, createWebHistory } from 'vue-router'
import Login from "@/components/LoginPage.vue";
import RegisterPage from "@/components/RegisterPage.vue";
import NewspaperList from "@/components/Newspaper/NewspaperList.vue";
import AddNewspaper from "@/components/Newspaper/AddNewspaper.vue";
import NewsPaperPage from "@/components/Newspaper/NewsPaperPage.vue";
import PostOffices from "@/components/PostOffice/PostOffices.vue";
import AddPostOffice from "@/components/PostOffice/AddPostOffice.vue";
import PostOfficePage from "@/components/PostOffice/PostOfficePage.vue";
import OrderList from "@/components/OrderingNewspaper/OrderList.vue";
import AddOrder from "@/components/OrderingNewspaper/AddOrder.vue";
import OrderPage from "@/components/OrderingNewspaper/OrderPage.vue";
import PrinterList from "@/components/Printer/PrinterList.vue";
import AddPrinter from "@/components/Printer/AddPrinter.vue";
import PrinterPage from "@/components/Printer/PrinterPage.vue";
import PrintingList from "@/components/Printing/PrintingList.vue";
import AddPrinting from "@/components/Printing/AddPrinting.vue";
import PrintingPage from "@/components/Printing/PrintingPage.vue";
import TransportingList from "@/components/Transporting/TransportingList.vue";
import AddTransporting from "@/components/Transporting/AddTransporting.vue";
import TransportingPage from "@/components/Transporting/TransportingPage.vue";
import FindAddress from "@/components/Printer/FindAddress.vue";
import FindPrice from "@/components/Newspaper/FindPrice.vue";
import WhereSells from "@/components/Printing/WhereSells.vue";
import LostDelivers from "@/components/Transporting/LostDelivers.vue";
import ReportPage from "@/components/Printer/ReportPage.vue";
```

### Непосредственно роуетр
```
const routes =[
    {path: '/login', component: Login},
    {path: '/register', component: RegisterPage},
    {path: '/newspapers', component: NewspaperList},
    {path: '/add-newspaper', component: AddNewspaper},
    {path: '/newspapers/:id', component: NewsPaperPage},
    {path: '/post-offices', component: PostOffices},
    {path: '/add-post-office', component: AddPostOffice},
    {path: '/post-offices/:id', component: PostOfficePage},
    {path: '/orders', component: OrderList},
    {path: '/add-order', component: AddOrder},
    {path: '/orders/:id', component: OrderPage},
    {path: '/printers', component: PrinterList},
    {path: '/add-printer', component: AddPrinter},
    {path: '/printers/:id', component: PrinterPage},
    {path: '/printing', component: PrintingList},
    {path: '/add-printing', component: AddPrinting},
    {path: '/printing/:id', component: PrintingPage},
    {path: '/transporting', component: TransportingList},
    {path: '/add-transporting', component: AddTransporting},
    {path: '/transporting/:id', component: TransportingPage},
    {path: '/printers/:id/report', component: ReportPage},
    {path: '/find-address', component: FindAddress},
    {path: '/find-price', component: FindPrice},
    {path: '/find-where', component: WhereSells},
    {path: '/lost-delivers', component: LostDelivers},

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
```
