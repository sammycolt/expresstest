<template>
  <div>
    <!--<section class="container">-->
      <!--<navbar class="text-center" ></navbar>-->
    <!--</section>-->
    <section class="container grid-960">
      <reg-form></reg-form>
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

import CreateNote from './Notes/CreateNote'
import NoteList from './Notes/NoteList'
import Navbar from './Navbar'
import UsersList from './Auth/UsersList'
import RegistrationForm from './Auth/RegistrationForm.vue'
import LoginForm from './Auth/LoginForm.vue'
import Account from './Auth/Account.vue'

export default {
  name: 'start',
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
