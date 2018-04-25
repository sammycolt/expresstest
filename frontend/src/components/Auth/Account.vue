<template>
<div>

  <div v-if="checkType('student')">
    <test-list></test-list>
  </div>
  <div v-else-if="checkType('teacher')">
    <create-test></create-test>
    <test-list></test-list>
  </div>
</div>
</template>

<script>
import UsersList from './UsersList.vue'
import NoteList from '../Notes/NoteList.vue'
import CreateNote from '../Notes/CreateNote.vue'
import CreateTest from '../Tests/CreateTest.vue'
import TestList from '../Tests/TestList.vue'
import { UserType } from '../../enums/userType'
import AddStudent from '../Students/AddStudent.vue'
import {Tabs, Tab} from 'vue-tabs-component'

import { mapGetters } from 'vuex'

export default {
  name: 'account',
  components: {
    'tabs': Tabs,
    'tab': Tab,
    'users-list': UsersList,
    'note-list': NoteList,
    'create-note': CreateNote,
    'create-test': CreateTest,
    'test-list': TestList,
    'add-student': AddStudent
  },
  computed: mapGetters(['userInfo']),
  methods: {
    checkType (currType) {
      var type = this.userInfo['type']
      var typeToCheck = null
      if (currType === 'teacher') {
        typeToCheck = UserType.TEACHER
      } else {
        typeToCheck = UserType.STUDENT
      }
      return type === String(typeToCheck)
    }
  }
}
</script>
