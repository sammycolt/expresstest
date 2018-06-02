<template>
  <div>
    <div class="card"  v-for="course in this.courses">
      <div class="card-header is-error">
        <button class="btn btn-clear float-right" @click="deleteCourse(course)"></button>
        <div class="card-title">Course: {{ courseDetails[course].name }}</div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
  name: 'courses-list',
  props: ['testId'],
  computed: mapState({
    courses (state) {
      if (state.testDetails[this.testId]) {
        return state.testDetails[this.testId].courses
      }
    },
    courseDetails (state) {
      return state.coursesDictionaryById
    },
    courseToTests (state) {
      return state.courseToTests
    }
  }),
  methods: {
    deleteCourse (courseId) {
      var payload = {
        'id': this.courseToTests[this.testId][courseId],
        'test': this.testId
      }
//      console.log('delete')
      this.$store.dispatch('deleteCourseToTest', payload)
    }
  }
}
</script>
