<template>

  <ion-page>
    <ion-header>
      <ion-toolbar style="text-align: center;">
        <ion-title style="color: green; font-weight: bold;   text-shadow: 0.5px 0.5px green;
 text-align: center;">My Game Box

          <span>
          </span>

        </ion-title>
        <img style="width: 30px; height: 30px;"
          src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwikiclipart.com%2Fwp-content%2Fuploads%2F2017%2F01%2FTreasure-chest-free-to-use-clip-art-2.png&f=1&nofb=1">

      </ion-toolbar>
    </ion-header>


    <ion-content :scroll-events="true">
      <ion-fab vertical="top" horizontal="start" slot="fixed">
        <ion-fab-button id="open-modal">
          <ion-icon :icon="add"></ion-icon>
        </ion-fab-button>
      </ion-fab>



      <ion-content :scroll-events="true">

        <div class="swiper-content">
          <swiper ref="mySwiper" :autoplay="true" :modules="modules" :options="swiperOption" class="show-swiper">
            <template v-for="todo in recent" :key="todo.id">
              <swiper-slide>
                <div class="swiper-item">
                  <span><img style="width: 400px; height: 250px" class="banner" v-bind:src="todo.banner_img"></span>
                  <div class="centered"> {{ todo.name }}</div>
                </div>
              </swiper-slide>
            </template>
          </swiper>
        </div>

        <div class="">
          <h3 style="text-align: center;"> Jogos em Destaque <br> (comunidade) </h3>
          <swiper ref="featuredSwiper" :autoplay="true" :modules="modules" :options="swiperOption">
            <template v-for="todo in todos" :key="todo.id">
              <swiper-slide>
                <div class="swiper-item">
                  <Todo :name="todo.name" :rating="todo.rating" :imgUrl="todo.banner_img" :id="todo.id" :progress=false
                    @changedProgress="toggleOngoing" @remmed="removeTodo" @updatedContent="changeContent" />
                </div>
              </swiper-slide>
            </template>
          </swiper>


          <h3 style="text-align: center;"> Jogos Recentes </h3>
          <swiper ref="featuredSwiper" :autoplay="true" :modules="modules" :options="swiperOption">
            <template v-for="todo in recent" :key="todo.id">
              <swiper-slide>
                <div class="swiper-item">
                  <Todo :name="todo.name" :rating="todo.rating" :imgUrl="todo.banner_img" :id="todo.id" :progress=false
                    @changedProgress="toggleOngoing" @remmed="removeTodo" @updatedContent="changeContent" />
                </div>
              </swiper-slide>
            </template>
          </swiper>




        </div>

        <ion-modal ref="modal" trigger="open-modal">
          <ion-header>
            <ion-toolbar>
              <ion-buttons slot="start">
                <ion-button @click="cancel()">Cancel</ion-button>
              </ion-buttons>
              <ion-title>Novo jogo</ion-title>
              <ion-buttons slot="end">
                <ion-button :strong="true" @click="confirm()">Confirm</ion-button>
              </ion-buttons>
            </ion-toolbar>
          </ion-header>
          <ion-content class="ion-padding">
            <NewGame />
          </ion-content>
        </ion-modal>
      </ion-content>
    </ion-content>
  </ion-page>

</template>

