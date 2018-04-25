<template>
<div class="panel" v-if="coursesDictionaryByName">
  <div class="panel-header text-center">
    <div class="panel-title h5 mt-10">Share test to course</div>
  </div>
  <div class="panel-body">
    <div>
      <form class="form-horizontal">
        <div class="form-group">
          <select class="form-select" v-model="cor">
            <option v-for="course in this.courses">{{ course.name }}</option>
          </select>
      </div>
      </form>
    </div>
  </div>
  <div class="panel-footer">
    <div class="form-group">
      <div>
        <button class="btn btn-primary btn-block" @click="share">Share</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>

import { mapGetters } from 'vuex'

export default{
  name: 'add-course',
  props: ['testId'],
  computed: mapGetters(['courses', 'coursesDictionaryByName']),
  data () {
    return {
      'cor': {}
    }
  },
  methods: {
    share (event) {
      var course1 = this.coursesDictionaryByName[this.cor]
      var payload = {
        'course': course1.id,
        'quiz': this.testId
      }
      this.$store.dispatch('addCourseToTest', payload)
      event.preventDefault()
    }
  },
  created: function () {
    this.$store.dispatch('getCourses').then(response => {
//      for (var i in this.students) {
//        this.studentsDictionaryByUsername[this.students[i].username] = this.students[i]
//      }
    })
  }

}
</script>
