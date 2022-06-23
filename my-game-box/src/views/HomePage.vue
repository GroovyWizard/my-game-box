<template>

  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title style=" ">Home</ion-title>
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
            <template v-for="todo in todos" :key="todo.id">
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
          <h3 style="text-align: center;"> Jogos em Destaque </h3>
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
      todos: [],
      recent: [],
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
        let response = await fetch("http://127.0.0.1:8000/api/game/list?option=featured");
        this.todos = await response.json();
      } catch (error) {
        console.log(error);
      }

      try {
        let response = await fetch("http://127.0.0.1:8000/games/");
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