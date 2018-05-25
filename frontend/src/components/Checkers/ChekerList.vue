<template>
  <div id="app">
    <center v-if="this.myCheckers.length">
      <br>
      <h5> My checkers</h5>
    </center>
    <div class="card" v-for="checker in this.myCheckers">
      <div class="card-header">
        <button class="btn btn-clear float-right" v-on:click="deleteChecker(checker.id)"></button>
        <div class="card-title"><a :href="checker.file_url">{{ checker.name }}</a></div>
      </div>
      <div class="card-body">{{ checker.description }}</div>
    </div>

    <center v-if="this.otherCheckers.length">
      <br>
      <h5>Other checkers</h5>
    </center>
    <div class="card" v-for="checker in this.otherCheckers">
      <div class="card-header">
        <div class="card-title"><a :href="checker.file_url">{{ checker.name }}</a></div>
      </div>
      <div class="card-body">{{ checker.description }}</div>
    </div>

    <div v-if="!this.myCheckers.length && !this.otherCheckers.length">
      <br>
      <center>
        <h5>No checkers here yet</h5>
      </center>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
  name: 'checker-list',
  computed: mapState({
    myCheckers (state) {
      return state.myCheckers
    },
    otherCheckers (state) {
      return state.otherCheckers
    }
  }),
  methods: {
    deleteChecker (checkerId) {
      this.$store.dispatch('deleteChecker', checkerId)
    }
  },
  beforeMount () {
    this.$store.dispatch('getMyCheckers')
    this.$store.dispatch('getOtherCheckers')
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
