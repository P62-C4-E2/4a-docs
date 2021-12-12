<template>
  <h2>{{ vehiculoById.nombre }}</h2>
</template>
<script>
import gql from "graphql-tag";
export default {
  name: "detallesVehiculo",

  data: function () {
    return {
      VehiculoId: vehiculo_id,
      vehiculoById: {
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
      },
    };
  },

  apollo: {
    vehiculoById: {
      query: gql`
        query VehiculoById($vehiculoId: String!) {
          vehiculoById(vehiculoId: $vehiculoId) {
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
          }
        }
      `,
      variables(){
          return {
              VehiculoId: this.VehiculoId,
          }
      }
    },
  },
};
</script>