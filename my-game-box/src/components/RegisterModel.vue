<template>
    <div id="register">
        <h1>Registre-se</h1>
        <input type="text" name="username" v-model="input.name" placeholder="Usuario" />
        <br>
        <input type="password" name="password" v-model="input.password" placeholder="Senha" />
        <br>
        <ion-button type="button" v-on:click="register()">Registrar</ion-button>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'RegisterModel',
    data() {
        return {
            input: {
                name: "",
                password: ""
            }
        }
    },
    methods: {
        async register() {
            try {
                let response = await axios.post("http://127.0.0.1:8000/users/", this.input);
                let res = await response;
                localStorage.setItem("user_id", res.data.id)
                alert("Registrado com sucesso");
                this.$emit('reload', localStorage.getItem("user_id"));

            } catch (error) {
                console.log(error);
                alert("Oops um erro ocorreu.")
            }

        }
    }
}
</script>

<style scoped>
#register {
    text-align: center;
    border: 1px solid #CCCCCC;
    background-color: #FFFFFF;
    margin: 10px;
    padding: 10px;
}
</style>
