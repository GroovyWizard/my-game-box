<template>

    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button default-href="tab1"></ion-back-button>
                </ion-buttons>
                <ion-title>Jogo</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content scrollY style="text-align: center;">
            <ion-img :src="game.banner_img"></ion-img>
            <ion-text>
                <h1> {{ game.name }} ( {{ game.release_year }} ) </h1>
                Nota IGDB : <span style="font-weight: bold;"> {{ game.rating }}</span>
                Nota pessoal: <span style="font-weight: bold;"> {{ favorite_rating }} </span>
                <h4 style="color: blue;"> Publisher: {{ game.publisher }} </h4>

            </ion-text>
            <ion-grid style="">
                <ion-row class="ion-align-items-center">
                    <ion-col size="12" class="ion-align-items-center">
                        <h3>Sua nota para este jogo:</h3>
                        <input type="text" name="rating" v-model="form.rating" placeholder="Sua nota" />
                        <br>
                    </ion-col>
                </ion-row>
            </ion-grid>
            <h3> Adicionar a Lista: </h3>
            <span id="favorite">
                <ion-button color=warning v-on:click="favorite()"> Favoritar </ion-button>
            </span>
            <span id="play-later">
                <ion-button color=success v-on:click="play_later()"> Jogando </ion-button>
            </span>
            <span>
                <ion-button color=tertiary v-on:click="finished()"> Terminado </ion-button>
            </span>


        </ion-content>



    </ion-page>

</template>

<script>
import { IonBackButton, IonPage, IonCol, IonRow, IonGrid, IonItem, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import axios from 'axios';

export default {
    name: 'GamePage',
    components: {
        IonBackButton, IonRow, IonCol, IonGrid, IonHeader, IonToolbar, IonTitle, IonPage
    },
    props: ['id'],

    data() {
        return {
            game: {
                "id": 6,
                "name": "Elden Ring",
                "rating": 95,
                "description": "lden Ring is a fantasy, action and open world game with RPG elements such as stats, weapons and spells. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
                "publisher": "From Software",
                "release_year": 2022,
                "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fmiyazaki_key_art_of_elden_ring_4k_hd_elden_ring-3840x2160.jpg&f=1&nofb=1",
                "uploaded_image": null
            },
            form: {
                game: 0,
                user: 0,
                rating: 98
            },
            favorite_rating: "Não possui"
        };
    },
    methods: {
        async getData() {
            try {
                let response = await fetch(`http://10.0.2.2:8000/games/${this.id}`);
                this.game = await response.json();
            } catch (error) {
                console.log(error);
            }
        },
        async getRating() {
            let user = localStorage.getItem("user_id")

            try {
                let response = await fetch(`http://10.0.2.2:8000/favorites?user=${user}&game=${this.id}`);
                let res = await response.json()
                this.favorite_rating = res[0].rating;
            } catch (error) {
                console.log(error);
            }
        },
        async favorite() {
            this.form.game = this.id
            this.form.user = localStorage.getItem("user_id")

            axios.post('http://10.0.2.2:8000/favorites/', this.form)
                .then(() => {
                    alert("Favorito salvo com sucesso")
                })
                .catch((error) => {
                    console.log(error)
                })

            await this.getRating();

        },
        async play_later() {
            this.form.game = this.id
            this.form.user = localStorage.getItem("user_id")

            axios.post('http://10.0.2.2:8000/playing/', this.form)
                .then(() => {
                    alert("Salvo com sucesso na lista jogando")
                })
                .catch((error) => {
                    console.log(error)
                })

            await this.getRating();
        },
        async finished() {
            this.form.game = this.id
            this.form.user = localStorage.getItem("user_id")

            axios.post('http://10.0.2.2:8000/played/', this.form)
                .then(() => {
                    alert("Salvo com sucesso na lista de jogados")
                })
                .catch((error) => {
                    console.log(error)
                })

            await this.getRating();
        }


    },
    created() {
        this.getRating();
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