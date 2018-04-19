<template>
<section class="container grid-960">
  <div class="panel" v-if="givenAnswers && !this.showResults && questions">
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
          <ol>
            <li v-for="(answer, index2) in question.answers">
              <!--{{givenAnswers}}-->
                <label class="form-checkbox">
                  <input type="checkbox" v-model="givenAnswers[question.id][answer.id].given" @change="change(givenAnswers[question.id][answer.id].given, answer.id, question.id)">
                  <i class="form-icon"></i> {{answer.answer_text}}
                </label>
            </li>
          </ol>
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
      <div v-if="questionIndex === questions.length - 1">
        <button class="btn btn-primary btn-block" @click="finish">Finish test</button>
      </div>
    </div>
  </div>
  <student-test-results v-if="this.showResults" :testId="this.testId"></student-test-results>
</section>
</template>

<script>
import { mapState } from 'vuex'
import TestResults from './StudentTestResults.vue'

export default{
  name: 'test-passing',
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
    }
  }),
  data () {
    return {
      'testId': this.$route.params.id,
      'showResults': false,
      questionIndex: 0
    }
  },
  components: {
    'student-test-results': TestResults
  },
  methods: {
    next () {
      this.setIndex(this.questionIndex + 1)
      this.submit()
    },
    prev () {
      this.setIndex(this.questionIndex - 1)
      this.submit()
    },
    finish () {
      this.submit()
      this.showResults = true
    },
    submit () {
//      console.log(this.questions.length)
      for (var i = 0; i < this.questions.length; ++i) {
        for (var j = 0; j < this.questions[i].answers.length; ++j) {
          if (this.givenAnswers[this.questions[i].id][this.questions[i].answers[j].id].given) {
            this.$store.dispatch('addAnswerByUser', {
              'user': this.$store.state.userInfo.id,
              'answer': this.questions[i].answers[j].id
            })
          }
        }
      }
    },
    setIndex (value) {
      console.log(this.questionIndex, value)
      if ((value >= 0) && (value < this.questions.length)) {
        this.questionIndex = value
      }
      console.log(this.questionIndex)
    },
    change (given, answerId, questionId) {
      if (given) {
        this.$store.dispatch('addAnswerByUser', {
          'user': this.$store.state.userInfo.id,
          'answer': answerId
        })
      } else {
//        console.log('unChange')
        var abuId = this.givenAnswers[questionId][answerId].answerByUserId
//        console.log(abuId)
        this.$store.dispatch('deleteAnswerByUser', abuId)
      }
    }
  },
  created: function () {
    this.$store.dispatch('getTestDetails', this.testId)
  }
}
</script>
