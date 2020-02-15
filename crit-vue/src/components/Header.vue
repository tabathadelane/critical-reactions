<template>
  <div class="hello" style="color: seagreen; font-size: 24px;">
    <h1><i class="fad fa-dice-d20"></i> {{ party }}</h1>
    
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
    party: String
  }
}
</script>

<style scoped>
h1 {
  font-family: 'Berkshire Swash', cursive;


}
</style>