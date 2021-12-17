<template>
  <div class="Crear_vehiculo">
    <h1>Crear nuevo Vehiculo</h1>
    <form v-on:submit.prevent="createVehiculo">
      <input type="text" v-model="vehiculo.id" placeholder="ID" />
      <input type="text" v-model="vehiculo.nombre" placeholder="nombre" />
      <input type="text" v-model="vehiculo.placa" placeholder="placa" />
      <input type="text" v-model="vehiculo.marca" placeholder="marca" />
      <input type="text" v-model="vehiculo.modelo" placeholder="modelo" />
      <input type="text" v-model="vehiculo.color" placeholder="color" />
      <input
        type="text"
        v-model="vehiculo.cilindraje"
        placeholder="cilindraje"
      />
      <!-- <label>Full Equipo</label>
      <input type="checkbox" v-model="vehiculo.fullEquipo" /> -->
      <input
        type="text"
        v-model="vehiculo.fullEquipo"
        placeholder="Full Equipo"
      />
      <input
        type="text"
        v-model="vehiculo.image_URL"
        placeholder="URL imagen"
      />
      <input
        type="text"
        v-model="vehiculo.transmision"
        placeholder="Transmisión"
      />
      <input type="text" v-model="vehiculo.categoria" placeholder="Categoria" />
      <input type="number" v-model="vehiculo.tarifa" placeholder="Tarifa" />
      <input
        type="text"
        v-model="vehiculo.disponible"
        placeholder="Disponible"
      />
      <button type="submit">Crear Vehículo</button>
    </form>
  </div>
  <hr />
  <div class="Consultar_Vehiculo">
    <h2>Visualizar Detalles Vehículo</h2>
    <form>
      <p>Introduzca el ID del vehículo a revisar</p>
      <input
        type="text"
        v-model="vehiculoconsulta.id"
        placeholder="ID vehículo"
      />
      <button>Buscar</button>
    </form>
    <h3>
      Vehículo: <span>{{ vehiculoconsulta.nombre }}</span>
    </h3>
    <p>Placa: {{ vehiculoconsulta.placa }}</p>
    <p>
      Marca: <span>{{ vehiculoconsulta.marca }}</span>
    </p>
    <p>
      Modelo: <span>{{ vehiculoconsulta.modelo }}</span>
    </p>
  </div>
</template>

<script>
import gql from "graphql-tag";
export default {
  name: "vehiculosAdmin",
  data: function () {
    return {
      vehiculoId: localStorage.getItem("id") || "none",
      vehiculo: {
        id: "",
        nombre: "",
        placa: "",
        marca: "",
        modelo: "",
        color: "",
        cilindraje: "",
        fullEquipo: "",
        image_URL: "",
        transmision: "",
        categoria: "",
        tarifa: "",
        disponible: "",
      },
      vehiculoconsulta: {
        id: "",
        nombre: "",
        placa: "",
        marca: "",
        modelo: "",
        color: "",
        cilindraje: "",
        fullEquipo: "",
        image_URL: "",
        transmision: "",
        categoria: "",
        tarifa: "",
        disponible: "",
      },
    };
  },
  methods: {
    createVehiculo: async function () {
      await this.$apollo.mutate({
        mutation: gql`
          mutation Mutation($vehiculo: VehiculoInput!) {
            nuevoVehiculo(vehiculo: $vehiculo) {
              id
              nombre
              placa
              marca
              modelo
              color
              cilindraje
              fullEquipo
              image_URL
              transmision
              categoria
              tarifa
              disponible
            }
          }
        `,
        variables: {
          vehiculo: this.vehiculo,
          vehiculoId: this.vehiculoId
        },
      });
    },

    loadVehiculoDetails: function () {
      apollo: {
        vehiculoById: {
          query: gql`
            query Query($vehiculoId: String!) {
              vehiculoById(vehiculoId: $vehiculoId) {
                id
                nombre
                placa
                marca
                modelo
                color
                cilindraje
                fullEquipo
                image_URL
                transmision
                categoria
                tarifa
                disponible
              }
            }
          `;
        }
      }
    },
  },
};
</script>