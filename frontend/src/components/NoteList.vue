<template>
  <div id="app">
    <div class="card" v-for="note in notes">
      <div class="card-header">
        <button class="btn btn-clear float-right" v-on:click="deleteNote(note)"></button>
        <div class="card-title">{{ note.title }}</div>
        <div class="card-subtitle">{{ convertDateToTimeAgo(note.created_at) }}</div>
      </div>
      <div class="card-body">{{ note.body }}</div>
    </div>
  </div>
</template>


<script>
import { mapGetters } from 'vuex'
import prettydate from 'pretty-date'

export default {
  name: 'note-list',
  computed: mapGetters(['notes']),
  methods: {
    convertDateToTimeAgo (date) {
      return prettydate.format(new Date(date))
    },
    deleteNote (note) {
      console.log(this.notes)
      this.$store.dispatch('deleteNote', note)
    }
  },
  beforeMount () {
    this.$store.dispatch('getNotes')
  }
}
</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
