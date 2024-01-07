import { createRouter, createWebHistory } from 'vue-router'
import MainPage from "@/components/MainPage.vue";
import NewsPaperList from "@/components/NewsPaperList.vue";
import NewsPaperDetails from "@/components/NewsPaperDetails.vue";
import NewsPaperEdit from "@/components/NewsPaperEdit.vue";
import NewsPaperCreate from "@/components/NewsPaperCreate.vue";

import PrintingHouseList from "@/components/PrintingHouseList.vue";
import PrintingHouseDetails from "@/components/PrintingHouseDetails.vue";
import PrintingHouseEdit from "@/components/PrintingHouseEdit.vue";
import PrintingHouseCreate from "@/components/PrintingHouseCreate.vue";

import PostOfficeList from "@/components/PostOfficeList.vue";
import PostOfficeDetails from "@/components/PostOfficeDetails.vue";
import PostOfficeEdit from "@/components/PostOfficeEdit.vue";
import PostOfficeCreate from "@/components/PostOfficeCreate.vue";

import NewsPaperPrintList from "@/components/NewsPaperPrintList.vue";
import NewsPaperPrintDetails from "@/components/NewsPaperPrintDetails.vue";
import NewsPaperPrintEdit from "@/components/NewsPaperPrintEdit.vue";
import NewsPaperPrintCreate from "@/components/NewsPaperPrintCreate.vue";

import NewsPaperArrivalList from "@/components/NewsPaperArrivalList.vue";
import NewsPaperArrivalDetails from "@/components/NewsPaperArrivalDetails.vue";
import NewsPaperArrivalEdit from "@/components/NewsPaperArrivalEdit.vue";
import NewsPaperArrivalCreate from "@/components/NewsPaperArrivalCreate.vue";

import NewsPaperOrderList from "@/components/NewsPaperOrderList.vue";
import NewsPaperOrderDetails from "@/components/NewsPaperOrderDetails.vue";
import NewsPaperOrderEdit from "@/components/NewsPaperOrderEdit.vue";
import NewsPaperOrderCreate from "@/components/NewsPaperOrderCreate.vue";

import Auth from "@/components/Auth.vue";
import ErrorPage from "@/components/ErrorPage.vue";
import Registration from "@/components/Registration.vue";
import UserProfile from "@/components/UserProfile.vue";
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '',
      name: 'Auth',
      component: Auth
    },
    {
      path: '/mainpage',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/error',
      name: 'ErrorPage',
      component: ErrorPage
    },
    {
      path: '/registration',
      name: 'Registration',
      component: Registration
    },
    {
      path: '/userprofile',
      name: 'UserProfile',
      component: UserProfile
    },
    {
      path: '/newspapers',
      name: 'NewsPaperList',
      component: NewsPaperList
    },
    {
      path: '/newspapers/:id',
      name: 'NewsPaperDetails',
      component: NewsPaperDetails
    },
    {
      path: '/newspapers/:id/edit',
      name: 'NewsPaperEdit',
      component: NewsPaperEdit,
      props: (route) => ({ newspaper: route.params.newspaper }),

    },
    {
      path: '/newspapers/add',
      name: 'NewsPaperCreate',
      component: NewsPaperCreate
    },
    {
      path: '/printinghouses',
      name: 'PrintingHouseList',
      component: PrintingHouseList
    },
    {
      path: '/printinghouses/:id',
      name: 'PrintingHouseDetails',
      component: PrintingHouseDetails
    },
    {
      path: '/printinghouses/:id/edit',
      name: 'PrintingHouseEdit',
      component: PrintingHouseEdit,
      props: (route) => ({ printinghouse: route.params.printinghouse }),

    },
    {
      path: '/printinghouses/add',
      name: 'PrintingHouseCreate',
      component: PrintingHouseCreate
    },
    {
      path: '/postoffices',
      name: 'PostOfficeList',
      component: PostOfficeList
    },
    {
      path: '/postoffices/:id',
      name: 'PostOfficeDetails',
      component: PostOfficeDetails
    },
    {
      path: '/postoffices/:id/edit',
      name: 'PostOfficeEdit',
      component: PostOfficeEdit,
      props: (route) => ({ postoffices: route.params.postoffices }),

    },
    {
      path: '/postoffices/add',
      name: 'PostOfficeCreate',
      component: PostOfficeCreate
    },
    {
      path: '/newspaperprints',
      name: 'NewsPaperPrintList',
      component: NewsPaperPrintList
    },
    {
      path: '/newspaperprints/:id',
      name: 'NewsPaperPrintDetails',
      component: NewsPaperPrintDetails
    },
    {
      path: '/newspaperprints/:id/edit',
      name: 'NewsPaperPrintEdit',
      component: NewsPaperPrintEdit,
      props: (route) => ({ newspaperprints: route.params.newspaperprints }),

    },
    {
      path: '/newspaperprints/add',
      name: 'NewsPaperPrintCreate',
      component: NewsPaperPrintCreate
    },
    {
      path: '/newspaperarrivals',
      name: 'NewsPaperArrivalList',
      component: NewsPaperArrivalList
    },
    {
      path: '/newspaperarrivals/:id',
      name: 'NewsPaperArrivalDetails',
      component: NewsPaperArrivalDetails
    },
    {
      path: '/newspaperarrivals/:id/edit',
      name: 'NewsPaperArrivalEdit',
      component: NewsPaperArrivalEdit,
      props: (route) => ({ newspaperarrivals: route.params.newspaperarrivals }),

    },
    {
      path: '/newspaperarrivals/add',
      name: 'NewsPaperArrivalCreate',
      component: NewsPaperArrivalCreate
    },
    {
      path: '/newspaperorders',
      name: 'NewsPaperOrderList',
      component: NewsPaperOrderList
    },
    {
      path: '/newspaperorders/:id',
      name: 'NewsPaperOrderDetails',
      component: NewsPaperOrderDetails
    },
    {
      path: '/newspaperorders/:id/edit',
      name: 'NewsPaperOrderEdit',
      component: NewsPaperOrderEdit,
      props: (route) => ({ newspaperorders: route.params.newspaperorders }),

    },
    {
      path: '/newspaperorders/add',
      name: 'NewsPaperOrderCreate',
      component: NewsPaperOrderCreate
    },
  ]
})

export default router
