<template>
  <div class="members">
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
h1 {
  font-family: 'Macondo Swash Caps', cursive;
}

.m {
  width: 40%;
  margin: auto;
}
.m-box {
  border: 5px solid;
  border-radius: 5px;
  margin: 10px;
  
}
</style>
