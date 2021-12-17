<template>
    <div class="information">
        <h1>¡Bienvenido <span>{{userDetailById.username}}</span>!</h1>
        <h2>Tu nombre: <span>{{userDetailById.nombres}}</span></h2>
        <p>Tu correo Registrado: <span>{{userDetailById.email}}</span></p>
        <button v-on:click="nuevaReserva">Nuevo Alquiler</button>
        <button v-on:click="loadUserDetails">Historial de Reservas</button>
        <button v-show="userDetailById.is_staff" v-on:click="loadAdminPage">Página Administración</button>
        
    </div>    
</template>

<script>
import gql from "graphql-tag";
import jwt_decode from "jwt-decode";
export default {
  name: "home",
  methods: {
      loadUserDetails: function(){
      this.$router.push({name: "reservasByUser"})
    },
    nuevaReserva: function(){
        this.$router.push({name: "alquiler"})
    },
    loadAdminPage: function() {
        this.$router.push({name: 'adminPage'})
    },
  },
  
  data: function(){
      return {
          userId: jwt_decode(localStorage.getItem("token_refresh")).user_id,
          userDetailById:{
              username: "",
              nombres: "",
              email: "",
              is_staff: ""
          },
      };
  },

  apollo: {
      userDetailById: {
          query: gql `
            query ($userId:Int!){
                userDetailById(userId: $userId){
                    username
                    nombres
                    email
                    is_staff
                }
            }
          `,
          variables() {
              return {
                  userId: this.userId,
              };
          }
      },
  }
};
</script>
<style>
.information{
    color: rgb(0, 0, 51);
    justify-content: center;
    text-align: center;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.information p{
    font-size: 40px;
}

.information span:hover{
    text-decoration: underline;
    color: blue;
}

</style>