import Login from "@/components/Login.vue";
import Register from "@/components/Register.vue";
import CollectiveAgreement from "@/components/CollectiveAgreement.vue";
import IndividAgreement from "@/components/IndividAgreement.vue";
import CollectiveInsurance from "@/components/CollectiveInsurance.vue";
import IndividInsurance from "@/components/IndividInsurance.vue";
import Companies from "@/components/Companies.vue";
import Employees from "@/components/Employees.vue";
import Agents from "@/components/Agents.vue";
import CreateAgent from "@/components/CreateAgent.vue";
import CreateInsurance from "@/components/CreateInsurance.vue";
import CreateCompany from "@/components/CreateCompany.vue";
import CreateEmployee from "@/components/CreateEmployee.vue";
import CreateCollectiveAgreement from "@/components/CreateCollectiveAgreement.vue";
import {createRouter, createWebHistory} from "vue-router";

const routes = [  // массив с роутами
   // отдельный роут:
   {
      path: '/login', // конкретный url-адрес
      component: Login // Ссылка на компонент
   },
   {
      path: '/register', // конкретный url-адрес
      component: Register // Ссылка на компонент
   },
   {
      path: '/collective',
      component: CollectiveAgreement
   },
   {
      path: '/individual',
      component: IndividAgreement
   },
   {
      path: '/collective-agreement/:insid?',
      component: CollectiveInsurance
   },
      {
      path: '/individual-agreement/:insid?',
      component: IndividInsurance
   },
   {
      path: '/companies',
      component: Companies
   },
   {
      path: '/company-employees/:compid?',
      component: Employees
   },
   {
      path: '/agents/',
      component: Agents
   },
   {
      path: '/agent/:compid?',
      component: CreateAgent
   },
      {
      path: '/agent/create',
      component: CreateAgent
   },
   {
      path: '/company/:compid?',
      component: CreateCompany
   },
   {
      path: '/company/create',
      component: CreateCompany
   },
      {
      path: '/collective-agreement-crud/:compid?',
      component: CreateCollectiveAgreement
   },
   {
      path: '/collective-agreement-crud/create',
      component: CreateCollectiveAgreement
   },
   {
      path: '/employee/:compid?',
      component: CreateEmployee
   },
   {
      path: '/insurance/:compid?',
      component: CreateInsurance
   }
]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router // экспортируем сконфигурированный роутер