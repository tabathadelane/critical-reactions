<template>
  <div id="app">
    <head>
      <link href="https://pro.fontawesome.com/releases/v5.12.0/css/all.css" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Uncial+Antiqua&display=swap" rel="stylesheet">
    </head>
    <div style="font-size: 24px;">
      <!-- <i class="fad fa-dice-d20" style="color: purple;"></i> -->
      <i class="fad fa-dice-d20 fa-10x" style="color: seagreen;"></i>
      <!-- <i class="fas fa-exclamation fa-sm fa-stack-1x"></i> -->
      <!-- <i class="fad fa-moon-cloud fa-10x fa-swap-opacity" style="--fa-secondary-color: wheat;"></i> -->
    </div>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <HelloWorld msg="Critical Reactions Coming Soon"/>
    <Members :members="members"/>
    
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Members from './components/Members.vue'

// function getCookie(name) {
//   var cookieValue = null;
//   if (document.cookie && document.cookie !== "") {
//     var cookies = document.cookie.split(";");
//     for (var i = 0; i < cookies.length; i++) {
//       var cookie = cookies[i].trim();
//       // Does this cookie string begin with the name we want?
//       if (cookie.substring(0, name.length + 1) === name + "=") {
//         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//         break;
//       }
//     }
//   }
//   return cookieValue;
// }

export default {
  name: 'App',
  components: {
    HelloWorld,
    Members
  },
  data() {
    return {
      members: []
    };
  },
  mounted() {
    this.getMembers();
  },

  methods: {
    async getMembers() {
      // try {
      const response = await fetch("http://127.0.0.1:8000/api/members/",{
        method: "GET",
        headers: {
          "Content-type": "application/json; charset=UTF-8",
        }
      });
      const data = await response.json();
      this.members = data;
      // } catch (error) {}
    },
  },
}
</script>

<style>
#app {
  font-family: 'Uncial Antiqua', cursive;
  text-align: center;
  color: #2c3e50;
  margin-top: 100px;
}
</style>
