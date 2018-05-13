<template>
  <section class="container grid-960">

    <div class="panel" v-if="testResults && testDetails && groupsInfo && studentsInfo">
      <div class="panel-header text-center">
        <h3>Results: </h3>
          <table class="docs-table table table-striped text-center">
            <thead>
              <tr>
                <th></th>
                <th></th>
                <th v-for="question in testDetails[testId].questions" class="tooltip" :data-tooltip="question.text">{{question.text.substring(0, question.text.length >= 5 ? 5 : question.text.length)}}</th>
                <th>total</th>
                <th>%</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="result in testResults[testId]">
                <td>{{calculateGroups(result.user)}}</td>
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
        </div>
        <center>
          <div v-if="testDetails && testResults" style="max-width: 400px; max-height: 400px">
            <results-chart :chart-data="this.chartData"></results-chart>
          </div>
        </center>

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
  </section>
</template>

<script>
import { mapState } from 'vuex'
import ResultsChart from './ResultsChart.vue'

export default{
  name: 'teacher-test-results',
  props: ['testId'],
  components: {
    'results-chart': ResultsChart
  },
  computed: mapState({
    testResults (state) {
      return state.testResults
    },
    studentsInfo (state) {
      return state.studentsDictionaryById
    },
    testDetails (state) {
      return state.testDetails
    },
    groupsInfo (state) {
      return state.groupsDictionaryById
    },
    groups (state) {
      return state.groups
    },

    calculateLabelsForChart (state) {
      var labels = []
      var testId = this.testId
//      console.log('Kek' + this.testId.toString())
      for (var i = 0; i < state.testDetails[testId].questions.length; ++i) {
        var question = state.testDetails[testId].questions[i]
        labels.push(question.text.substring(0, question.text.length >= 5 ? 5 : question.text.length))
      }
      return labels
    },
    calculateDataSets (state) {
      var dataset1 = {
        label: 'Correct answers',
        backgroundColor: '#f87979',
        data: []
      }
      var dataset2 = {
        label: 'Incorrect answers',
        backgroundColor: '#0000ff',
        data: []
      }
      var testId = this.testId
//      console.log(this.testDetails)
      for (var j = 0; j < state.testDetails[testId].questions.length; ++j) {
        dataset1.data.push(0)
        dataset2.data.push(0)
      }
      for (var i = 0; i < state.testResults[testId].length; ++i) {
        var result = state.testResults[testId][i]
        for (j = 0; j < state.testDetails[testId].questions.length; ++j) {
          var question = state.testDetails[testId].questions[j]
          if (this.checkCorrectness(result, question.id)) {
            dataset1.data[j] += 1
          } else {
            dataset2.data[j] += 1
          }
        }
      }
      return [
        dataset1,
        dataset2
      ]
    },
    chartData (state) {
      return {
        'labels': this.calculateLabelsForChart,
        'datasets': this.calculateDataSets
      }
    }
  }),
  methods: {
    checkCorrectness (result, questionId) {
      var found = false
      for (var i = 0; i < result.correct_questions.length; ++i) {
        var question = result.correct_questions[i]
        if (question.id === questionId) {
          found = true
        }
      }
      return found
    },
    calculateGroups (student) {
//      console.log(student)
//      var ans = ''
//      console.log(this.studentsInfo[student])
//      var groups = this.studentsInfo[student].group_set
//      for (var i = 0; i < groups.length - 1; ++i) {
//        console.log(groups[i], this.groupsInfo[groups[i]])
//       ans += this.groupsInfo[groups[i]].name + ', '
//      }
//      ans += this.groupsInfo[groups[groups.length - 1]].name
//      return ans
    }
  },
  created: function () {
    this.$store.dispatch('getTestResults')
    this.$store.dispatch('getStudents')
    this.$store.dispatch('getGroups')
  }
}
</script>
