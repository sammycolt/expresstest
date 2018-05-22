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
                <th>Time</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="result in filterResults[testId]">
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
                <td>
                  {{ calculateTime(result.remaining_time) }}
                </td>
              </tr>
              <tr>
                <td>
                  Average
                </td>
                <td>
                </td>
                <td>
                </td>
                <td>
                </td>
                <td>
                </td>
                <td>
                </td>
                <td>
                </td>
                <td>
                </td>
                <td>
                </td>
                <td>
                  {{ averageTime(filterResults[testId]) }}
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
    filterResults (state) {
      var set = new Set()
      var ans = {}
      for (var i = 0; i < this.testResults[this.testId].length; ++i) {
        var result = this.testResults[this.testId][i]
        if (!set.has(result.user)) {
//          console.log('add')
          set.add(result.user)
          if (!ans[this.testId]) {
            ans[this.testId] = [result]
          } else {
            ans[this.testId].push(result)
          }
        }
      }
//      console.log(ans)
      return ans
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
      console.log('!!!', this.filterResults[testId].length)
      for (var i = 0; i < this.filterResults[testId].length; ++i) {
        var result = this.filterResults[testId][i]
        for (j = 0; j < this.testDetails[testId].questions.length; ++j) {
          var question = this.testDetails[testId].questions[j]
//          console.log(this.checkCorrectness(result, question.id))
          if (this.checkCorrectness(result, question.id)) {
//            console.log('*')
            dataset1.data[j] += 1
          } else {
//            console.log('%')
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
    averageTime (results) {
      var sum = 0
      for (var i = 0; i < results.length; ++i) {
        sum += results[i].remaining_time
      }
      return this.calculateTime(sum / results.length)
    },
    calculateTime (seconds) {
      if (seconds > 0) {
        if (this.testDetails[this.testId].max_time * 60 < seconds) {
          seconds = this.testDetails[this.testId].max_time * 60
        }
        seconds = Math.ceil(seconds)
        var min = Math.floor(seconds / 60)
        var sec = seconds % 60
        return min.toString() + 'm, ' + sec.toString() + 's'
      }
    },
    calculateGroups (student) {
//      console.log(student)
      var ans = ''
//      console.log(this.studentsInfo[student])
      var groups = this.studentsInfo[student].group_set
      for (var i = 0; i < groups.length - 1; ++i) {
        ans += this.groupsInfo[groups[i]].name + ', '
      }
      ans += this.groupsInfo[groups[groups.length - 1]].name
      return ans
    }
  },
  created: function () {
    this.$store.dispatch('getTestResults')
    this.$store.dispatch('getStudents')
    this.$store.dispatch('getGroups')
    this.timer1 = setInterval(() => {
//      console.log('Kek')
      this.$store.dispatch('getTestResults')
    }, 2000)
  },
  beforeDestroy: function () {
    clearInterval(this.timer1)
  }
}
</script>
