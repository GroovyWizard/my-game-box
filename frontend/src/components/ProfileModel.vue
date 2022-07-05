<template>
    <div class="profile">
        <h1>Perfil</h1>
        <img style="width: 90px; height: 90px" src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fmultidoge.org%2Fimages%2FMultiDoge.png&f=1&nofb=1">
        <p style="font-weight: bold;"> ID: {{ user_id }} </p>
        <p> Nome: {{ name }} </p>
      <ion-button color=danger v-on:click="logout()" >
        Sair
      </ion-button >
    </div>
</template>

<script >


export default {
    name: 'ProfileModel',
    components: {

    },
    data() {
        return {
            name: "",
            favoriteGame: "",
            user_id: localStorage.getItem("user_id")

        };
    },
    methods: {
        logout() {
            localStorage.removeItem('user_id');
            this.$emit('reload', localStorage.removeItem("user_id"));

        },
        async getData() {
            try {
                let response = await fetch(`http://10.0.2.2:8000/users?id=${this.user_id}`);
                let profile = await response.json();
                this.name = profile[0].name || "Um erro ocorreu logue novamente.";
                this.favoriteGame = profile[0].favoriteGame
            } catch (error) {
                console.log(error);
            }
        },
    },
    created() {
        this.getData();
    },

}




</script>

<style scoped>
.profile{
    text-align: center;
    padding: 30px;
    margin: 30px;
}

</style>