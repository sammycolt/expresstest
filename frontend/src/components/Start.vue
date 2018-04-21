<template>
  <div>
    <!--<section class="container">-->
      <!--<navbar class="text-center" ></navbar>-->
    <!--</section>-->
    <section class="container grid-960">
      <auth v-if="!check()"></auth>
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

import Account from './Auth/Account.vue'
import Auth from './Auth/Auth.vue'

export default {
  name: 'start',
  components: {
    'account': Account,
    'auth': Auth
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
