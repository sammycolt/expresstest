
<template>
  <div>
    <div class="card"  v-for="student in this.students">
      <div class="card-header is-error">
        <button class="btn btn-clear float-right" @click="deleteStudent(student.id)"></button>
        <div class="card-title">Student: {{ studentDetails[student.id].username }}</div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
  name: 'students-list',
  props: ['testId'],
  computed: mapState({
    students (state) {
      if (state.testDetails[this.testId]) {
        return state.testDetails[this.testId].readers
      }
    },
    studentDetails (state) {
      return state.studentsDictionaryById
    },
    studentToTests (state) {
      return state.userToTests
    }
  }),
  methods: {
    deleteStudent (studentId) {
      var payload = {
        'id': this.studentToTests[this.testId][studentId],
        'test': this.testId
      }
//      console.log('delete')
      this.$store.dispatch('deleteUserToTest', payload)
    }
  }
}
</script>
