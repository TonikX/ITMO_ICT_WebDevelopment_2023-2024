import { createRouter, createWebHistory } from 'vue-router'
import Login from "@/components/LoginPage.vue";
import RegisterPage from "@/components/RegisterPage.vue";
import AddAviary from "@/components/Aviary/AddAviary.vue";
import AviaryList from "@/components/Aviary/AviaryList.vue";
import AviaryPage from "@/components/Aviary/AviaryPage.vue";
import AddLocation from "@/components/Location/AddLocation.vue";
import LocationList from "@/components/Location/LocationList.vue";
import LocationPage from "@/components/Location/LocationPage.vue";
import AddTOD from "@/components/TypeOfDiet/AddTOD.vue";
import TODList from "@/components/TypeOfDiet/TODList.vue";
import TODPage from "@/components/TypeOfDiet/TODPage.vue";
import ZooList from "@/components/Zoo/ZooList.vue";
import AddZoo from "@/components/Zoo/AddZoo.vue";
import ZooPage from "@/components/Zoo/ZooPage.vue";
import DietList from "@/components/Diet/DietList.vue";
import AddDiet from "@/components/Diet/AddDiet.vue";
import DietPage from "@/components/Diet/DietPage.vue";
import HabitatList from "@/components/Habitat/HabitatList.vue";
import HabitatPage from "@/components/Habitat/HabitatPage.vue";
import AddHabitat from "@/components/Habitat/AddHabitat.vue";
import AnimalList from "@/components/Animal/AnimalList.vue";
import AnimalPage from "@/components/Animal/AnimalPage.vue";
import AddAnimal from "@/components/Animal/AddAnimal.vue";
import AddWP from "@/components/WinterPlace/AddWP.vue";
import WPList from "@/components/WinterPlace/WPList.vue";
import WPPage from "@/components/WinterPlace/WPPage.vue";
import OwningList from "@/components/Owning/OwningList.vue";
import OwningPage from "@/components/Owning/OwningPage.vue";
import AddOwning from "@/components/Owning/AddOwning.vue";
import AddAIA from "@/components/AnimalInAviary/AddAIA.vue";
import AIAList from "@/components/AnimalInAviary/AIAList.vue";
import AIAPage from "@/components/AnimalInAviary/AIAPage.vue";
import WorkerList from "@/components/Worker/WorkerList.vue";
import WorkerPage from "@/components/Worker/WorkerPage.vue";
import AddWorker from "@/components/Worker/AddWorker.vue";
import AnumalsInCommunas from "@/components/AnimalInAviary/AnumalsInCommunas.vue";
import InSame from "@/components/Animal/InSame.vue";
import InLease from "@/components/Owning/InLease.vue";
import ShowEmpty from "@/components/Aviary/ShowEmpty.vue";
import AnimalsIn from "@/components/Location/AnimalsIn.vue";


const routes =[
    {path: '/login', component: Login},
    {path: '/register', component: RegisterPage},
    {path: '/add-aviary', component: AddAviary},
    {path: '/aviarys', component: AviaryList},
    {path: '/aviarys/:id', component: AviaryPage},
    {path: '/empty', component: ShowEmpty},
    {path: '/add-location', component: AddLocation},
    {path: '/locations', component: LocationList},
    {path: '/locations/:id', component: LocationPage},
    {path: '/locations/:id/in', component: AnimalsIn},
    {path: '/add-zoo', component: AddZoo},
    {path: '/zoos', component: ZooList},
    {path: '/zoos/:id', component: ZooPage},
    {path: '/add-food', component: AddTOD},
    {path: '/foods', component: TODList},
    {path: '/foods/:id', component: TODPage},
    {path: '/add-diet', component: AddDiet},
    {path: '/diets', component: DietList},
    {path: '/diets/:id', component: DietPage},
    {path: '/add-habitat', component: AddHabitat},
    {path: '/habitats', component: HabitatList},
    {path: '/habitats/:id', component: HabitatPage},
    {path: '/add-animal', component: AddAnimal},
    {path: '/animals', component: AnimalList},
    {path: '/animals/:id', component: AnimalPage},
    {path: '/animals/:id/neighbours', component: InSame},
    {path: '/add-winter-place', component: AddWP},
    {path: '/winter-places', component: WPList},
    {path: '/winter-places/:id', component: WPPage},
    {path: '/add-owning', component: AddOwning},
    {path: '/ownings', component: OwningList},
    {path: '/in-lease', component: InLease},
    {path: '/ownings/:id', component: OwningPage},
    {path: '/add-who-is-there', component: AddAIA},
    {path: '/who-is-theres', component: AIAList},
    {path: '/who-is-theres/:id', component: AIAPage},
    {path: '/list-communas', component: AnumalsInCommunas},
    {path: '/add-worker', component: AddWorker},
    {path: '/workers', component: WorkerList},
    {path: '/workers/:id', component: WorkerPage},

]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
