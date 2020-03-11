<template>
  <div class="members">
    <h1 class="m-4" style="font-family: 'Berkshire Swash', cursive;"> Meet {{party.title}}: </h1>
    <div  class="m" v-for="m in party.m" :key="m.pk" >
      <b-card  bg-variant="light" class="m-box" :style="'border-color: '+m.theme+'; color: '+m.theme+';' ">
        <template v-slot:header>
          <h2 class="mb-0"><i :class="'fad ' + m.icon" :style="'color: '+m.theme+';'"></i> {{m.name}}</h2>
        </template>

        <b-list-group flush>
          <b-list-group-item class="mb-2">{{m.race}}</b-list-group-item>
          <b-list-group-item class="mb-2">{{m.dndclass}} - {{m.specialty}}</b-list-group-item>
          <b-list-group-item class="mb-2">Interests: {{m.interests}}</b-list-group-item>
        </b-list-group>
        <b-card-body>
          <b-card-text>{{m.bio}}</b-card-text>
        </b-card-body>
      </b-card>
      <!-- 
        previous css and grid styling before bootstrap. I wated to keep it for reference incase I decided I didn't like bootstrap

        <div class="m-box" :id="''+m.theme+''" :style="'border-color: '+m.theme+';' ">
        <h1 style="font-size: 32px;"><i :class="'fad ' + m.icon" :style="'color: '+m.theme+';'"></i> {{m.name}}</h1>
        <hr>
        <p class="race">{{m.race}}</p>
        <p class="dndclass">{{m.dndclass}}</p>
        <p class="specialty">{{m.specialty}}</p>
        <p class="interests">Interests: {{m.interests}}</p>
        <p class="bio">{{m.bio}}</p>
      </div> -->
    </div>
    
  </div>
</template>

<script>
export default {
  name: 'Members',
  props: {
    party: Array
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 /* h1 {
  font-family: 'Macondo Swash Caps', cursive;
} */


.m {
  width: 80%;
  margin: auto;
}
.m-box {
  border: 2px solid;
  border-radius: 5px;
  margin: 10px;
  
} 
</style>
