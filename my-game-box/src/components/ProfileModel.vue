<template>
    <div id="profile">
        <h1>Perfil</h1>
        {{ user_id }}
        {{ name }}
      <ion-button v-on:click="logout()" >
        Deslogar
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
                let response = await fetch(`http://127.0.0.1:8000/users?id=${this.user_id}`);
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
