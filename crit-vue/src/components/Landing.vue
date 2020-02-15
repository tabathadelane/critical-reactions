<template>
  <div class="hello" style="font-size: 48px;">
    <h1><i class="fad fa-dice-d20"></i> {{ party }}</h1>
    
  </div>
</template>

<script>
export default {
  name: 'Landing',
  props: {
    party: String
  }
}
</script>

<style scoped>


h1 {
  font-family: 'Berkshire Swash', cursive;
  color: darkgoldenrod;
  text-shadow: -5px 8px 3px rgba(0,0,0,0.5), 1px -1px 2px rgba(255,255,255,0.5);
  margin:40vh 0 0 0;
  display: inline-block;
  width:500px;

}
.hello {
  background-color: #212324;
  background-image: url('~@/assets/waterdeep-night.png');
  background-position: bottom center;
  background-repeat: no-repeat;
  background-size: 60vw;
  margin: auto;
  height: 95vh;
}
</style>