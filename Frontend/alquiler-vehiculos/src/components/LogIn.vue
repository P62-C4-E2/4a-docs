<template>
    <div class="center">
        <h1>Login</h1>
        <form v-on:submit.prevent="processLogInUser">
            <div class="txt_field">
                <input type="text" v-model="user.username">
                <span></span>
                <label>Username</label>
            </div>
            <div class="txt_field">
                <input type="password" v-model="user.password">
                <span></span>
                <label>Contraseña</label>
            </div>
            <button type="submit">Iniciar Sesión</button>
        </form>
    </div>
</template>

<script>
import gql from "graphql-tag";
export default {
    name: "logIn",

    data: function(){
        return {
            user: {
                username: "",
                password: "",
            },
        };
    },
    methods: {
        processLogInUser: async function() {
            await this.$apollo
                .mutate({
                    mutation: gql `
                        mutation($credentials: CredentialsInput!) {
                            logIn(credentials: $credentials) {
                                refresh
                                access
                            }
                        }
                    `,
                    variables: {
                        credentials: this.user,
                    },
                })
                .then((result) =>{
                    let dataLogIn = {
                        username: this.user.username,
                        token_access: result.data.logIn.access,
                        token_refresh: result.data.logIn.refresh,
                    };

                    this.$emit("completedLogIn", dataLogIn);
                })
                .catch((error) => {
                    alert("ERROR 401: Credenciales Incorrectas.");
                });
        },
    },
}
</script>

<style>
    body {
        margin: 0;
        padding: 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        background-image: url('../assets/lamborghini_image.jpeg');
        width:100%;		
        height:100%;			
        position:fixed;
        background-size:100%;
        height: 100vh;
        overflow: hidden;
    }
    .center {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 400px;
        background: rgba(255, 255, 255, 0.4);
        border-radius: 10px;

    }

    .center h1{
        text-align: center;
        padding: 0 0 20px 0;
        border-bottom: 1px solid silver;
    }

    .center form{
        padding: 0 40px;
        box-sizing: border-box;
    }

    form .txt_field{
        position: relative;
        border-bottom: 2px solid #adadad;
        margin: 30px 0;
    }

    .txt_field input{
        width: 100%;
        padding: 0 5px;
        height: 40px;
        font-size: 16px;
        border: none;
        background: none;
        outline: none;
    }

    .txt_field label{
        position: absolute;
        top: 50%;
        left: 5px;
        color: rgb(44, 44, 44);
        transform: translateY(-50%);
        font-size: 16px;
        pointer-events: none;
        transition: .5s;
    }

    .txt_field span::before{
        content: '';
        position: absolute;
        top: 40px;
        left: 0;
        width: 0;
        height: 2px;
        background: rgb(0, 0, 51);
        transition: .5s;
    }

    .txt_field input:focus ~ label,
    .txt_field input:valid ~ label{
        top: -5px;
        color: rgb(0, 0, 51);
    }

    .txt_field input:focus ~ span::before,
    .txt_field input:valid ~ span::before{
        width: 100%;
    }

    button[type="submit"]{
        width: 100%;
        height: 50px;
        border: 3px solid gray;
        background:rgb(0, 0, 51);
        color: white;
        border-radius: 25px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        font-weight: 18px;
        font-weight: 700;
        cursor: pointer;
        outline: none;
        margin: 10px;
    }

    button[type="submit"]:hover{
        border-color: rgb(0, 0, 51);
        transition: .5s;
        color:rgb(0, 0, 51);
        background: white;
    }
    
</style>
