<template>
<form class="form-horizontal" @submit="submitForm">
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Title</label>
  </div>
  <div class="col-9">
    <input class="form-input" type="text" v-model="title" placeholder="Type note title..."/>
  </div>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Body</label>
  </div>
  <div class="col-9">
    <textarea class="form-input" v-model="body" rows="8" placeholder="Type your note..."></textarea>
  </div>
</div>
<div class="form-group">
  <div class="col-3"></div>
  <div class="col-9">
    <button class="btn btn-primary" type="submit">Create</button>
  </div>
</div>
</form>
</template>

<script>
export default {
  name: 'create-note',
  data () {
    return {
      'title': '',
      'body': ''
    }
  },
  methods: {
    submitForm (event) {
      this.createNote()
      this.title = ''
      this.body = ''
      event.preventDefault()
    },
    createNote () {
      this.$store.dispatch('createNote', { title: this.title, body: this.body })
    }
  }
}
</script>

<style>
</style>
