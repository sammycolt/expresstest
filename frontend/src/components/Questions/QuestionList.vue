<template>
  <div id="app">
    <div class="card" v-for="question in this.questions">
      <div class="card-header">
        <button class="btn btn-clear float-right" @click="deleteQuestion(question.id)"></button>
        <div class="card-title" @click="onClick(question)" v-if="!question.text_in_html">Text: {{ question.text }}</div>
        <div class="card-title" @click="onClick(question)" v-else="" v-html="question.text"></div>
        <div class="card-subtitle" @click="onClick(question)">Answers: {{ question.answers.length }}</div>
        <div class="card-subtitle" @click="onClick(question)">Score: {{ question.score }}</div>
        <div class="card-subtitle" @click="onClick(question)">Type: {{ type(question.type) }}</div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'
import { QuestionType } from '../../enums/questionType'

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
    onClick (question) {
      this.$router.push({name: 'QuestionInfo', params: { 'id': question.id, 'testId': this.testId }})
    },
    deleteQuestion (questionId) {
      var payload = {
        'questionId': questionId,
        'testId': this.testId
      }
      this.$store.dispatch('deleteQuestion', payload)
    },
    type (questionType) {
      console.log(QuestionType)
      try {
        return QuestionType.properties[questionType].name
      } catch (err) {
        return QuestionType.properties[1].name
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
