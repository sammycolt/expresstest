<template>
<section class="container grid-960">
  <div class="panel">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Test: {{ title }}</div>
    </div>
    <tabs>
      <tab name="Questions">
        <create-question :testId="this.id"></create-question>
        <question-list :testId="this.id"></question-list>
      </tab>
      <tab name="Share">
        <add-group :testId="this.id"></add-group>
        <add-student :testId="this.id"></add-student>
        <add-course :testId="this.id"></add-course>
      </tab>
      <tab name="Results">
        <teacher-test-results :testId="this.id"></teacher-test-results>
      </tab>
    </tabs>
  </div>
</section>
</template>

<script>

import { mapState } from 'vuex'
import CreateQuestion from '../Questions/CreateQuestion.vue'
import QuestionList from '../Questions/QuestionList.vue'
import AddStudent from '../Students/AddStudent.vue'
import TeacherTestResults from '../TestPassing/TeacherTestResults.vue'
import AddGroup from '../Groups/AddGroup.vue'
import AddCourse from '../Courses/AddCourse.vue'
import {Tabs, Tab} from 'vue-tabs-component'

export default {
  name: 'test-info',
  components: {
    'create-question': CreateQuestion,
    'question-list': QuestionList,
    'add-student': AddStudent,
    'teacher-test-results': TeacherTestResults,
    'add-group': AddGroup,
    'add-course': AddCourse,
    'tabs': Tabs,
    'tab': Tab
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
//    console.log(this.$store.state.testDetails[this.id])
  }
}
</script>
