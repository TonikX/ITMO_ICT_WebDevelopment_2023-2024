
import {createRouter, createWebHistory} from "vue-router";
import Login from '@/components/Login.vue';
import FoundationList from '@/components/FoundationList.vue';
import CardList from '@/components/CardList.vue';
import CardDetail from '@/components/CardDetail.vue';
import CardCreate from '@/components/CardCreate.vue';
import ItemCreate from '@/components/ItemCreate.vue';
import AnimalFacts from '@/components/Facts.vue';

const routes = [
   {
       path: '/login',
       name: 'login',
       component: Login
   },
   {
       path: '/facts',
       name: 'facts',
       component: AnimalFacts
   },
   {   path: '/foundations',
       name: 'FoundationList',
       component: FoundationList
   },
   {   path: '/foundations/:fond_id',
       name: 'CardList',
       component: CardList,
       props: true
   },
   {
      path: '/foundations/:fond_id/cards/create/',
      name: 'CardCreate',
      component: CardCreate,
   },
   {
       path: '/cards/:id',
       name: 'CardDetail',
       component: CardDetail,
       props: true,
   },
   {
       path: '/items/create',
       name: 'ItemCreate',
       component: ItemCreate,
   },
]

const router = createRouter({
   history: createWebHistory(), routes
})

export default router
