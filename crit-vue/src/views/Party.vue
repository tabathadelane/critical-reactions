<template>
  
  <b-jumbotron >
    <template v-slot:header ><p style="font-family: 'Berkshire Swash', cursive;">Party for hire.</p></template>
    <template v-slot:lead class="pl-5">Why are we the best? Who is {{party.title}}?</template>
    <hr class="my-4">
    <p>{{party.who}}</p>
    <hr class="my-4">
    <p>{{party.what}}</p>
    <hr class="my-4">
    <p>{{party.why}}</p>
    <div class="justify-content-end">
      <b-button variant="dark" class="m-2" ><router-link to="/members"><h4>Meet the party</h4></router-link></b-button>
    </div>
  </b-jumbotron>
</template>

<script>
export default {
  name: 'Party',
  props: {
    party: Object
  }
}
</script>

<style scoped>

</style>
