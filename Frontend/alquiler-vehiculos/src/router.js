import {createRouter, createWebHistory} from 'vue-router';
import App from './App.vue';

import LogIn from './components/LogIn.vue';
import SignUp from './components/SignUp.vue';
import Home from './components/Home.vue';
import ListaVehiculos from './components/ListaVehiculos.vue';
import VehiculoDetails from './components/VehiculoDetails.vue';

const routes = [{
  path: '/',
  name: 'root',
  component: App
},
{
  path: '/user/home',
  name: 'home',
  component: Home
},
{
  path: '/user/logIn',
  name: "logIn",
  component: LogIn
},
{
  path: '/user/signUp',
  name: "signUp",
  component: SignUp
},
{
  path:'/user/vehiculos',
  name: 'ListaVehiculos',
  component: ListaVehiculos
},
{
  path:`/user/vehiculos/details`,
  name: 'detallesVehiculo',
  component: VehiculoDetails
}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router;
