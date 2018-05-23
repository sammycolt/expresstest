<template>
    <div class="card-header">
      <button v-if="checkType()" class="btn btn-clear float-right" @click="deleteTest()"></button>
      <div class="card-title" @click="onClick">Test: {{ title }}</div>
      <div class="card-subtitle" @click="onClick">Author: {{ username }}</div>
      <div class="card-subtitle" @click="onClick">Questions: {{ questionsCount }}</div>
      <div class="card-subtitle" @click="onClick">Max time: {{ maxTime }} min</div>
      <div class="card-subtitle" v-if="!checkType()">Attempts: {{ remainingAttempts }}</div>
      <div class="card-subtitle" v-if="!checkType() && remainingTime !== undefined && remainingTime !== null && remainingTime !== '0m, 0s'">
        Seconds to end: {{ remainingTime }}
      </div>
      <div class="card-subtitle" v-if="!checkType() ">
          <span class="label label-primary" v-bind:class="correctClass(remainingTime !== undefined && remainingTime !== null && remainingTime !== '0m, 0s')">
            {{ correctLabel(remainingTime !== undefined && remainingTime !== null && remainingTime !== '0m, 0s') }}
          </span>
        </div>
      <br v-if="!checkType()">
      <button v-if="!checkType()" class="btn btn-sm" @click="onClick">Pass</button>
      <button v-if="!checkType()" class="btn btn-sm" @click="results()">Results</button>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import { UserType } from '../../enums/userType'

export default {
  name: 'test-list-elem',
  props: ['title', 'author', 'id', 'questionsCount', 'maxTime', 'remainingAttempts', 'remainingTime'],
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
    },
    results () {
      this.$router.push({name: 'TestResults', params: {'id': this.id}})
    },
    correctClass (isCorrect) {
      if (isCorrect) {
        return 'label-success'
      } else {
        return 'label-error'
      }
    },
    correctLabel (isCorrect) {
      if (isCorrect) {
        return 'Going'
      } else {
        return 'Not going'
      }
    }
  },
  created: function () {
    this.$store.dispatch('getUserDetails', this.author)
  }
}
</script>
