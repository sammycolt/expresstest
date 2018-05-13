<template>
<div class="panel">
  <div class="panel-header text-center">
    <div class="panel-title h5 mt-10">Create Answer</div>
  </div>
  <div class="panel-body">
    <div>
      <form class="form-horizontal">
        <div class="form-group">
          <div class="col-3">
            <label class="form-label">Text</label>
          </div>
          <div class="col-9">
            <input class="form-input "  type="text" v-model="text" placeholder="Type text...">
          </div>
        </div>
        <div class="form-group">
          <label class="form-switch">
            <input type="checkbox" v-model="isCorrect">
            <i class="form-icon"></i> Correct
          </label>
      </div>
      </form>
    </div>
  </div>
  <div class="panel-footer">
    <div class="form-group">
      <div>
        <button class="btn btn-primary btn-block" v-on:click="create">Create</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'create-answer',
  props: ['questionId', 'quizId'],
  data () {
    return {
      text: '',
      isCorrect: false
    }
  },
  methods: {
    create (event) {
      var questions = this.$store.state.testDetails[this.quizId].questions
      var question = null
      for (var i = 0; i < questions.length; ++i) {
        if (questions[i].id === this.questionId) {
          question = questions[i]
        }
      }
      if (question.type === '1') {
        var numOCorrectAnswers = 0
        for (i = 0; i < question.answers.length; ++i) {
          if (question.answers[i].is_correct) {
            numOCorrectAnswers++
          }
        }
        if (numOCorrectAnswers > 0) {
          if (this.isCorrect) {
            alert('This type of question available only one correct answer')
            return
          }
        }
      }

//      console.log(question)
      this.$store.dispatch('createAnswer', {
        'answerData': {
          'answer_text': this.text,
          'is_correct': this.isCorrect
        },
        'questionId': this.questionId
      })
      this.text = ''
      this.isCorrect = false
      event.preventDefault()
    }
  },
  created: function () {
    this.$store.dispatch('getTestDetails', this.quizId)
  }
}
</script>
