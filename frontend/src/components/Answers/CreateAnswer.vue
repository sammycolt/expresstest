<template>
<div class="panel">
  <div class="panel-header text-center">
    <div class="panel-title h5 mt-10">Create Answer</div>
  </div>
  <div class="panel-body">
    <div>
      <form class="form-horizontal">
        <div class="form-group">
          <div class="col-3">
            <label class="form-label">Text</label>
          </div>
          <div class="col-9">
            <input class="form-input "  type="text" v-model="text" placeholder="Type text...">
          </div>
        </div>
        <div class="form-group">
          <label class="form-switch">
            <input type="checkbox" v-model="isCorrect">
            <i class="form-icon"></i> Correct
          </label>
      </div>
      </form>
    </div>
  </div>
  <div class="panel-footer">
    <div class="form-group">
      <div>
        <button class="btn btn-primary btn-block" v-on:click="create">Create</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'create-answer',
  props: ['questionId'],
  data () {
    return {
      text: '',
      isCorrect: false
    }
  },
  methods: {
    create (event) {
      this.$store.dispatch('createAnswer', {
        'answerData': {
          'answer_text': this.text,
          'is_correct': this.isCorrect
        },
        'questionId': this.questionId
      })
      this.text = ''
      this.isCorrect = false
      event.preventDefault()
    }
  }
}
</script>
