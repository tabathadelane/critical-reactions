<template>
  <div class="members">
    <div  class="m" v-for="m in members" :key="m.pk" >
      <div class="m-box" :id="''+m.theme+''" :style="'border-color: '+m.theme+';' ">
        <h1 style="font-size: 32px;"><i :class="'fad ' + m.icon" :style="'color: '+m.theme+';'"></i> {{m.name}}</h1>
        <hr>
        <p class="race">{{m.race}}</p>
        <p class="dndclass">{{m.dndclass}}</p>
        <p class="specialty">{{m.specialty}}</p>
        <p class="interests">Interests: {{m.interests}}</p>
        <p class="bio">{{m.bio}}</p>
      </div>
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Members',
  props: {
    members: Array
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
