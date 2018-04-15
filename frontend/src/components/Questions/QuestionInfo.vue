<template>
<section class="container grid-960">
  <div class="panel">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Question: {{ text }}</div>
      <div class="panel-default h5 mt-10">Answers:</div>
    </div>
  </div>
  <create-answer :questionId="this.id"></create-answer>
  <answer-list :questionId="this.id"></answer-list>
</section>
</template>

<script>

import { mapState } from 'vuex'
import CreateAnswer from '../Answers/CreateAnswer.vue'
import AnswerList from '../Answers/AnswerList.vue'

export default {
  name: 'question-info',
  components: {
    'create-answer': CreateAnswer,
    'answer-list': AnswerList
  },
  computed: mapState({
    text (state) {
      if (state.questionDetails[this.id]) {
        return state.questionDetails[this.id].text
      }
    }
  }),
  data () {
    return {
      id: this.$route.params.id
    }
  },
  created: function () {
    this.$store.dispatch('getQuestionDetails', this.id)
    console.log(this.$store.state.questionDetails[this.id])
  }
}
</script>
