<template>
  <div id="app">
    <head>
      <link href="https://pro.fontawesome.com/releases/v5.12.0/css/all.css" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Berkshire+Swash|Lato|Macondo+Swash+Caps&display=swap" rel="stylesheet">
      <title>Critical Reactions</title>
    </head>
    <Header msg="Critical Reactions"/>
    <Members :members="members"/>
    
  </div>
</template>

<script>
import Header from './components/Header.vue'
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
    Header,
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
      const response = await fetch("http://127.0.0.1:8000/api/members/");
      const data = await response.json();
      this.members = data;
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


#app {
  font-family: 'Lato', sans-serif; 
  text-align: center;
  color: #2c3e50;
  margin-top: 100px;
}
</style>
