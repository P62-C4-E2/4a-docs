<template slot="actions" slot-scope="data">
  <h2>Elija uno de nuestros vehiculos para más información:</h2>
  <div class="contenedor_vehiculos">
    <ul v-for="vehiculo in vehiculos" :key="vehiculo.id">
      <div class="vehiculo_item">
        <li>
          <img :src="vehiculo.image_URL">
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
          <button :id="vehiculo.id" v-on:click="loadDetails(vehiculoId)">Ver Detalles</button>
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
        vehiculoId: vehiculo.id,
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
    loadDetails(vehiculoId){
      this.$router.push({
        name: "detallesVehiculo",
        params: vehiculoId,
      })
    }
  },
};
</script>

<style>
.contenedor_vehiculos .vehiculo_item{
  display: grid;
  grid-auto-rows: minmax(50px, auto);
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
  padding: 10px;
  height: 270px;
  justify-items: center;
}
ul{
  justify-items: center;
}

.contenedor_vehiculos .vehiculo_item ul{
  justify-items: center;
}

.contenedor_vehiculos .vehiculo_item li{
  display: grid;
  grid-template-columns: repeat(1, 500px);
  grid-auto-rows: minmax(30px, auto);
  list-style: none;
  background: rgb(0, 0, 51);
  width: 800px;
  margin-left: 250px;
  transform: scale(1);
  transition: transform .2s;
  border-radius:25px;
}
.contenedor_vehiculos .vehiculo_item li:hover{
  transform: scale(1.2);
}
.contenedor_vehiculos .vehiculo_item li img {
  grid-column: 1/2;
  align-content: center;
  justify-content: center;
  margin: 10px;
  width: 350px;
  height: 250px;
  border-radius: 15px;
}

.contenedor_vehiculos .vehiculo_item li p, h4 {
  grid-column: 2/2;
  color: white;
  text-align: justify;
  text-justify: center;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.contenedor_vehiculos .vehiculo_item li p, h4, button {
  align-items: center;
  justify-content: center;
  grid-column: 2/2;
  align-content: space-around;
}

.contenedor_vehiculos .vehiculo_item li button{
  margin-top: 15px;
  margin-bottom: 15px;
  position: relative;
  width: 80%;
}

button {
  color: white;
  background: rgb(0, 0, 51);
  border: 3px solid gray;
  border-radius: 20px;
  padding: 10px 20px;
  margin: 10px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-weight: bold;
}

button:hover {
  color: rgb(0, 0, 51);
  background: white;
  border: 3px solid rgb(0, 0, 51);
}
</style>
