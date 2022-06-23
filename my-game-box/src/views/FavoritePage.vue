<template>

    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button default-href="home"></ion-back-button>
                </ion-buttons>
                <ion-title>Minhas Listas</ion-title>
            </ion-toolbar>
        </ion-header>

        <ion-fab vertical="top" horizontal="end" slot="fixed">
            <ion-button v-on:click="reloadPage">
                <ion-icon :icon="reload"></ion-icon>
            </ion-button>
        </ion-fab>
        <!-- <ion-content scrollX>
            

            <template v-for="game in games" :key="game.id">
                <Game :favorited=true :favorite_id="game.id" :name="game['game'].name" :rating="game['game'].rating"
                    :imgUrl="game['game'].banner_img" :id="game['game'].id" :progress=false @reload="getData"
                    @changedProgress="toggleOngoing" @remmed="removeTodo" @updatedContent="changeContent" />
            </template>
        </ion-content> -->


        <ion-content :scroll-events="true">
            <div class="">
                <h3 style="text-align: center;"> Meus Favoritos </h3>
                <swiper ref="featuredSwiper" :autoplay="true" :modules="modules" :options="swiperOption">
                    <template v-for="game in games" :key="game.id">
                        <swiper-slide>
                            <div class="swiper-item">
                                <Game :favorite_id="game.id" :favorited=true :name="game['game'].name" :rating="game['game'].rating"
                                    :imgUrl="game['game'].banner_img" :id="game['game'].id" :progress=false
                                    @changedProgress="toggleOngoing" @remmed="removeTodo"
                                    @updatedContent="changeContent" />
                            </div>
                        </swiper-slide>
                    </template>
                </swiper>

            </div>

            <h3 style="text-align: center;"> Jogar Depois </h3>

            <swiper ref="playLaterSwiper" :autoplay="true" :modules="modules" :options="swiperOption">
                <template v-for="game in playLater" :key="game.id">
                    <swiper-slide>
                        <div class="swiper-item">
                            <Game :played_id="game.id" :played=true :name="game['game'].name" :rating="game['game'].rating"
                                :imgUrl="game['game'].banner_img" :id="game['game'].id" :progress=false
                                @changedProgress="toggleOngoing" @remmed="removeTodo" @updatedContent="changeContent" />
                        </div>
                    </swiper-slide>
                </template>
            </swiper>

            <h3 style="text-align: center;"> Jogando Agora </h3>
           
           <swiper ref="playLaterSwiper" :autoplay="true" :modules="modules" :options="swiperOption">
                <template v-for="game in playing" :key="game.id">
                    <swiper-slide>
                        <div class="swiper-item">
                            <Game :playing_id="game.id" :playing=true :name="game['game'].name" :rating="game['game'].rating"
                                :imgUrl="game['game'].banner_img" :id="game['game'].id" :progress=false
                                @changedProgress="toggleOngoing" @remmed="removeTodo" @updatedContent="changeContent" />
                        </div>
                    </swiper-slide>
                </template>
            </swiper>


        </ion-content>



    </ion-page>

</template>

<script>
import { IonBackButton, IonButton, IonPage, IonIcon, IonItem, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Game from "../components/CharacterModel.vue"
import { reload, star } from 'ionicons/icons';
import 'swiper/css';
import '@ionic/vue/css/ionic-swiper.css';
import 'swiper/css/autoplay';
import { Swiper, SwiperSlide } from 'swiper/vue';



export default {
    name: 'FavoritePage',
    components: {
        Swiper, SwiperSlide, IonButton, Game, IonIcon, IonContent, IonBackButton, IonHeader, IonToolbar, IonTitle, IonPage
    },
    props: ['id'],

    data() {
        return {
            games: [],
            playLater: [],
            playing: [],
        };
    },
    setup() {
        return { reload, star }
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

            try {
                let user_id = localStorage.getItem("user_id")
                let response = await fetch(`http://127.0.0.1:8000/played?id=${user_id}`);
                this.playLater = await response.json();
            } catch (error) {
                console.log(error);
            }



            try {
                let user_id = localStorage.getItem("user_id")
                let response = await fetch(`http://127.0.0.1:8000/playing?id=${user_id}`);
                this.playing = await response.json();
            } catch (error) {
                console.log(error);
            }



        },

        async reloadPage() {
            await this.getData();
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