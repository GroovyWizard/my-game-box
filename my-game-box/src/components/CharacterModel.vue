
<template>
  <ion-card>
    <ion-card-header>
      <ion-card-subtitle> <img class="characterImage" v-bind:src="imgUrl">
      </ion-card-subtitle>
      <ion-card-title>{{ name }}</ion-card-title>
    </ion-card-header>

    <ion-card-content>
      <ion-button v-on:click="showFavorites()">
        <ion-icon   :icon="star" />
      </ion-button>
      {{ rating }}
    </ion-card-content>
  </ion-card>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'
import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon, IonItem, IonLabel } from '@ionic/vue';
import { pin, walk, warning, wifi, wine, star } from 'ionicons/icons';

export default {
  components: [IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon, IonItem, IonLabel],
  props: ['name', 'id', 'rating', 'progress', 'imgUrl'],
  emits: ['changedProgress', 'remmed', 'updatedContent'],
  setup(props, { emit }) {
    const editing = ref(false)
    const updated = ref(false)
    const newContent = ref('')
    
    function showFavorites(){
      console.log(localStorage.getItem('user_id'))
    }

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
    return { showFavorites, toggleTodo, rem, editing, newContent, nowEditing, updateTodo, cancelUpdateTodo, star }
  }
}
</script>

<style scoped>
.todo {
  position: relative;
  height: 100px;
  width: 700px;
  margin: auto;
  text-align: center;
}

.todobg {
  position: absolute;
  top: 0;
  left: 1%;
  z-index: -1;
  margin: auto;
  background: white;
  border-radius: 20px;
  border-color: black;
  height: 100%;
  width: 99%;
}

.colorline {
  position: absolute;
  top: 2%;
  left: 0;
  margin: auto;
  z-index: -1;
  margin: auto;
  background: purple;
  border-radius: 20px;
  height: 96%;
  width: 100%;
}

.todotext {
  position: absolute;
  margin-left: 8%;
  display: flex;
  justify-content: left;
  text-align: left;
  align-items: center;
  height: 100%;
  width: 67%;
}

.characterImage {
  height: 200px;
  width: 400px;
  margin-right: 50px;
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

.controlButtonDone,
.controlButtonCancel,
.controlButtonEdit,
.controlButtonAdd {
  background: indigo;
  border: 0;
  color: white;
  padding: 10px;
  border-radius: 10px;
  transition: 0.4s ease;
}

.controlButtonDone:hover,
.controlButtonCancel:hover,
.controlButtonEdit:hover,
.controlButtonAdd:hover {
  transition: all 0.2s ease;
  transform: scale(1.2);
}

.controlButtonDoneCompleted,
.controlButtonAdd {
  color: green;
}

.controlButtonCancel {
  color: red;
}

.todoinput {
  color: rgb(60, 60, 60);
  width: 100%;
  border-radius: 20px;
  border: 1px lightslategray solid;
  padding-top: 10px;
  padding-bottom: 10px;
  ;
  padding-left: 10px;
  padding-right: 10px;
  transition: all 0.2s ease;
  background: whitesmoke;
}

.todoinput:focus {
  transition: all 0.2s ease;
  transform: scale(1.025);
  border: 2px lightslategray solid;
  outline: none;
}
</style>