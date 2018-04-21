<template>
  <div id="app">
    <h4>Available tests:</h4>
    <div class="card" v-for="test in this.tests">
      <test-list-elem :title="test.title" :author="test.author" :id="test.id" :questionsCount="test.questions.length"></test-list-elem>
    </div>
  </div>
</template>


<script>
import { mapGetters } from 'vuex'
import TestListElem from './TestListElem.vue'

export default {
  name: 'test-list',
  computed: mapGetters(['tests']),
  components: {
    'test-list-elem': TestListElem
  },
  created: function () {
    this.$store.dispatch('getTests')
    this.$store.dispatch('getTestResults')
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
