<template>
  <div id="app">
    <div class="card" v-for="question in this.questions">
      <div class="card-header" @click="onClick(question)">
        <div class="card-title">Text: {{ question.text }}</div>
        <div class="card-subtitle">Answers: {{ question.answers.length }}</div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
  name: 'question-list',
  props: ['testId'],
  computed: mapState({
    questions (state) {
      if (state.testDetails[this.testId]) {
        return state.testDetails[this.testId].questions
      }
    }
  }),
  methods: {
    onClick (q) {
      alert(q)
    }
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
