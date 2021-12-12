<template>
  <div class="signUp_container">
    <h1>Registro</h1>
    <form v-on:submit.prevent="processSignUp">
      <div class="wrapper">
        <div class="user_text_field">
          <input type="text" v-model="user.username" placeholder="Username" />
        </div>
        <div class="password_text_field">
          <input
            type="password"
            v-model="user.password"
            placeholder="Password"
          />
        </div>
        <div class="nombres_text_field">
          <input type="text" v-model="user.nombres" placeholder="Nombres" />
        </div>
        <div class="apellidos_text_field">
          <input type="text" v-model="user.apellidos" placeholder="Apellidos" />
        </div>
        <div class="email_text_field">
          <input type="email" v-model="user.email" placeholder="email" />
        </div>
        <div class="doc_text_field">
          <input
            type="text"
            v-model="user.documento"
            placeholder="No. Documento"
          />
        </div>
        <div class="bday_text_field">
          <label>Fecha de Nacimiento</label><br />
          <input type="date" v-model="user.fecha_nto" />
        </div> 
        <div class="tel_text_field">
          <input type="tel" v-model="user.telefono" placeholder="Teléfono" />
        </div>
        <div class="lic_text_field">
          <input
            type="text"
            v-model="user.lic_cond"
            placeholder="No. Licencia"
          />
        </div>
        <div class="licdate_text_field">
          <label>Fecha de Expedición</label><br />
          <input type="date" v-model="user.exped_lic" />
        </div>
      </div> 

      <button type="submit">Registrarse</button>
    </form>
  </div>
</template>

<script>
import gql from "graphql-tag";
export default {
  name: "signUp",
  data: function () {
    return {
      user: {
        username: "",
        password: "",
        nombres: "",
        apellidos: "",
        email: "",
        tipo_documento: "CC", 
        documento: "",
        fecha_nto: "",
        telefono: "",
        lic_cond: "",
        exped_lic: "",
      },
    };
  
  },
  methods: {
    processSignUp: async function () {
      await this.$apollo
        .mutate({
          mutation: gql`
            mutation ($userInput: SignUpInput!) {
              signUpUser(userInput: $userInput) {
                refresh
                access
              }
            }
          `,
          variables: {
            userInput: this.user,
          },
        })
        .then((result) => {
          let dataLogIn = {
            username: this.user.username,
            token_access: result.data.signUpUser.access,
            token_refresh: result.data.signUpUser.refresh,
          };
          

          this.$emit("completedSignUp", dataLogIn);
        })
        .catch((error) => {
          alert("ERROR: Fallo en el registro.");
        });
    },
  },
};
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  overflow: hidden;
}

.signUp_container {
  position: absolute;
  margin: 30px 0 20px 0;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 700px;
  background: white;
  border-radius: 20px;
}

.signUp_container h1 {
  text-align: center;
  justify-content: center;
  border-bottom: 1px solid #adadad;
}

.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 10px;
  grid-auto-rows: minmax(50px, auto);
  padding: 15px;
  align-items: center;
  justify-content: space-between;
}

.username_text_field {
  grid-column: 1/3;
  grid-row: 1;
}

.password_text_field {
  grid-column: 2/3;
  grid-row: 1;
}
.nombres_text_field {
  grid-column: 3/3;
  grid-row: 1;
}
.apellidos_text_field {
  grid-column: 1/3;
  grid-row: 2;
}
.email_text_field {
  grid-column: 2/3;
  grid-row: 2;
}
.doc_text_field {
  grid-column: 3/3;
  grid-row: 2;
}
.bday_text_field {
  grid-column: 1/3;
  grid-row: 3;
  transform: translate(0, -8px);
}

.tel_text_field {
  grid-column: 2/3;
  grid-row: 3;
}
.lic_text_field {
  grid-column: 3/3;
  grid-row: 3;
}
.licdate_text_field {
  grid-column: 1/3;
  grid-row: 4;
  transform: translate(0, -8px);
} 
</style>
