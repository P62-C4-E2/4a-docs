<template>
    <div class="center">
        <h1>Login</h1>
        <form method="post">
            <div class="txt_field">
                <input type="text" required>
                <span></span>
                <label>Username</label>
            </div>
            <div class="txt_field">
                <input type="password" required>
                <span></span>
                <label>Contraseña</label>
            </div>
            <button type="submit">Iniciar Sesión</button>
            <div class="signUp_link">
                ¿Aún no estás registrado? <a href="#">Regístrate</a>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    name: "logIn",
}
</script>

<style>
    body {
        margin: 0;
        padding: 0;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
        /*background: linear-gradient(70deg, black, white);*/
        background-image: url('../assets/background-image1.jpeg');
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
    }

    button[type="submit"]:hover{
        border-color: rgb(0, 0, 51);
        transition: .5s;
        color:rgb(0, 0, 51);
        background: white;
    }

    .signUp_link{
        margin: 30px;
        text-align: center;
        font-size: 16px;
        color: black;
    }

    .signUp_link a{
        color: #2691d9;
        text-decoration: none;
    }

    .signUp_link a:hover{
        text-decoration: underline;
    }
    
</style>
