<template>

    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button default-href="home"></ion-back-button>
                </ion-buttons>
                <ion-title>Jogo</ion-title>
            </ion-toolbar>
        </ion-header>
        <ion-content scrollY>
            <ion-img :src="game.banner_img"></ion-img>
            <ion-text>
                <h1> {{ game.name }} </h1>
                <h1> Publisher: {{ game.publisher }} </h1>
                <h1> Ano de lançamento: {{ game.release_year }}</h1>
                <h1> Nota Metacritic : {{ game.rating }}</h1>
                <h1> Nota pessoal: {{ favorite_rating }} </h1>
            </ion-text>
            <!-- <Game :name="game.name" :rating="game.rating" :imgUrl="game.banner_img" :id="game.id" /> -->
            <div id="rating">
                <h3>Sua nota para este jogo:</h3>
                <input type="text" name="rating" v-model="form.rating" placeholder="Sua nota" />
                <br>
                <ion-button v-on:click="favorite()"> Favoritar </ion-button>
            </div>

            <div id="play-later">
                <h3>Adicionar a jogar depois</h3>
                <ion-button v-on:click="play_later()"> Adicionar </ion-button>
            </div>

            <div>
                <h3>Adicionar aos terminados</h3>
                <ion-button v-on:click="finished()"> Adicionar</ion-button>
            </div>

        </ion-content>



    </ion-page>

</template>

<script>
import { IonBackButton, IonPage, IonItem, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import axios from 'axios';

export default {
    name: 'GamePage',
    components: {
        IonBackButton, IonHeader, IonToolbar, IonTitle, IonPage
    },
    props: ['id'],

    data() {
        return {
            game: [],
            form: {
                game: 0,
                user: 0,
                rating: 0
            },
            favorite_rating: "Não possui"
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
        async getRating() {
            let user = localStorage.getItem("user_id")

            try {
                let response = await fetch(`http://127.0.0.1:8000/favorites?user=${user}&game=${this.id}`);
                let res = await response.json()
                this.favorite_rating = res[0].rating;
            } catch (error) {
                alert(error);
            }
        },
        async favorite() {
            this.form.game = this.id
            this.form.user = localStorage.getItem("user_id")

            axios.post('http://127.0.0.1:8000/favorites/', this.form)
                .then(() => {
                    alert("Favorito salvo com sucesso")
                })
                .catch((error) => {
                    console.log(error)
                })
                
                await this.getRating();

        },


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