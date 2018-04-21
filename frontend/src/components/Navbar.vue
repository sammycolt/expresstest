<template>
  <nav class="navbar">
    <section class="navbar-section">
      <a v-if="notStartPage" class="btn btn-default" @click="goBack()">Back</a>
    </section>
    <section class="navbar-center"></section>
    <section class="navbar-section">
      <a class="btn btn-default" @click="logout()">Logout</a>
    </section>
  </nav>
</template>

<script>
export default {
  name: 'navbar',
  computed: {
    notStartPage () {
      return this.$route.path !== '/'
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logoutUser')
      this.$router.push({name: 'Start'})
    },
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    }
  }
}
</script>
