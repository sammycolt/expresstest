<template>
  <div id="app">
    <div class="card" v-for="test in this.tests">
      <test-list-elem :title="test.title" :author="test.author" :id="test.id"></test-list-elem>
    </div>
  </div>
</template>


<script>
import { mapGetters } from 'vuex'
import TestListElem from './TestListElem.vue'

export default {
  name: 'note-list',
  computed: mapGetters(['tests']),
  components: {
    'test-list-elem': TestListElem
  },
  beforeMount () {
    this.$store.dispatch('getTests')
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
