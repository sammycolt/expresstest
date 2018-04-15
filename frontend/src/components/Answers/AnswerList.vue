<template>
  <div id="app">
    <div class="card"  v-for="answer in this.answers">
      <div class="card-header is-error">
        <div class="card-title">Text: {{ answer.answer_text }}</div>
        <div class="card-subtitle">
          <span class="label label-primary" v-bind:class="correctClass(answer.is_correct)">{{ correctLabel(answer.is_correct) }}</span>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
  name: 'question-list',
  props: ['questionId'],
  computed: mapState({
    answers (state) {
      if (state.questionDetails[this.questionId]) {
        return state.questionDetails[this.questionId].answers
      }
    }
  }),
  methods: {
    correctClass (isCorrect) {
      if (isCorrect) {
        return 'label-success'
      } else {
        return 'label-error'
      }
    },
    correctLabel (isCorrect) {
      if (isCorrect) {
        return 'Correct'
      } else {
        return 'Incorrect'
      }
    }
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
