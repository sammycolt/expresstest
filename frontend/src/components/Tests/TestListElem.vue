<template>
<div class="card-header" @click="onClick">
  <div class="card-title">Test: {{ title }}</div>
  <div class="card-subtitle">Author: {{ username }}</div>
  <div class="card-subtitle">Questions: {{ questionsCount }}</div>
</div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'test-list-elem',
  props: ['title', 'author', 'id', 'questionsCount'],
  computed: mapState({
    username (state) {
      if (state.userDetails[this.author]) {
        return state.userDetails[this.author].username
      }
    }
  }),
  methods: {
    onClick () {
//      console.log(this)
      this.$router.push({name: 'TestInfo', params: { 'id': this.id }})
    }
  },
  created: function () {
    this.$store.dispatch('getUserDetails', this.author)
  }
}
</script>
