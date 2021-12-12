<template>
  <h2>Elija uno de nuestros vehiculos para más información:</h2>
  <div class="contenedor_vehiculos">
    <ul v-for="vehiculo in vehiculos" :key="vehiculo.id">
      <div class="vehiculo_item">
        <li>
          <h4>
            Nombre: <span>{{ vehiculo.nombre }}</span>
          </h4>
          <p>
            <strong
              >Categoria: <span>{{ vehiculo.categoria }}</span></strong
            >
          </p>
          <p>
            <strong
              >Tarifa: COP$<span>{{ vehiculo.tarifa }}</span
              >/día</strong
            >
          </p>
          <button v-on:click="loadDetails">Ver Detalles</button>
        </li>
      </div>
    </ul>
  </div>
</template>

<script>

import gql from "graphql-tag";

export default {
  name: "ListaVehiculos",
  props: ["vehiculo"],
  data: {
    function() {
      return {
        vehiculoId: vehiculo_id,
        vehiculos: {
            id:"",
            nombre: "",
            categoria: "",
            tarifa:"",
            image_URL: ""
        }
      };
    },
  },
  apollo: {
    vehiculos: {
      query: gql`
        query Query {
          vehiculos {
            id
            nombre
            image_URL
            categoria
            disponible
            tarifa
          }
        }
      `,
      variables() {
        return {
            vehiculoId: this.vehiculoId
        };
      },
    },
  },

  methods: {
    loadDetails: function () {
      this.$router.push({ name: "detallesVehiculo" });
    },
  },
};
</script>

<style>
.contenedor_vehiculos {
  align-content: center;
  justify-content: center;
  display: grid;
  grid-template-columns: repeat(4, 280px);
  grid-auto-rows: 180px;
}

.contenedor_vehiculos .vehiculo_item {
  background: url("../assets/FordRaptor.jpg");
  background-size: 100%;
  width: 250px;
  padding: 5px;
  margin: 10px;
  height: 120px;
  align-content: center;
  justify-content: center;
}

.contenedor_vehiculos .vehiculo_item li {
  text-decoration: none;
  list-style: none;
}

.contenedor_vehiculos .vehiculo_item p,
h4 {
  margin: 3.5px;
  margin-top: 15px;
  text-align: center;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  color: white;
}

.contenedor_vehiculos .vehiculo_item span::before {
  color: white;
  text-decoration: none;
}

.contenedor_vehiculos .vehiculo_item h4 span:hover {
  color: blue;
  text-decoration: underline;
}

.contenedor_vehiculos .vehiculo_item button {
  color: white;
  background: rgb(0, 0, 51);
  border: 3px solid gray;
  border-radius: 20px;
  padding: 10px 20px;
  position: relative;
  align-items: center;
}

.contenedor_vehiculos .vehiculo_item button:hover {
  color: rgb(0, 0, 51);
  background: white;
  border: 3px solid rgb(0, 0, 51);
}
</style>
