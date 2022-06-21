<template>

    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button default-href="home"></ion-back-button>
                </ion-buttons>
                <ion-title>Favoritos</ion-title>
            </ion-toolbar>
        </ion-header>

        <ion-content scrollY>
            
            <template v-for="game in games" :key="game.id" >
                    <Game :favorited=true :name="game['game'].name" :rating="game['game'].rating" :imgUrl="game['game'].banner_img" :id="game['game'].id" :progress=false
                    @changedProgress="toggleOngoing" @remmed="removeTodo" @updatedContent="changeContent" />
            </template>

        </ion-content>



    </ion-page>

</template>

<script>
import { IonBackButton, IonPage, IonItem, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Game from "../components/CharacterModel.vue"


export default {
    name: 'FavoritePage',
    components: {
        Game, IonContent, IonBackButton, IonHeader, IonToolbar, IonTitle, IonPage
    },
    props: ['id'],

    data() {
        return {
            games: [],

        };
    },
    methods: {
        async getData() {
            try {
                let user_id = localStorage.getItem("user_id")
                let response = await fetch(`http://127.0.0.1:8000/favorites?id=${user_id}`);
                this.games = await response.json();
            } catch (error) {
                console.log(error);
            }
        },
    },
    async mounted() {
        await this.getData();
    },

}
</script>

<style scoped>
.navv {
    margin-top: 10px;
    text-align: center;
}

.navs {
    display: inline-block;
    margin: 25px;
    font-size: 0.85em;
    color: gray;
    transition: all 0.2s ease;
}

.navs-active {
    display: inline-block;
    margin: 25px;
    font-size: 0.9em;
    color: rgb(40, 40, 40);
    transition: all 0.2s ease;
}

.navs:hover,
.navs-active:hover,
.navsPlus:hover,
.navs-activePlus:hover {
    cursor: pointer;
}

.content {
    text-align: center;
    margin: 20px auto;
}

.navsPlus {
    transform: translateY(10%);
    margin: 25px;
    display: inline-block;
    font-size: 1.5em;
    color: gray;
    transition: all 0.2s ease;
}

.navs-activePlus {
    transform: translateY(10%);
    display: inline-block;
    margin-left: 22.5px;
    margin-right: 22.5px;
    margin-top: 17.5px;
    margin-bottom: 17.5px;
    font-size: 2em;
    color: rgb(40, 40, 40);
    transition: all 0.2s ease;
}
</style>