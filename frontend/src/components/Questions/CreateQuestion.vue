<template>
<div class="panel">
  <div class="panel-header text-center">
    <div class="panel-title h5 mt-10">Add Question</div>
  </div>
  <div class="panel-body">
    <div>
      <form class="form-horizontal">
        <div class="form-group">
          <div class="col-9">
           <textarea class="form-input" v-model="body" rows="8" placeholder="Type your question..."></textarea>
          </div>
        </div>
        <div class="form-group">
          <div class="col-3">
            <label class="form-label">Score</label>
          </div>
          <div class="col-6">
            <input class="form-input" v-model="score" placeholder="Type score here...">
          </div>
        </div>
      </form>
    </div>
  </div>
  <div class="panel-footer">
    <div class="form-group">
      <div>
        <button class="btn btn-primary btn-block" @click="create">Create</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default{
  name: 'create-test',
  props: ['testId'],
  data () {
    return {
      'body': '',
      'score': 0
    }
  },
  methods: {
    create (event) {
      this.$store.dispatch('createQuestion', {
        'quiz': this.testId,
        'text': this.body
      })
      this.body = ''
      event.preventDefault()
    }
  }

}
</script>
