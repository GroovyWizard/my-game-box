<template>

    <ion-page>
        <ion-header>
            <ion-toolbar>
                <ion-buttons slot="start">
                    <ion-back-button default-href="tab1"></ion-back-button>
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
            games: [
    {
        "id": 8,
        "rating": 45,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 6,
            "name": "Elden Ring",
            "rating": 95,
            "description": "lden Ring is a fantasy, action and open world game with RPG elements such as stats, weapons and spells. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
            "publisher": "From Software",
            "release_year": 2022,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fmiyazaki_key_art_of_elden_ring_4k_hd_elden_ring-3840x2160.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 12,
        "rating": 98,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 8,
            "name": "Final Fantasy XIV",
            "rating": 93,
            "description": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
            "publisher": "Square Enix",
            "release_year": 2013,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 13,
        "rating": 98,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 4,
            "name": "Star Wars Knights Of The Old Republic",
            "rating": 91,
            "description": "Star Wars: Knights of the Old Republic is a role-playing video game. Players will be able to create their own characters and be able to choose what gender, appearance, class, skills, attributes, and feats they have throughout the game - no two characters will be the same!",
            "publisher": "BioWare",
            "release_year": 2003,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstore-images.s-microsoft.com%2Fimage%2Fapps.31109.70175563886973287.cdcc9630-9116-4c57-94d8-f8a844937ece.7ddd4ee1-277e-40f8-ae1c-ae9e73e75923%3Fmode%3Dscale%26q%3D90%26h%3D1080%26w%3D1920&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 14,
        "rating": 76,
        "user": {
            "id": 16,
            "name": "Lucao",
            "password": "djajhdahjdh"
        },
        "game": {
            "id": 9,
            "name": "Devil May Cry 5",
            "rating": 99,
            "description": "Years have passed since the legions of hell have set foot in this world, but now a new demonic invasion has begun, and humanity’s last hope will rest in the hands of three lone demon hunters, each offering a radically different play style. United by fate and a thirst for vengeance, these demon hunters will have to face their demons if they hope to survive.",
            "publisher": "Capcom",
            "release_year": 2019,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.wallpapersden.com%2Fimage%2Fdownload%2Fdevil-may-cry-5-special_bGhlbWeUmZqaraWkpJRmZ21lrWZlZ2k.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 15,
        "rating": 28,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 10,
            "name": "Devil May Cry 3",
            "rating": 100,
            "description": "DMC",
            "publisher": "Capcom",
            "release_year": 2004,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages7.alphacoders.com%2F659%2F659763.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    }
],
            playLater: [
    {
        "id": 8,
        "rating": 45,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 6,
            "name": "Elden Ring",
            "rating": 95,
            "description": "lden Ring is a fantasy, action and open world game with RPG elements such as stats, weapons and spells. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
            "publisher": "From Software",
            "release_year": 2022,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fmiyazaki_key_art_of_elden_ring_4k_hd_elden_ring-3840x2160.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 12,
        "rating": 98,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 8,
            "name": "Final Fantasy XIV",
            "rating": 93,
            "description": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
            "publisher": "Square Enix",
            "release_year": 2013,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 13,
        "rating": 98,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 4,
            "name": "Star Wars Knights Of The Old Republic",
            "rating": 91,
            "description": "Star Wars: Knights of the Old Republic is a role-playing video game. Players will be able to create their own characters and be able to choose what gender, appearance, class, skills, attributes, and feats they have throughout the game - no two characters will be the same!",
            "publisher": "BioWare",
            "release_year": 2003,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstore-images.s-microsoft.com%2Fimage%2Fapps.31109.70175563886973287.cdcc9630-9116-4c57-94d8-f8a844937ece.7ddd4ee1-277e-40f8-ae1c-ae9e73e75923%3Fmode%3Dscale%26q%3D90%26h%3D1080%26w%3D1920&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 14,
        "rating": 76,
        "user": {
            "id": 16,
            "name": "Lucao",
            "password": "djajhdahjdh"
        },
        "game": {
            "id": 9,
            "name": "Devil May Cry 5",
            "rating": 99,
            "description": "Years have passed since the legions of hell have set foot in this world, but now a new demonic invasion has begun, and humanity’s last hope will rest in the hands of three lone demon hunters, each offering a radically different play style. United by fate and a thirst for vengeance, these demon hunters will have to face their demons if they hope to survive.",
            "publisher": "Capcom",
            "release_year": 2019,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.wallpapersden.com%2Fimage%2Fdownload%2Fdevil-may-cry-5-special_bGhlbWeUmZqaraWkpJRmZ21lrWZlZ2k.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 15,
        "rating": 28,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 10,
            "name": "Devil May Cry 3",
            "rating": 100,
            "description": "DMC",
            "publisher": "Capcom",
            "release_year": 2004,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages7.alphacoders.com%2F659%2F659763.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    }
],
            playing: [
    {
        "id": 8,
        "rating": 45,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 6,
            "name": "Elden Ring",
            "rating": 95,
            "description": "lden Ring is a fantasy, action and open world game with RPG elements such as stats, weapons and spells. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
            "publisher": "From Software",
            "release_year": 2022,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fmiyazaki_key_art_of_elden_ring_4k_hd_elden_ring-3840x2160.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 12,
        "rating": 98,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 8,
            "name": "Final Fantasy XIV",
            "rating": 93,
            "description": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
            "publisher": "Square Enix",
            "release_year": 2013,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 13,
        "rating": 98,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 4,
            "name": "Star Wars Knights Of The Old Republic",
            "rating": 91,
            "description": "Star Wars: Knights of the Old Republic is a role-playing video game. Players will be able to create their own characters and be able to choose what gender, appearance, class, skills, attributes, and feats they have throughout the game - no two characters will be the same!",
            "publisher": "BioWare",
            "release_year": 2003,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstore-images.s-microsoft.com%2Fimage%2Fapps.31109.70175563886973287.cdcc9630-9116-4c57-94d8-f8a844937ece.7ddd4ee1-277e-40f8-ae1c-ae9e73e75923%3Fmode%3Dscale%26q%3D90%26h%3D1080%26w%3D1920&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 14,
        "rating": 76,
        "user": {
            "id": 16,
            "name": "Lucao",
            "password": "djajhdahjdh"
        },
        "game": {
            "id": 9,
            "name": "Devil May Cry 5",
            "rating": 99,
            "description": "Years have passed since the legions of hell have set foot in this world, but now a new demonic invasion has begun, and humanity’s last hope will rest in the hands of three lone demon hunters, each offering a radically different play style. United by fate and a thirst for vengeance, these demon hunters will have to face their demons if they hope to survive.",
            "publisher": "Capcom",
            "release_year": 2019,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.wallpapersden.com%2Fimage%2Fdownload%2Fdevil-may-cry-5-special_bGhlbWeUmZqaraWkpJRmZ21lrWZlZ2k.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    },
    {
        "id": 15,
        "rating": 28,
        "user": {
            "id": 1,
            "name": "ronnie",
            "password": "jamesdio"
        },
        "game": {
            "id": 10,
            "name": "Devil May Cry 3",
            "rating": 100,
            "description": "DMC",
            "publisher": "Capcom",
            "release_year": 2004,
            "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages7.alphacoders.com%2F659%2F659763.jpg&f=1&nofb=1",
            "uploaded_image": null
        }
    }
],
        };
    },
    setup() {
        return { reload, star }
    },
    methods: {
        async getData() {
            try {
                let user_id = localStorage.getItem("user_id")
                let response = await fetch(`http://10.0.2.2:8000/favorites?id=${user_id}`);
                this.games = await response.json();
            } catch (error) {
                console.log(error);
            }

            try {
                let user_id = localStorage.getItem("user_id")
                let response = await fetch(`http://10.0.2.2:8000/played?id=${user_id}`);
                this.playLater = await response.json();
            } catch (error) {
                console.log(error);
            }



            try {
                let user_id = localStorage.getItem("user_id")
                let response = await fetch(`http://10.0.2.2:8000/playing?id=${user_id}`);
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