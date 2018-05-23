<template>
<section class="container grid-960">
  <div class="panel" v-if="results">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Result: {{results[this.testId][0].total_score}}</div>
       <div class="panel-title h3 mt-10">Percents: {{Number((results[this.testId][0].percentage * 100).toFixed(1))}} %</div>
      <div class="panel-title h3 mt-10" v-if="results[this.testId][0].remaining_time > 0">Time: {{calculateTime(results[this.testId][0].remaining_time)}}</div>
    </div>
  </div>

  <div class="panel" v-if="results && questions">

    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">{{this.title}}</div>
    </div>
    <div class="panel-body">
      <ul class="step">
        <li class="step-item" v-for="(question, index) in this.questions" :class="[index === questionIndex ? 'active' : '']" @click="setIndex(index)">
          <a>{{index + 1}}</a>
        </li>
      </ul>
      <div v-for="(question, index) in this.questions" class="step-item">
        <div v-show="index === questionIndex">
          <h5>{{ question.text }}</h5>
          <span class="label label-primary" v-bind:class="correctClass(question)">{{ correctLabel(question) }}</span>
        </div>
      </div>
    </div>
    <div class="panel-footer form-horizontal">
      <div class="form-group">
        <div class="col-2">
          <button v-if="questionIndex > 0" class="btn btn-primary btn-block" @click="prev">Prev</button>
        </div>
        <div class="col-8"></div>
        <div class="col-2">
          <button v-if="questionIndex < questions.length - 1" class="btn btn-primary btn-block" @click="next">Next</button>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import { mapState } from 'vuex'

export default{
  name: 'test-results-in-detail',
  computed: mapState({
    questions (state) {
      if (state.testDetails[this.testId]) {
        return state.testDetails[this.testId].questions
      }
    },
    title (state) {
      if (state.testDetails[this.testId]) {
        return state.testDetails[this.testId].title
      }
    },
    givenAnswers (state) {
      return state.givenAnswers
    },
    results (state) {
      return state.testResults
    }
  }),
  data () {
    return {
      'testId': this.$route.params.id,
      questionIndex: 0
    }
  },
  methods: {
    next () {
      this.setIndex(this.questionIndex + 1)
    },
    prev () {
      this.setIndex(this.questionIndex - 1)
    },
    setIndex (value) {
      if ((value >= 0) && (value < this.questions.length)) {
        this.questionIndex = value
      }
    },
    calculateTime (seconds) {
      if (seconds > 0) {
        seconds = Math.ceil(seconds)
        var min = Math.floor(seconds / 60)
        var sec = seconds % 60
        return min.toString() + 'm, ' + sec.toString() + 's'
      }
    },
    correctClass (question) {
      var label = this.correctLabel(question)
      if (label === 'Correct, first') {
        return 'label-success'
      } else if (label === 'Incorrect') {
        return 'label-error'
      } else {
        return 'label-warning'
      }
    },
    correctLabel (question) {
      var found = 0
      for (var i = 0; i < this.results[this.testId][0].questions.length; ++i) {
        if (this.results[this.testId][0].questions[i].question.id === question.id) {
          if (this.results[this.testId][0].questions[i].show_in_res === true) {
            found = 1
          } else {
            found = 2
          }
        }
      }
      if (found === 1) {
        return 'Correct, first'
      } else if (found === 0) {
        return 'Incorrect'
      } else {
        return 'Correct, not first'
      }
    }
  },
  created: function () {
    this.$store.dispatch('getTestDetails', this.testId)
    this.$store.dispatch('getTestResults')
    setTimeout(() => {
      this.$store.dispatch('getTestResults')
    }, 500)
  }
}
</script>
