<template>
<div class="panel">
  <div class="panel-header text-center">
    <div class="panel-title h5 mt-10">Share test to student</div>
  </div>
  <div class="panel-body">
    <div>
      <form class="form-horizontal">
        <div class="form-group">
          <select class="form-select" v-model="stdnt">
            <option v-for="student in this.students">{{ student.username }}</option>
          </select>
      </div>
      </form>
    </div>
  </div>
  <div class="panel-footer">
    <div class="form-group">
      <div>
        <button class="btn btn-primary btn-block" v-on:click="share">Share</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>

import { mapGetters } from 'vuex'

export default{
  name: 'add-student',
  props: ['testId'],
  computed: mapGetters(['students']),
  data () {
    return {
      'stdnt': {},
      'studentsDictionary': {}
    }
  },
  methods: {
    share (event) {
      var student1 = this.studentsDictionary[this.stdnt]
      console.log(this.studentsDictionary)
      console.log(this.stdnt)
      console.log(this.studentsDictionary[this.stdnt])
      console.log(student1)
      var payload = {
        'user': student1.id,
        'quiz': this.testId
      }
      this.$store.dispatch('addUserToTest', payload)
      event.preventDefault()
    }
  },
  created: function () {
    this.$store.dispatch('getStudents').then(response => {
      for (var i in this.students) {
        this.studentsDictionary[this.students[i].username] = this.students[i]
      }
    })
  }

}
</script>
