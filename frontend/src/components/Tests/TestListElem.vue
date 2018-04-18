<template>
<div class="card-header" @click="onClick">
  <div class="card-title">Test: {{ title }}</div>
  <div class="card-subtitle">Author: {{ username }}</div>
  <div class="card-subtitle">Questions: {{ questionsCount }}</div>
</div>
</template>

<script>
import { mapState } from 'vuex'
import { UserType } from '../../enums/userType'

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
      if (this.$store.state.userInfo.type === UserType.TEACHER.toString()) {
        this.$router.push({name: 'TestInfo', params: {'id': this.id}})
      } else if (this.$store.state.userInfo.type === UserType.STUDENT.toString()) {
        this.$router.push({name: 'TestPassing', params: {'id': this.id}})
      }
    }
  },
  created: function () {
    this.$store.dispatch('getUserDetails', this.author)
  }
}
</script>
