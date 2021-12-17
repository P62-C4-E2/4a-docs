import {createRouter, createWebHistory} from 'vue-router';
import App from './App.vue';

import LogIn from './components/LogIn.vue';
import SignUp from './components/SignUp.vue';
import Home from './components/Home.vue';
import ListaVehiculos from './components/ListaVehiculos.vue';
import VehiculoDetails from './components/VehiculoDetails.vue';
import Historial from './components/Historial.vue';
import Alquiler from './components/Alquiler.vue';
import Admin from './components/Admin.vue';
import VehiculosAdmin from './components/VehiculosAdmin.vue';

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
  path:`/user/vehiculos/details/:vehiculoId`,
  name: 'detallesVehiculo',
  component: VehiculoDetails
},
{
  path: `/user/reservas`,
  name: 'reservasByUser',
  component: Historial
},
{
  path: '/user/reservas/nuevaReserva',
  name: 'alquiler',
  component: Alquiler
},
{
  path: '/user/admin',
  name: 'adminPage',
  component: Admin
},
{
  path: '/user/admin/vehiculos',
  name: 'vehiculosAdmin',
  component: VehiculosAdmin
}
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router;
