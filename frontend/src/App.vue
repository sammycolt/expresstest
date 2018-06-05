<template>
<div>
  <br>
  <navbar v-if="isLogged"></navbar>
  <br>
  <router-view></router-view>
</div>
</template>
<script>

import Navbar from './components/Navbar.vue'
import { mapState } from 'vuex'

export default {
  components: {
    'navbar': Navbar
  },
  computed: mapState({
    isLogged (state) {
      return state.isLogged
    }
  })
}
</script>

<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);
  @import "~vue-wysiwyg/dist/vueWysiwyg.css";

  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
