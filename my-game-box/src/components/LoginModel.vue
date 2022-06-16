<template>
    <div id="login">
        <h1>Login</h1>
        <input type="text" name="username" v-model="input.username" placeholder="Username" />
        <input type="password" name="password" v-model="input.password" placeholder="Password" />
        <button type="button" v-on:click="login()">Login</button>
    </div>
</template>

<script>
import { Storage } from '@ionic/storage';
import CharacterRequester from "../requester/CharacterRequester"
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
                } catch (error) {
                    console.log(error);
                }
            localStorage.setItem("name", this.input.username);
            // if(this.input.username != "" && this.input.password != "") {
            //     if(this.input.username == this.$parent.mockAccount.username && this.input.password == this.$parent.mockAccount.password) {
            //         this.$emit("authenticated", true);
            //         this.$router.replace({ name: "secure" });
            //     } else {
            //         console.log("The username and / or password is incorrect");
            //     }
            // } else {
            //     console.log("A username and password must be present");
            // }
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
    margin-top: 200px;
    padding: 20px;
}
</style>
