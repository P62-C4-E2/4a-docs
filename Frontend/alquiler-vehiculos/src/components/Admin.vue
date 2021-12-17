<template>
    <h2>Bienvenido a la página de Administración</h2>
    <button>Ver Lista de Alquileres</button>
    <button v-on:click="loadVehiculosAdmin">Revisar Vehiculos</button>
</template>

<script>
export default {
    name: 'adminPage',
    methods: {
        loadVehiculosAdmin: function(){
            this.$router.push({name: 'vehiculosAdmin'})
        }
    }
}
</script>