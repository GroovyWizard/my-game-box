<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-back-button default-href="tab1"></ion-back-button>
        </ion-buttons>
        <ion-title>Pesquisar Jogos</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
        <div style="text-align: center; padding:20px; margin:20px;"> 
          <label style="font-size: 20px" for="search"> Nome: </label>
          <input type="search" class="form-control" id="search" placeholder="Devil May Cry 5" v-model="form.search">

          <span id="">
            <ion-button color=warning v-on:click="submitForm()"> Pesquisar </ion-button>
            <ion-button color=danger v-on:click="clear()"> Limpar </ion-button>

          </span>
        </div>

    <div v-if="game==0">
      <p> Oops.. Não achamos nenhum jogo com esse nome.</p>
    </div>
    <div v-else-if="game && game != 0">
        <Game :name="game.name" :rating="game.rating" :imgUrl="game.banner_img" :id="game.id" />
    </div>

    </ion-content>

  

  </ion-page>
</template>

<script >
import { IonPage, IonBackButton, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import Game from "../components/CharacterModel.vue"

export default {
  name: 'SearchPage',
  components: { IonBackButton, Game, IonHeader, IonToolbar, IonTitle, IonContent, IonPage },
  data() {
    return {
      form: {
        search: 'Devil May Cry 5',

      },
      game: null,
    }
  },
  methods: {
    async submitForm() {
      try {
        let response = await fetch(`http://10.0.2.2:8000/games?option=${this.form.search}`);
        let res = await response.json();
        if(res[0].length === 0) {
          this.game = 0;
        }
        this.game = res[0];
        console.log(this.game)
      } catch (error) {
        console.log(error);
        this.game = 0;
      }
    },
    clear() {
      this.game = null;
    }
  }
};


</script>
