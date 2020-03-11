<template>
  <div id="app">
    <head>
      <link href="https://pro.fontawesome.com/releases/v5.12.0/css/all.css" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Berkshire+Swash|Lato|Macondo+Swash+Caps&display=swap" rel="stylesheet">
      <title>Critical Reactions</title>
    </head>
    <div id="app">
      <Header :party="party"/>
      <router-view class="container-lg" :party="party" />
      <!-- <button v-for="tab in tabs" :key="tab" @click="selected = tab;">
        {{ tab }}
      </button>

      <component :party="party" :is="selected"></component> -->
    </div>
    <!-- <div  >

      <Landing :party="party.title"/>
      <Party :party="party"/>
      <Members :members="party.m"/>
    </div> -->
    
  </div>
</template>

<script>
import Header from './components/Header.vue'


export default {
  name: 'App',
  components: {
    Header,
  },
  data() {
    return {
      party: Object,
    };
  },
  mounted() {
    this.getMembers();
  },

  methods: {
    async getMembers() {
      // try {
      const response = await fetch("http://127.0.0.1:8000/api/party/1/");
      const data = await response.json();
      this.party = data;
      // } catch (error) {}
    },
  },
}
</script>

<style lang="scss">
$primary: seagreen;
$secondary: darkgoldenrod;
$dark: #2c3e50;
$card-color: $dark;

$body-bg: lighten($dark, 70%);
$link-hover-color: lighten($primary, 15%);
$card-bg: transparentize($dark, .7);

@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';
</style>

/* 
font-family: 'Berkshire Swash', cursive;
font-family: 'Macondo Swash Caps', cursive;
font-family: 'Lato', sans-serif; 
*/

/* body{
  margin:0;
}
#app {
  font-family: 'Lato', sans-serif; 
  text-align: center;
  color: #2c3e50;
} */

