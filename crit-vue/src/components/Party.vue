<template>
  <div class="party">
    <div class="p-box" >
      <p class="who">{{party.who}}</p>
      <p class="what">{{party.what}}</p>
      <p class="why">{{party.why}}</p>
    </div>    
  </div>
</template>

<script>
export default {
  name: 'Party',
  props: {
    party: Object
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.party{
  height: 100vh;

}
h1 {
  font-family: 'Macondo Swash Caps', cursive;
}

.p-box {
  margin: auto;
  width: 60vw;

  
}
</style>
