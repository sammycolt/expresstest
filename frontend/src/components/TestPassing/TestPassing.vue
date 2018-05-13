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
          <div v-if="question.type === '0'">
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
          <div v-else-if="question.type === '1'">
            <ol>
              <li v-for="(answer, index2) in question.answers">
                <label class="form-radio">
                  <input type="radio" :value="answer.id" v-model="givenAnswers[question.id].given" @click="update(question.id)">
                  <i class="form-icon"></i> {{answer.answer_text}}
                </label>
              </li>
            </ol>
          </div>
          <div v-else-if="question.type === '2'">
              <input class="form-input" type="text" placeholder="Answer..." v-model="givenAnswers[question.id].textInput">
          </div>
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
    },
    results (state) {
      return state.testResults
    }
  }),
  data () {
    return {
      'testId': this.$route.params.id,
      'showResults': false,
      'textInput': '',
      questionIndex: 0
    }
  },
  components: {
    'student-test-results': TestResults
  },
  methods: {
    next () {
      this.setIndex(this.questionIndex + 1)
    },
    prev () {
      this.setIndex(this.questionIndex - 1)
    },
    finish () {
      this.showResults = true
      this.submit()
    },
    submit () {
//      console.log(this.questions.length)
      for (var i = 0; i < this.questions.length; ++i) {
        if (this.questions[i].type === '1') {
          this.update(this.questions[i].id)
        } else {
          if (this.questions[i].type === '2') {
            this.processInput(this.questions[i])
          }
        }
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
      this.submit()
      if ((value >= 0) && (value < this.questions.length)) {
        this.questionIndex = value
      }
      console.log(this.questionIndex)
    },
    processInput (question) {
      var isCorrect = false
      var corrAnsId = 0
      for (var i = 0; i < question.answers.length; ++i) {
        var answer = question.answers[i]
        if (answer.answer_text === this.givenAnswers[question.id].textInput) {
          isCorrect = true
          corrAnsId = answer.id
        }
      }
      if (isCorrect) {
        this.givenAnswers[question.id][corrAnsId].given = true
      }
//      console.log(isCorrect)
    },
    update (questionId) {
      var a = this.givenAnswers[questionId].given
      for (var i = 0; i < this.givenAnswers[questionId].length; ++i) {
        var answer = this.givenAnswer[questionId][i]
        if (answer.given) {
          this.change(false, answer.id, questionId)
          this.givenAnswers[questionId][answer.id].given = false
        }
      }
      if (a) {
        this.change(true, a, questionId)
        this.givenAnswers[questionId][a].given = true
      }
//      console.log(a)
    },
    change (given, answerId, questionId) {
      if (given) {
        if (answerId !== 'false') {
//          console.log(answerId)
          this.$store.dispatch('addAnswerByUser', {
            'user': this.$store.state.userInfo.id,
            'answer': answerId
          })
        }
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
    if (this.results[this.testId]) {
      this.$store.dispatch('removeTestResults', {
        'testId': this.testId,
        'resultId': this.results[this.testId][0].id
      })
    }
  }
}
</script>
