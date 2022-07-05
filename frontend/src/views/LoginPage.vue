<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
    
        <ion-title>Login</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Tab 2</ion-title>
        </ion-toolbar>
      </ion-header>
      <div v-if="loggedIn">
        <ProfileModel @reload="ForcesUpdateComponent($event);" />
      </div>
      <div v-else>
        <RegisterModel @reload="ForcesUpdateComponent($event);" />
        <LoginModel @reload="ForcesUpdateComponent($event);" />
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent } from '@ionic/vue';
import LoginModel from '../components/LoginModel.vue';
import RegisterModel from '../components/RegisterModel.vue';
import ProfileModel from '../components/ProfileModel.vue';

export default defineComponent({
  name: 'Tab2Page',
  components: { ProfileModel, RegisterModel, LoginModel, IonHeader, IonToolbar, IonTitle, IonContent, IonPage },
  data() {
    return {
      loggedIn: localStorage.getItem("user_id")
    }
  },
  methods: {
    ForcesUpdateComponent(user_id: any) {
      this.loggedIn = user_id;
    }
  }
});
</script>

<style scoped>
</style>