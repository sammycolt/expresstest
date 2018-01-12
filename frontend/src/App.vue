<template>
  <div>
    <!--<section class="container">-->
      <!--<navbar class="text-center" ></navbar>-->
    <!--</section>-->
    <section class="container grid-960">
      <!--<reg-form></reg-form>-->
      <login-form v-if="!check()"></login-form>
      <account v-else-if="check()"></account>
      <!--<div class="columns">-->
        <!--<div class="column col-2"></div>-->
        <!--<div class="column col-8 col-md-12">-->
          <!--<div v-if="variant_">-->
            <!--<header class="text-center">-->
              <!--<h2>Create note</h2>-->
            <!--</header>-->
            <!--<create-note></create-note>-->
          <!--</div>-->
          <!--<div v-else>-->
            <!--<header class="text-center">-->
              <!--<h2>List of notes</h2>-->
            <!--</header>-->
            <!--<note-list></note-list>-->
          <!--</div>-->
        <!--</div>-->
        <!--<div class="column col-2"></div>-->
      <!--</div>-->
    </section>
  </div>
</template>

<script>

import CreateNote from './components/CreateNote'
import NoteList from './components/NoteList'
import Navbar from './components/Navbar'
import UsersList from './components/UsersList'
import RegistrationForm from './components/RegistrationForm.vue'
import LoginForm from './components/LoginForm.vue'
import Account from './components/Account.vue'

export default {
  name: 'app',
  components: {
    'navbar': Navbar,
    'create-note': CreateNote,
    'note-list': NoteList,
    'users-list': UsersList,
    'reg-form': RegistrationForm,
    'login-form': LoginForm,
    'account': Account
  },
  data: function () {
    return {
      variant_: false
    }
  },
  methods: {
    check () {
      return this.$store.getters.isLogged
    }
  }
}
</script>

<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);

  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }

  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
