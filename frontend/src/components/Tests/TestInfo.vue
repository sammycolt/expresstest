<template>
<section class="container grid-960">
  <div class="panel">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Test: {{ title }}</div>
      <div class="panel-default h5 mt-10">Questions:</div>
    </div>
    <add-student :testId="this.id"></add-student>
    <create-question :testId="this.id"></create-question>
    <question-list :testId="this.id"></question-list>
  </div>
</section>
</template>

<script>

import { mapState } from 'vuex'
import CreateQuestion from '../Questions/CreateQuestion.vue'
import QuestionList from '../Questions/QuestionList.vue'
import AddStudent from '../Students/AddStudent.vue'

export default {
  name: 'test-info',
  components: {
    'create-question': CreateQuestion,
    'question-list': QuestionList,
    'add-student': AddStudent
  },
  computed: mapState({
    title (state) {
      if (state.testDetails[this.id]) {
        return state.testDetails[this.id].title
      }
    }
  }),
  data () {
    return {
      id: this.$route.params.id
    }
  },
  created: function () {
    this.$store.dispatch('getTestDetails', this.id)
    console.log(this.$store.state.testDetails[this.id])
  }
}
</script>
