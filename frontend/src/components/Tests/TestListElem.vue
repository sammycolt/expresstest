<template>
<div class="card-header">
  <button v-if="checkType()" class="btn btn-clear float-right" @click="deleteTest()"></button>
  <div class="card-title" @click="onClick">Test: {{ title }}</div>
  <div class="card-subtitle" @click="onClick">Author: {{ username }}</div>
  <div class="card-subtitle" @click="onClick">Questions: {{ questionsCount }}</div>
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
    },
    userType (state) {
      return state.userInfo.type
    }
  }),
  methods: {
    onClick () {
      if (this.userType === UserType.TEACHER.toString()) {
        this.$router.push({name: 'TestInfo', params: {'id': this.id}})
      } else if (this.$store.state.userInfo.type === UserType.STUDENT.toString()) {
        this.$router.push({name: 'TestPassing', params: {'id': this.id}})
      }
    },
    deleteTest () {
      this.$store.dispatch('deleteTest', this.id)
    },
    checkType () {
      return this.userType === UserType.TEACHER.toString()
    }
  },
  created: function () {
    this.$store.dispatch('getUserDetails', this.author)
  }
}
</script>
