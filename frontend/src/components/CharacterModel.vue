
<template>
  <ion-card>
    <ion-card-header>
      <ion-card-subtitle> <img style="width: 300px; height: 200px" v-bind:src="imgUrl">
      </ion-card-subtitle>
      <ion-card-title class="gametext">{{ name }}</ion-card-title>
    </ion-card-header>

    <ion-card-content style="text-align: center;">
      <ion-button v-on:click="goToGamePage">
        <ion-icon style="text-align: center;" :icon="eye"></ion-icon>
      </ion-button>
      <span v-if="favorited">
        <ion-button color="danger" v-on:click="removeFavorite">
          <ion-icon :icon="close"></ion-icon>
        </ion-button>
      </span>
      <span v-else-if="playing">
        <ion-button color="secondary" v-on:click="removePlaying">
          <ion-icon :icon="close"></ion-icon>
        </ion-button>
      </span>
      <span v-else-if="played">
          <ion-button color="tertiary" v-on:click="removePlayed">
            <ion-icon :icon="close"></ion-icon>
          </ion-button>
      </span>
    </ion-card-content>
  </ion-card>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon, IonItem, IonLabel } from '@ionic/vue';
import { eye, close, ellipse, square, triangle, home, person, search, star } from 'ionicons/icons';

export default {
  components: [IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon, IonItem, IonLabel],
  props: ['played_id', 'playing_id', 'name', 'favorite_id', 'id', 'rating', 'progress', 'imgUrl', 'favorited', 'played', 'playing'],
  emits: ['changedProgress', 'remmed', 'updatedContent'],

  methods: {
    goToGamePage() {
      console.log(this.id)
      this.$router.push(`/tabs/game/${this.id}`)
    },

    removeFavorite() {
      console.log(this.favorite_id)
      axios.delete(`http://10.0.2.2:8000/favorites/${this.favorite_id}`,
        { data: { id: this.id }, headers: {} })
        .then(() => {
          alert("Jogo removido dos favoritos")
          this.$emit('reload');

        })
        .catch(() => {
          alert("Um erro ocorreu")
        })
    },


    removePlayed() {
      console.log(this.played_id)
      axios.delete(`http://10.0.2.2:8000/played/${this.played_id}`,
        { data: { id: this.id }, headers: {} })
        .then(() => {
          alert("Jogo removido dos Terminados")
          this.$emit('reload');

        })
        .catch(() => {
          alert("Um erro ocorreu")
        })
    },

    removePlaying() {
      console.log(this.playing_id)
      axios.delete(`http://10.0.2.2:8000/playing/${this.playing_id}`,
        { data: { id: this.id }, headers: {} })
        .then(() => {
          alert("Jogo removido da lista Jogando")
          this.$emit('reload');

        })
        .catch(() => {
          alert("Um erro ocorreu")
        })
    }
  },



  setup(props, { emit }) {
    const editing = ref(false)
    const updated = ref(false)
    const newContent = ref('')

    function toggleTodo() {
      emit('changedProgress', props.id)
    }
    function rem() {
      console.log()
    }
    function nowEditing() {
      editing.value = true
      newContent.value = props.name
    }
    function updateTodo() {
      if (newContent.value.length > 0) {
        sendUpdate(props.id, newContent.value)
        newContent.value = ''
        editing.value = false
      }
    }
    function cancelUpdateTodo() {
      editing.value = false
    }
    function sendUpdate(id, value) {
      console.log(id, value)
      axios.put(`https://localhost:7022/Character/${id}/${value}`)
        .then(() => {
          updated.value = true
        }).finally(() => {
          updated.value = true
        });
    }
    return { close, eye, toggleTodo, rem, editing, newContent, nowEditing, updateTodo, cancelUpdateTodo }
  }
}
</script>

<style scoped>
.todo {
  position: relative;
  height: 100px;
  width: 300px;
  text-align: center;
}

.gametext {
  align-items: center;
  text-align: center;
  font-size: medium;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
}

.characterImage {
  height: 200px;
  width: 400px;
}

.controlButtons {
  margin-right: 5%;
  position: absolute;
  top: 0;
  right: 0;
  width: 20%;
  height: 100%;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}
</style>