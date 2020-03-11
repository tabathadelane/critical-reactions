<template>
  <!-- <div  :style="'background:url('+bg+'); max-height: 100%'"> -->
      <b-jumbotron bg-variant="transparent" vertical-align="bottom">
        <template v-slot:header><p style="font-family: 'Berkshire Swash', cursive;">Welcome!</p></template>
        <template v-slot:lead class="pl-5">Get to know {{party.title}}, and learn what we can do for you!</template>
        <b-button variant="dark" class="m-2" ><router-link to="/party"><h4>Why us?</h4></router-link></b-button>
        <b-button variant="dark" class="m-2" ><router-link to="/members"><h4>Meet the party!</h4></router-link></b-button>
      </b-jumbotron>
  <!-- </div>   -->
</template>

<script>

import png from "@/assets/waterdeep-night.png";
export default {
  name: 'Home',
  props: {
    party: Object
  },
  data (){
    return{
      bg: png
    }
  }
}
</script>

<style scoped>

</style>
<style lang="scss" scoped>
// $font-family-sans-serif: 'Berkshire Swash', cursive;
$primary: #f8f9fa;
$dark: #2c3e50;
$jumbotron-color: seagreen;

@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';


</style>