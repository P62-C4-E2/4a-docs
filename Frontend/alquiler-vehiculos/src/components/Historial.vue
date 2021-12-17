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

};
</script>

<style>
#Historial{
    width: 80%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
}

#Historial .container-table{
    width: 80%;
    max-height: 250px;
    overflow-y: scroll;
    overflow-x: hidden;
    background: rgba(0, 0, 0, 0.3);
}

#Historial table{
    width: 100%;
    border-collapse: collapse;
    border: 1px solid rgba(0, 0, 0, 0.3);
}

#Historial table td,
#Historial table th {
    border: 1px solid #ddd;
    color: white;
    padding: 8px;
}

#Historial table tr:nth-child(even) {
    background-color: rgba(0, 0, 0, 0.3);
}

#Historial table tr:hover {
    background-color: rgba(0, 0, 0, 0.1);
}

#Historial h2 {
    color: rgb(0, 0 , 51);
}

#Historial h2 span:hover{
    text-decoration: underline;
    color: blue;
}
</style>