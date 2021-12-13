<template>
    <div class="information">
        <h1>¡Bienvenido <span>{{userDetailById.nombres}}</span>!</h1>
        <button v-on:click="loadUserDetails">Historial de Reservas</button>
    </div>    
</template>

<script>
import gql from "graphql-tag";
import jwt_decode from "jwt-decode";
export default {
  name: "home",
  methods: {
      
  },
  
  data: function(){
      return {
          userId: jwt_decode(localStorage.getItem("token_refresh")).user_id,
          userDetailById:{
              username: "",
              nombres: "",
              email: "",
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

</style>