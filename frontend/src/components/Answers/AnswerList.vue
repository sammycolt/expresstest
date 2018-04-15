<template>
  <div id="app">
    <div class="card" v-for="answer in this.answers">
      <div class="card-header">
        <div class="card-title">Text: {{ answer.answer_text }}</div>
        <div class="card-subtitle">Correct: {{ answer.is_correct }}</div>
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
  })
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
