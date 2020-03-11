<template>
  <div>
    <!-- <h1><i class="fad fa-dice-d20 text-primary"></i><router-link to="/"> {{ party.title }}</router-link></h1> -->
    


    <b-navbar toggleable="md" type="dark" variant="dark">
      <b-navbar-brand><h2 style="font-family: 'Berkshire Swash', cursive;"><i class="fad fa-dice-d20 text-primary"></i><router-link to="/"> {{ party.title }}</router-link></h2></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" class="justify-content-end" is-nav>
        <b-navbar-nav class="justify-content-end" >  
                
          <b-nav-item ><router-link to="/party"><h4>Why</h4></router-link></b-nav-item>
          <b-nav-item ><router-link to="/members"><h4>Who</h4></router-link></b-nav-item>
          <b-nav-item ><router-link to="/testimonials"><h4>What</h4></router-link></b-nav-item>
          <b-nav-item ><router-link to="/bookus"><h4>When</h4></router-link></b-nav-item>
          <b-nav-item ><router-link to="/AltheasBardBlog"><h4>Blog</h4></router-link></b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: {
    party: Object
  }
}
</script>

<style scoped>

</style>