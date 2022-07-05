<template>
  <div id="container">
    <strong>{{ name }}</strong>
    <p> 
    <img alt="Vue logo" style="width: 300px; height:200px;"
    src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Forig00.deviantart.net%2Faa0e%2Ff%2F2011%2F218%2F2%2F9%2Ffinal_fantasy_ii_logo_by_eldi13-d45pon1.png&f=1&nofb=1"> </p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'ExploreContainer',
  props: {
    name: String
  }
});
</script>

<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
}
</style>
