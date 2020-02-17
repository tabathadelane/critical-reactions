<template>
  <div id="app">
    <head>
      <link href="https://pro.fontawesome.com/releases/v5.12.0/css/all.css" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Berkshire+Swash|Lato|Macondo+Swash+Caps&display=swap" rel="stylesheet">
      <title>Critical Reactions</title>
    </head>
    <div>
      <button v-for="tab in tabs" :key="tab" @click="selected = tab;">
        {{ tab }}
      </button>

      <component :party="party" :is="selected"></component>
    </div>
    <!-- <div  >

      <Landing :party="party.title"/>
      <Header :party="party.title"/>
      <Party :party="party"/>
      <Members :members="party.m"/>
    </div> -->
    
  </div>
</template>

<script>
import Landing from './components/Landing.vue'
import Header from './components/Header.vue'
import Party from './components/Party.vue'
import Members from './components/Members.vue'


export default {
  name: 'App',
  components: {
    Landing,
    Header,
    Party,
    Members
  },
  data() {
    return {
      party: Object,
      tabs: ["Landing", "Header", "Party", "Members",],
      selected: "Landing"
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

<style>

/* 
font-family: 'Berkshire Swash', cursive;
font-family: 'Macondo Swash Caps', cursive;
font-family: 'Lato', sans-serif; 
*/

body{
  margin:0;
}
#app {
  font-family: 'Lato', sans-serif; 
  text-align: center;
  color: #2c3e50;
}
</style>
