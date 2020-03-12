<template >
      <!-- <b-jumbotron bg-variant="transparent" vertical-align="bottom">
        <template v-slot:header><p style="font-family: 'Berkshire Swash', cursive;">Welcome!</p></template>
        <template v-slot:lead class="pl-5">Get to know {{party.title}}, and learn what we can do for you!</template>
        <b-button variant="dark" class="m-2" ><router-link to="/party"><h4>Why us?</h4></router-link></b-button>
        <b-button variant="dark" class="m-2" ><router-link to="/members"><h4>Meet the party!</h4></router-link></b-button>
      </b-jumbotron> -->
    <b-container fluid>
      <b-carousel
        id="carousel-1"
        :interval="4000"
        fade
        controls
        indicators
        background="dark"
        img-width="1024"
        img-height="576"
        style="text-shadow: 1px 1px 2px #333;"
      >
        <!-- Text slides with image -->
        <!-- <b-carousel-slide
          caption="First slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
          img-src="https://picsum.photos/1024/480/?image=52"
        ></b-carousel-slide> -->

        <!-- Slides with custom text -->
        <b-carousel-slide 
          img-src="https://i.ibb.co/7Gm00qg/chult.png"
          >
          <h1 style="font-family: 'Berkshire Swash', cursive;" >
            Welcome
          </h1>
          <h4> We are the Critical Reactions</h4>
        </b-carousel-slide>
        <b-carousel-slide img-src="https://i.ibb.co/R9SkD3h/skullport.png" >
          <h1 style="font-family: 'Berkshire Swash', cursive;" >
            Welcome
          </h1>
          <h4> We are the Critical Reactions</h4>
        </b-carousel-slide>
        <b-carousel-slide img-src="https://i.ibb.co/vJB6yMQ/waterdeep-1.png">
          <h1 style="font-family: 'Berkshire Swash', cursive;" >
            Welcome
          </h1>
          <h4> We are the Critical Reactions</h4>
        </b-carousel-slide>
        <b-carousel-slide img-src="https://i.ibb.co/RjV7PKh/sigil.png">
          <h1 style="font-family: 'Berkshire Swash', cursive;" >
            Welcome
          </h1>
          <h4> We are the Critical Reactions</h4>
        </b-carousel-slide>
      </b-carousel>
      <b-container class="text-center mt-2"   >
          <b-button variant="dark" ><router-link to="/party"><h4>Meet the party</h4></router-link></b-button>
      </b-container>
    </b-container>

</template>

<script>

export default {
  name: 'Home',
  props: {
    party: Object
  },
}
</script>

<style scoped>

</style>
<style lang="scss" scoped>
// $font-family-sans-serif: 'Berkshire Swash', cursive;
$dark: #2c3e50;
$primary: seagreen;
$body-bg: $dark;

.btn-dark a{
  color: $primary!important;
  &:hover{ 
  color: lighten($primary, 20%)!important;
  text-decoration: none;
  }
}

@import 'node_modules/bootstrap/scss/bootstrap';
@import 'node_modules/bootstrap-vue/src/index.scss';


</style>

https://i.ibb.co/tK4n2cv/avernus.png
https://i.ibb.co/7Gm00qg/chult.png
https://i.ibb.co/S3m3Bc4/faerun.png
https://i.ibb.co/pyytKBs/hell.png
https://i.ibb.co/ZLwb7NJ/kwalish.png
https://i.ibb.co/MG0WxBG/molac.png
https://i.ibb.co/RjV7PKh/sigil.png
https://i.ibb.co/R9SkD3h/skullport.png
https://i.ibb.co/gwsTXS0/skullport-2.png
https://i.ibb.co/vJB6yMQ/waterdeep-1.png
https://i.ibb.co/tmkP0Vd/waterdeep-2.png
https://i.ibb.co/ggPYNzn/waterdeep-3.png
https://i.ibb.co/tLN10FN/yawningportal.png
https://i.ibb.co/7nkkBtY/yawningportal-2.png