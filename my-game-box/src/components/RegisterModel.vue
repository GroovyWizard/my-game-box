<template>
    <div id="register">
        <h1>Registre-se</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="register()">Login</button>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'RegisterModel',
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
            axios
                try {
                    let response = await fetch(`http://127.0.0.1:8000/users?username=${this.input.username}`);
                    let res = await response.json();
                    localStorage.setItem("user_id", res[0].id)
                    localStorage.setItem("user_name", res[0].name)
                } catch (error) {
                    console.log(error);
                }
        }
    }
}
</script>

<style scoped>
#register {
    width: 500px;
    border: 1px solid #CCCCCC;
    background-color: #FFFFFF;
    margin: auto;
    padding: 20px;
}
</style>
