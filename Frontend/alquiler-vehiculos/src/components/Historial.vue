<template>
  <div id="Historial">
    <div class="container">
      <h2>
        Cliente: <span>{{ username }}</span>
      </h2>
    </div>
    <h2>Alquileres realizados</h2>
    <div class="container-table">
      <table>
        <tr>
          <th>Fecha de Inicio</th>
          <th>Fecha de Entrega</th>
          <th>Lugar de entrega</th>
          <th>Lugar de Retorno Vehiculo</th>
          <th>Entregado</th>
        </tr>
        <tr v-for="alquiler in alquilerByUsername" :key="alquiler.id">
          <td>{{ alquiler.fechaInicio }}</td>
          <td>{{ alquiler.fechaFinal }}</td>
          <td>{{ alquiler.lugarEntrega }}</td>
          <td>{{ alquiler.lugarRegreso }}</td>
          <td>{{ alquiler.entregado }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import gql from "graphql-tag";
export default {
  name: "reservasByUser",
  data: function () {
    return {
      username: localStorage.getItem("username") || "none",
      alquilerByUsername:[],
    };
  },

  apollo: {
    alquilerByUsername: {
      query: gql`
        query AlquilerByUsername($username: String!) {
          alquilerByUsername(username: $username) {
            id
            username
            vehiculoId
            vehiculoNombre
            fechaInicio
            fechaFinal
            lugarEntrega
            lugarRegreso
            entregado
          }
        }
      `,
      variables(){
          return {
              username: this.username
          };
      },
    },
  },

  created:function(){
      this.$apollo.queries.AlquilerByUsername.refetch();
  }
};
</script>

<style>
</style>