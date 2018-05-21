<template>

  <nav class="navbar container grid-960">
    <section class="navbar-section">
      <a v-if="notStartPage" class="btn btn-default" @click="goStart()">Main page</a>
      <a v-if="notStartPage" class="btn btn-default" @click="goBack()">Back</a>
    </section>
    <section class="navbar-center">
      <h5>
        User: {{this.username}}
      </h5>
    </section>
    <section class="navbar-section">
      <a class="btn btn-default" @click="logout()">Logout</a>
    </section>
  </nav>
</template>

<script>

import { mapState } from 'vuex'

export default {
  name: 'navbar',
  computed: mapState({
    notStartPage (state) {
      return this.$route.path !== '/'
    },
    username (state) {
      return state.userInfo.username
    }
  }),
  methods: {
    logout () {
      this.$store.dispatch('logoutUser')
      this.$router.push({name: 'Start'})
    },
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    goStart () {
      this.$router.push({name: 'Start'})
    }
  }
}
</script>
