<template>
  <b-jumbotron >
    <template v-slot:header ><p style="font-family: 'Berkshire Swash', cursive;">Coming Soon</p></template>
    <template v-slot:lead class="pl-5">Please be patient while we gather some kind words from our previous clients!</template>
    <hr class="my-4">
    <p>While we get this sorted out, please check out the other areas of the site.</p>
    <b-button variant="dark" class="m-2" ><router-link to="/party"><h4>Why us?</h4></router-link></b-button>
    <b-button variant="dark" class="m-2" ><router-link to="/members"><h4>Meet the party!</h4></router-link></b-button>
  </b-jumbotron>
  
</template>

<script>
export default {
  name: "Testimonials",
  props: {}
};
</script>