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
          <h1> PLACEHOLDER FAVORITOS </h1>

        </ion-content>



    </ion-page>

</template>

<script>
import { IonBackButton, IonPage, IonItem, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';

export default {
    name: 'FavoritePage',
    components: {
        IonBackButton, IonHeader, IonToolbar, IonTitle, IonPage
    },
    props: ['id'],

    data() {
        return {
            game: [],
        };
    },
    methods: {
        async getData() {
            try {
                let response = await fetch(`http://127.0.0.1:8000/games/${this.id}`);
                this.game = await response.json();
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