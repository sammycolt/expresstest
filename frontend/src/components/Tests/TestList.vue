<template>
  <div id="app" v-if="tests">
    <h4>Available tests:</h4>
    <div class="card" v-for="test in this.tests">
      <test-list-elem :title="test.title" :author="test.author" :id="test.id" :questionsCount="test.questions.length" :maxTime="test.max_time" :remainingAttempts="attempts(test)"
                      :remainingTime="time(test)"></test-list-elem>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'
import TestListElem from './TestListElem.vue'

export default {
  name: 'test-list',
  computed: mapState({
    tests (state) {
      return state.tests
    }
  }),
  methods: {
    attempts (test) {
      if (test.passing) {
        if (test.passing.remaining_attempts !== undefined && test.passing.remaining_attempts !== null) {
          return test.passing.remaining_attempts
        } else {
          return test.max_attempts
        }
      } else {
        return test.max_attempts
      }
    },
    time (test) {
//      console.log(test.passing.seconds_per_end)
      if (test.passing) {
        if (test.passing.seconds_per_end !== undefined && test.passing.seconds_per_end !== null) {
          var seconds = test.passing.seconds_per_end
          seconds = Math.ceil(seconds)
          var min = Math.floor(seconds / 60)
          var sec = seconds % 60
          return min.toString() + 'm, ' + sec.toString() + 's'
        } else {
          return null
        }
      }
    }
  },
  components: {
    'test-list-elem': TestListElem
  },
  created: function () {
    this.$store.dispatch('getTests')
    this.timer = setInterval(() => {
      this.$store.dispatch('getTests')
      for (var i = 0; i < this.tests.length; ++i) {
        var test = this.tests[i]
        if (test.passing) {
          if (test.passing.seconds_per_end !== undefined && test.passing.seconds_per_end !== null) {
            //          console.log('sjndj', test.passing.seconds_per_end)
            //          console.log(test.passing.seconds_per_end <= 0)
            if (test.passing.is_going) {
              if (test.passing.seconds_per_end <= 0) {
                this.$store.dispatch('stopPassing', test.passing.id)
              }
            }
          }
        }
      }
    }, 5000)
    this.$store.dispatch('getTestResults')
  },
  beforeDestroy: function () {
    clearInterval(this.timer)
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
