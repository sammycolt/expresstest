<template>
<div>
  <nav class="navbar">
    <section class="navbar-section"></section>
    <section class="navbar-center"></section>
    <section class="navbar-section">
      <a class="btn btn-default" v-on:click="logout()">Logout</a>
    </section>
  </nav>
  <note-list v-if="checkType('student')"></note-list>
  <div v-else-if="checkType('teacher')">
    <create-test></create-test>
    <test-list></test-list>
  </div>
</div>
</template>

<script>
import UsersList from './UsersList.vue'
import NoteList from './NoteList.vue'
import CreateNote from './CreateNote.vue'
import CreateTest from './CreateTest.vue'
import TestList from './TestList.vue'
import { UserType } from '../enums/userType'

import { mapGetters } from 'vuex'

export default {
  name: 'account',
  components: {
    'users-list': UsersList,
    'note-list': NoteList,
    'create-note': CreateNote,
    'create-test': CreateTest,
    'test-list': TestList
  },
  computed: mapGetters(['userInfo']),
  methods: {
    logout () {
      this.$store.dispatch('logoutUser')
    },
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
