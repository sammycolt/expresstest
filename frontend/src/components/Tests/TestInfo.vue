<template>
<section class="container grid-960">
  <div class="panel">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Test: {{ title }}</div>
    </div>

    <ul class="tab tab-block">
      <li class="tab-item" :class="isActive(1)">
        <a @click="setTabIndex(1)">Questions</a>
      </li>
      <li class="tab-item" :class="isActive(2)">
        <a @click="setTabIndex(2)">Share</a>
      </li>
      <li class="tab-item" :class="isActive(3)">
        <a @click="setTabIndex(3)">Results</a>
      </li>
      <li class="tab-item" :class="isActive(4)">
        <a @click="setTabIndex(4)">Checkers</a>
      </li>
    </ul>

    <div v-if="tabIndex === 1">
      <create-question :testId="this.id"></create-question>
      <question-list :testId="this.id"></question-list>
    </div>
    <div v-else-if="tabIndex === 2">
      <add-course :testId="this.id"></add-course>

      <add-group :testId="this.id"></add-group>
      <add-student :testId="this.id"></add-student>
    </div>
    <div v-else-if="tabIndex === 3">
      <teacher-test-results :testId="this.id"></teacher-test-results>
    </div>
    <div v-else-if="tabIndex === 4">
      <add-checker></add-checker>
        <checker-list></checker-list>
    </div>
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
import CheckerList from '../Checkers/ChekerList.vue'
import AddChecker from '../Checkers/AddCheker.vue'

export default {
  name: 'test-info',
  components: {
    'create-question': CreateQuestion,
    'question-list': QuestionList,
    'add-student': AddStudent,
    'teacher-test-results': TeacherTestResults,
    'add-group': AddGroup,
    'add-course': AddCourse,
    'checker-list': CheckerList,
    'add-checker': AddChecker
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
      'id': this.$route.params.id,
      tabIndex: 1
    }
  },
  methods: {
    setTabIndex (index) {
      this.tabIndex = index
    },
    isActive (index) {
      if (this.tabIndex === index) {
        return 'active'
      }
    }
  },
  created: function () {
    this.$store.dispatch('getTestDetails', this.id)
//    console.log(this.$store.state.testDetails[this.id])
  }
}
</script>
