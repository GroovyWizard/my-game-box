
<template>
  <ion-card>
    <ion-card-header>
      <ion-card-subtitle> <img style="width: 300px; height: 200px" v-bind:src="imgUrl">
      </ion-card-subtitle>
      <ion-card-title class="gametext">{{ name }}</ion-card-title>
    </ion-card-header>

    <ion-card-content>
      <ion-button v-on:click="goToGamePage" >
        <ion-icon :icon="star" />
      </ion-button>
      {{ rating }}
    </ion-card-content>
  </ion-card>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon, IonItem, IonLabel } from '@ionic/vue';
import { star } from 'ionicons/icons';

export default {
  components: [IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon, IonItem, IonLabel],
  props: ['name', 'id', 'rating', 'progress', 'imgUrl'],
  emits: ['changedProgress', 'remmed', 'updatedContent'],

  methods: {
     goToGamePage(){
      console.log(this.id)
      this.$router.push(`/tabs/game/${this.id}`)
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
      console.log(props.id)
      axios.delete(`https://localhost:7022/Character/${props.id}`,
        { data: { id: props.id }, headers: {} })
        .then(() => {
          alert("Personagem deletado com sucesso")
        })
        .catch(() => {
          alert("Um erro ocorreu")
        })
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
    return { toggleTodo, rem, editing, newContent, nowEditing, updateTodo, cancelUpdateTodo, star }
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