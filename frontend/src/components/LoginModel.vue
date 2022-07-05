<template>
    <div id="login">
        <h1>Login</h1>
        <br>
        <input type="text" name="username" v-model="input.username" placeholder="Usuario" />
        <br>
        <input type="password" name="password" v-model="input.password" placeholder="Senha" />
        <br>
        <ion-button color=success type="button" v-on:click="login()">Login</ion-button>
    </div>
    
</template>

<script>
import axios from "axios";

export default {
    name: 'LoginModel',
    data() {
        return {
            input: {
                username: "",
                password: ""
            }
        }
    },
    methods: {
        async login() {
                try {
                    let response = await fetch(`http://10.0.2.2:8000/users?username=${this.input.username}`);
                    let res = await response.json();
                    localStorage.setItem("user_id", res[0].id)
                    localStorage.setItem("user_id", res[0].id)
                } catch (error) {
                    console.log(error);
                }
                this.$emit('reload', localStorage.getItem("user_id"));
        }
    }
}
</script>

<style scoped>
#login {
    text-align: center;
    border: 1px solid #CCCCCC;
    background-color: #FFFFFF;
    margin: 10px;
    padding: 10px;
}
</style>
