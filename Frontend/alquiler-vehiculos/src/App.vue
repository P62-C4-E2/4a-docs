<template>
  <div id="app" class="app">
    <div class="header">
      <h1>ALQUILER DE VEHICULOS</h1>
      <nav>
        <button v-if="is_auth">Inicio</button>
        <button v-if="is_auth">Cuenta</button>
        <button v-if="is_auth">Cerrar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
      ></router-view>
    </div>


    <div class="footer">
      <h2>Alquiler de Vehiculos</h2>
    </div>
  </div>
</template>


<script>
export default {
  name: 'App',

  data: function(){
    return {
      is_auth:false
    }
  },

  components: {
  },

  methods: {
    loadLogIn: function(){
      this.$router.push({name: "logIn"})
    },
  },

  created: function() {
    
  }
}
</script>

<style>
  body{
    margin: 0 0 0 0;
  }

  .header {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    color: rgb(221, 220, 206);
    background: linear-gradient(70deg, rgb(0,0,51), white);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1 {
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: bold;
    width: 35%;
    text-align: center;
  }

  .header nav {
    height: 100%;
    width: 20%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 20px;
  }

  .header nav button {
    color:white;
    background: rgb(0,0,51);
    border: 3px solid gray;
    border-radius: 20px;
    padding: 10px 20px;
  }

  .header nav button:hover {
    color: rgb(0,0,51);
    background: white;
    border: 3px solid rgb(0,0,51);
  }

  .main-component{
    height: 75vh;
    margin: 0%;
    padding: 0%;
    background-image: './assets/lamborghini_image.jpeg';
  }

  .footer{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;
    background-color: rgb(0,0,51);
  }

  .footer h2{
    width: 100%;
    height: 100%;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
