<template>
  <section class="container grid-960">

    <div class="panel" v-if="testResults">
      <div class="panel-header text-center">
        <h3>Results: </h3>
        <div class="card"  v-for="(result, index) in testResults[this.testId]">
          <div class="card-header is-error" v-if="studentsInfo[result.user]">
            <div class="card-title">Student: {{ studentsInfo[result.user].username }}</div>
            <div class="card-body">
              Score: {{ result.total_score }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState } from 'vuex'

export default{
  name: 'teacher-test-results',
  props: ['testId'],
  computed: mapState({
    testResults (state) {
      return state.testResults
    },
    studentsInfo (state) {
      return state.studentsDictionaryById
    }
  }),
  created: function () {
    this.$store.dispatch('getTestResults')
    this.$store.dispatch('getStudents')
  }
}
</script>
