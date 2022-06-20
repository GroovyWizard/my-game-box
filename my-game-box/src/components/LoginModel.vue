<template>
    <div id="login">
        <h1>Login</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
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
            axios
                try {
                    let response = await fetch(`http://127.0.0.1:8000/users?username=${this.input.username}`);
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
    width: 500px;
    border: 1px solid #CCCCCC;
    background-color: #FFFFFF;
    margin: auto;
    margin-top: 20px;
    padding: 20px;
}
</style>