<script>
import Todo from "../components/CharacterModel.vue"
import NewGame from "../components/NewCharacter.vue"
import 'swiper/css';
import '@ionic/vue/css/ionic-swiper.css';
import 'swiper/css/autoplay';
import { IonFab, IonFabButton, IonPage, IonModal, IonItem, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import { Autoplay, Keyboard, Pagination, Scrollbar, Zoom } from 'swiper';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { OverlayEventDetail } from '@ionic/core/components';
import { defineComponent, ref } from 'vue';
import {
  add,
} from 'ionicons/icons';

export default {
  name: 'HomePage',
  components: {
    IonModal,
    Swiper,
    SwiperSlide,
    Todo, NewGame, IonHeader, IonToolbar, IonTitle, IonContent, IonPage
  },



  data() {
    return {
      todos: 
[
    {
        "id": 6,
        "name": "Elden Ring",
        "rating": 95,
        "description": "lden Ring is a fantasy, action and open world game with RPG elements such as stats, weapons and spells. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
        "publisher": "From Software",
        "release_year": 2022,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fmiyazaki_key_art_of_elden_ring_4k_hd_elden_ring-3840x2160.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 22,
        "name": "Cyberpunk 2077",
        "rating": 70,
        "description": ".",
        "publisher": "CD PROKEKT RED",
        "release_year": 2020,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffinancerewind.com%2Fwp-content%2Fuploads%2F2020%2F07%2Fcyberpunk-M.jpeg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 23,
        "name": "The Witcher 3",
        "rating": 99,
        "description": ".",
        "publisher": "CD PROJEKT RED",
        "release_year": 2020,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpicfiles.alphacoders.com%2F173%2F173509.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 9,
        "name": "Devil May Cry 5",
        "rating": 99,
        "description": "Years have passed since the legions of hell have set foot in this world, but now a new demonic invasion has begun, and humanity’s last hope will rest in the hands of three lone demon hunters, each offering a radically different play style. United by fate and a thirst for vengeance, these demon hunters will have to face their demons if they hope to survive.",
        "publisher": "Capcom",
        "release_year": 2019,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.wallpapersden.com%2Fimage%2Fdownload%2Fdevil-may-cry-5-special_bGhlbWeUmZqaraWkpJRmZ21lrWZlZ2k.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 1,
        "name": "God of War",
        "rating": 94,
        "description": "God of War is the sequel to God of War III as well as a continuation of the canon God of War chronology. Unlike previous installments, this game focuses on Norse mythology and follows an older and more seasoned Kratos and his son Atreus in the years since the third game. It is in this harsh, unforgiving world that he must fight to survive… and teach his son to do the same.",
        "publisher": "Santa Monica",
        "release_year": 2018,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wallpaperup.com%2Fuploads%2Fwallpapers%2F2018%2F01%2F26%2F1196896%2F3a930c52e637b0a4036b18880a92bb8f.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 3,
        "name": "Persona 5",
        "rating": 93,
        "description": "Persona 5, a turn-based JRPG with visual novel elements, follows a high school student with a criminal record for a crime he didn't commit. Soon he meets several characters who share similar fates to him, and discovers a metaphysical realm which allows him and his friends to channel their pent-up frustrations into becoming a group of vigilantes reveling in aesthetics and rebellion while fighting corruption.",
        "publisher": "Atlus",
        "release_year": 2016,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fpersona_5_solo_4k_hd-2560x1440.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 16,
        "name": "Pokemon X",
        "rating": 99,
        "description": ".",
        "publisher": "Nintendo",
        "release_year": 2016,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn02.nintendo-europe.com%2Fmedia%2Fimages%2F10_share_images%2Fgames_15%2Fnintendo_3ds_25%2FSI_3DS_PokemonX_image1600w.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 8,
        "name": "Final Fantasy XIV",
        "rating": 93,
        "description": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
        "publisher": "Square Enix",
        "release_year": 2013,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 13,
        "name": "Dark Souls 2",
        "rating": 99,
        "description": ".",
        "publisher": "From Software",
        "release_year": 2013,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwallpapercave.com%2Fwp%2F8aXz8SX.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 17,
        "name": "GTA V",
        "rating": 70,
        "description": ".",
        "publisher": "Rockstar Games",
        "release_year": 2013,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpaper.nu%2Fwp-content%2Fuploads%2F2015%2F02%2FGTA-V-Wallpaper-Full-HD-Background-Pictures.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 15,
        "name": "God of War III",
        "rating": 99,
        "description": ".",
        "publisher": "Sony",
        "release_year": 2012,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Fd%2Fa%2F4%2F1105453-god-of-war-3-wallpaper-hd-1920x1080-for-computer.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 11,
        "name": "Fallout New Vegas",
        "rating": 99,
        "description": ".",
        "publisher": "Bethesda",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.wallpapersafari.com%2F11%2F42%2FNUGKaf.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 18,
        "name": "CS GO",
        "rating": 80,
        "description": ".",
        "publisher": "Valve",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.zkGgtNv9OOnRuWWI8XgI4AHaEK%26pid%3DApi&f=1",
        "uploaded_image": null
    },
    {
        "id": 19,
        "name": "DOTA 2",
        "rating": 85,
        "description": ".",
        "publisher": "Valve",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthegamerhq.com%2Fwp-content%2Fuploads%2F2020%2F08%2FDota2-full-game-download-pc.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 20,
        "name": "World of Warcraft",
        "rating": 90,
        "description": ".",
        "publisher": "Blizzard",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2FAGC2gcb.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 21,
        "name": "Diablo 2",
        "rating": 90,
        "description": ".",
        "publisher": "Blizzard",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp4163459.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 14,
        "name": "Halo 3",
        "rating": 99,
        "description": ".",
        "publisher": "Microsoft",
        "release_year": 2007,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.purexbox.com%2F1b141f8f16c41%2Fits-been-13-long-years-since-halo-3-finished-the-fight.original.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 10,
        "name": "Devil May Cry 3",
        "rating": 100,
        "description": "DMC",
        "publisher": "Capcom",
        "release_year": 2004,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages7.alphacoders.com%2F659%2F659763.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 12,
        "name": "The Elder Scrolls III: Morrowind",
        "rating": 99,
        "description": ".",
        "publisher": "Bethesda",
        "release_year": 2004,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwallpapercave.com%2Fwp%2FFcSX5bd.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 4,
        "name": "Star Wars Knights Of The Old Republic",
        "rating": 91,
        "description": "Star Wars: Knights of the Old Republic is a role-playing video game. Players will be able to create their own characters and be able to choose what gender, appearance, class, skills, attributes, and feats they have throughout the game - no two characters will be the same!",
        "publisher": "BioWare",
        "release_year": 2003,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstore-images.s-microsoft.com%2Fimage%2Fapps.31109.70175563886973287.cdcc9630-9116-4c57-94d8-f8a844937ece.7ddd4ee1-277e-40f8-ae1c-ae9e73e75923%3Fmode%3Dscale%26q%3D90%26h%3D1080%26w%3D1920&f=1&nofb=1",
        "uploaded_image": null
    }
],
      recent: 
[
    {
        "id": 6,
        "name": "Elden Ring",
        "rating": 95,
        "description": "lden Ring is a fantasy, action and open world game with RPG elements such as stats, weapons and spells. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
        "publisher": "From Software",
        "release_year": 2022,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fmiyazaki_key_art_of_elden_ring_4k_hd_elden_ring-3840x2160.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 22,
        "name": "Cyberpunk 2077",
        "rating": 70,
        "description": ".",
        "publisher": "CD PROKEKT RED",
        "release_year": 2020,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffinancerewind.com%2Fwp-content%2Fuploads%2F2020%2F07%2Fcyberpunk-M.jpeg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 23,
        "name": "The Witcher 3",
        "rating": 99,
        "description": ".",
        "publisher": "CD PROJEKT RED",
        "release_year": 2020,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpicfiles.alphacoders.com%2F173%2F173509.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 9,
        "name": "Devil May Cry 5",
        "rating": 99,
        "description": "Years have passed since the legions of hell have set foot in this world, but now a new demonic invasion has begun, and humanity’s last hope will rest in the hands of three lone demon hunters, each offering a radically different play style. United by fate and a thirst for vengeance, these demon hunters will have to face their demons if they hope to survive.",
        "publisher": "Capcom",
        "release_year": 2019,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.wallpapersden.com%2Fimage%2Fdownload%2Fdevil-may-cry-5-special_bGhlbWeUmZqaraWkpJRmZ21lrWZlZ2k.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 1,
        "name": "God of War",
        "rating": 94,
        "description": "God of War is the sequel to God of War III as well as a continuation of the canon God of War chronology. Unlike previous installments, this game focuses on Norse mythology and follows an older and more seasoned Kratos and his son Atreus in the years since the third game. It is in this harsh, unforgiving world that he must fight to survive… and teach his son to do the same.",
        "publisher": "Santa Monica",
        "release_year": 2018,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.wallpaperup.com%2Fuploads%2Fwallpapers%2F2018%2F01%2F26%2F1196896%2F3a930c52e637b0a4036b18880a92bb8f.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 3,
        "name": "Persona 5",
        "rating": 93,
        "description": "Persona 5, a turn-based JRPG with visual novel elements, follows a high school student with a criminal record for a crime he didn't commit. Soon he meets several characters who share similar fates to him, and discovers a metaphysical realm which allows him and his friends to channel their pent-up frustrations into becoming a group of vigilantes reveling in aesthetics and rebellion while fighting corruption.",
        "publisher": "Atlus",
        "release_year": 2016,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpapers.in%2Fdownload%2Fpersona_5_solo_4k_hd-2560x1440.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 16,
        "name": "Pokemon X",
        "rating": 99,
        "description": ".",
        "publisher": "Nintendo",
        "release_year": 2016,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn02.nintendo-europe.com%2Fmedia%2Fimages%2F10_share_images%2Fgames_15%2Fnintendo_3ds_25%2FSI_3DS_PokemonX_image1600w.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 8,
        "name": "Final Fantasy XIV",
        "rating": 93,
        "description": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
        "publisher": "Square Enix",
        "release_year": 2013,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.tonica.la%2F__export%2F1621096012366%2Fsites%2Fdebate%2Fimg%2F2021%2F05%2F15%2Ffinal-fantasy-xiv-endwalker-estrena-trailer_1.jpg_189669459.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 13,
        "name": "Dark Souls 2",
        "rating": 99,
        "description": ".",
        "publisher": "From Software",
        "release_year": 2013,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwallpapercave.com%2Fwp%2F8aXz8SX.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 17,
        "name": "GTA V",
        "rating": 70,
        "description": ".",
        "publisher": "Rockstar Games",
        "release_year": 2013,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.hdwallpaper.nu%2Fwp-content%2Fuploads%2F2015%2F02%2FGTA-V-Wallpaper-Full-HD-Background-Pictures.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 15,
        "name": "God of War III",
        "rating": 99,
        "description": ".",
        "publisher": "Sony",
        "release_year": 2012,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fgetwallpapers.com%2Fwallpaper%2Ffull%2Fd%2Fa%2F4%2F1105453-god-of-war-3-wallpaper-hd-1920x1080-for-computer.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 11,
        "name": "Fallout New Vegas",
        "rating": 99,
        "description": ".",
        "publisher": "Bethesda",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.wallpapersafari.com%2F11%2F42%2FNUGKaf.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 18,
        "name": "CS GO",
        "rating": 80,
        "description": ".",
        "publisher": "Valve",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.zkGgtNv9OOnRuWWI8XgI4AHaEK%26pid%3DApi&f=1",
        "uploaded_image": null
    },
    {
        "id": 19,
        "name": "DOTA 2",
        "rating": 85,
        "description": ".",
        "publisher": "Valve",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthegamerhq.com%2Fwp-content%2Fuploads%2F2020%2F08%2FDota2-full-game-download-pc.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 20,
        "name": "World of Warcraft",
        "rating": 90,
        "description": ".",
        "publisher": "Blizzard",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2FAGC2gcb.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 21,
        "name": "Diablo 2",
        "rating": 90,
        "description": ".",
        "publisher": "Blizzard",
        "release_year": 2008,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp4163459.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 14,
        "name": "Halo 3",
        "rating": 99,
        "description": ".",
        "publisher": "Microsoft",
        "release_year": 2007,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages.purexbox.com%2F1b141f8f16c41%2Fits-been-13-long-years-since-halo-3-finished-the-fight.original.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 10,
        "name": "Devil May Cry 3",
        "rating": 100,
        "description": "DMC",
        "publisher": "Capcom",
        "release_year": 2004,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages7.alphacoders.com%2F659%2F659763.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 12,
        "name": "The Elder Scrolls III: Morrowind",
        "rating": 99,
        "description": ".",
        "publisher": "Bethesda",
        "release_year": 2004,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwallpapercave.com%2Fwp%2FFcSX5bd.jpg&f=1&nofb=1",
        "uploaded_image": null
    },
    {
        "id": 4,
        "name": "Star Wars Knights Of The Old Republic",
        "rating": 91,
        "description": "Star Wars: Knights of the Old Republic is a role-playing video game. Players will be able to create their own characters and be able to choose what gender, appearance, class, skills, attributes, and feats they have throughout the game - no two characters will be the same!",
        "publisher": "BioWare",
        "release_year": 2003,
        "banner_img": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstore-images.s-microsoft.com%2Fimage%2Fapps.31109.70175563886973287.cdcc9630-9116-4c57-94d8-f8a844937ece.7ddd4ee1-277e-40f8-ae1c-ae9e73e75923%3Fmode%3Dscale%26q%3D90%26h%3D1080%26w%3D1920&f=1&nofb=1",
        "uploaded_image": null
    }
],
    };
  },
  setup() {
    return {
      modules: [Autoplay],
      add,
    };
  },
  methods: {
    async getData() {
      try {
        let response = await fetch("http://10.0.2.2:8000/api/game/list?option=featured");
        this.todos = await response.json();
      } catch (error) {
        console.log(error);
      }

      try {
        let response = await fetch("http://10.0.2.2:8000/games/");
        this.recent = await response.json();
      } catch (error) {
        console.log(error);
      }




    },

    cancel() {
      this.$refs.modal.$el.dismiss(null, 'cancel');
    },
    confirm() {
      const name = this.$refs.input.$el.value;
      this.$refs.modal.$el.dismiss(name, 'confirm');
    },
  },
  created() {
    this.getData();
  },
}
</script>

<style scoped>
.banner {
  filter: blur(1px);
  -webkit-filter: blur(1px);
}

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

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-weight: bold;
  color: white;
  text-shadow: 3px 3px black;
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