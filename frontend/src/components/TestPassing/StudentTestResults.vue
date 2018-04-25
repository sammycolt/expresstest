<template>
  <section class="container grid-960">
    <div class="panel" v-if="testResults[this.testId]">
      <div class="panel-header text-center">
        <div class="panel-title h5 mt-10">Result: {{testResults[this.testId][0].total_score}}</div>
         <div class="panel-title h3 mt-10">Percents: {{Number((testResults[this.testId][0].percentage * 100).toFixed(1))}} %</div>
      </div>
    </div>
    <div class="panel" v-else="">
      <div class="panel-header text-center">
        <div class="panel-title h5 mt-10">Result: 0</div>
      </div>
    </div>
  </section>
</template>

<script>
import { mapState } from 'vuex'

export default{
  name: 'student-test-results',
  props: ['testId'],
  computed: mapState({
    testResults (state) {
      return state.testResults
    }
  }),
  created: function () {
    this.$store.dispatch('getTestResults')
  }
}
</script>
