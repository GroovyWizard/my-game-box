/* eslint-disable vue/no-v-for-template-key-on-child */
<template>

  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Home</ion-title>
      </ion-toolbar>
    </ion-header>


    <div class="navv">
      <span :class="{ 'navsPlus': !addit, 'navs-activePlus': addit }" @click="selectNav(4)">+</span>
    </div>
    <ion-content :scroll-events="true" @ionScrollStart="logScrollStart()" @ionScroll="logScrolling($event)"
      @ionScrollEnd="logScrollEnd()">

     

  <div class="swiper-content">
      <swiper ref="mySwiper" :options="swiperOption" class="show-swiper">
      <template v-for="todo in todos" :key="todo.id">
        <swiper-slide >
          <div class="swiper-item">
            <span><img v-bind:src="todo.banner_img"></span>
          </div>
        </swiper-slide>
      </template>
    </swiper>
  </div>


      <div class="content" v-for="todo in todos" :key="todo.id">
        <Todo :name="todo.name" :game="todo.rating" :imgUrl="todo.banner_img" :id="todo.id" :progress=false
          @changedProgress="toggleOngoing" @remmed="removeTodo" @updatedContent="changeContent" />
      </div>


      <NewTodo @addtodo="updateTodos" />
    </ion-content>
  </ion-page>

</template>

<script>
import Todo from "../components/CharacterModel.vue"
import NewTodo from "../components/NewCharacter.vue"
import 'swiper/css';
import '@ionic/vue/css/ionic-swiper.css';
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import { Swiper, SwiperSlide } from 'swiper/vue';

export default {
  name: 'HomePage',
  components: {
    Swiper,
    SwiperSlide,
    Todo, NewTodo, IonHeader, IonToolbar, IonTitle, IonContent, IonPage
  },



  data() {
    return {
      todos: [],
    };
  },
  methods: {
    async getData() {
      try {
        let response = await fetch("http://127.0.0.1:8000/games/");
        this.todos = await response.json();
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