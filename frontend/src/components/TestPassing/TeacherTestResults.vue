<template>
  <section class="container grid-960">

    <div class="panel" v-if="testResults && testDetails">
      <div class="panel-header text-center">
        <h3>Results: </h3>
        <table class="docs-table table table-striped text-center">
          <thead>
            <tr>
              <th></th>
              <th v-for="question in testDetails[testId].questions">{{question.text}}</th>
              <th>total</th>
              <th>%</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="result in testResults[testId]">
              <td class="text-left">{{studentsInfo[result.user].username}}</td>
              <td v-for="question in testDetails[testId].questions">
                <div v-if="checkCorrectness(result, question.id)">
                  {{ question.score }}
                </div>
                <div v-else="">
                  0
                </div>
              </td>
              <td>
                {{ result.total_score }}
              </td>
              <td>
                {{ Number((result.percentage * 100).toFixed(1)) }}
              </td>
            </tr>
          </tbody>
        </table>

        <!--<div class="card"  v-for="(result, index) in testResults[this.testId]">-->
          <!--<div class="card-header is-error" v-if="studentsInfo[result.user]">-->
            <!--<div class="card-title">Student: {{ studentsInfo[result.user].username }}</div>-->
            <!--<div class="card-body">-->
              <!--Score: {{ result.total_score }}-->
              <!--<br>-->
              <!--Percents: {{Number((result.percentage * 100).toFixed(1))}} %-->
            <!--</div>-->
          <!--</div>-->
        <!--</div>-->
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
    },
    testDetails (state) {
      return state.testDetails
    }
  }),
  methods: {
    checkCorrectness (result, questionId) {
      var found = false
      for (var i = 0; i < result.correct_questions.length; ++i) {
        var question = result.correct_questions[i]
        console.log(question.id, questionId)
        if (question.id === questionId) {
          found = true
        }
      }
      return found
    }
  },
  created: function () {
    this.$store.dispatch('getTestResults')
    this.$store.dispatch('getStudents')
  }
}
</script>
