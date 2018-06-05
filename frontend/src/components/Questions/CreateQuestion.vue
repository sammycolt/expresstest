<template>
<div class="panel">
  <div class="panel-header text-center">
    <div class="panel-title h5 mt-10">Add Question</div>
  </div>
  <div class="panel-body">
    <div>
      <form class="form-horizontal">
         <div class="form-group">
          <label class="form-switch">
            <input type="checkbox" v-model="use_wysiwyg">
            <i class="form-icon"></i> Use WYSIWYG
          </label>
        </div>
        <div class="form-group" v-if="use_wysiwyg === false">
          <div class="col-9">
           <textarea class="form-input" v-model="body" rows="8" placeholder="Type your question..."></textarea>
          </div>
        </div>
        <div class="form-group" v-else="">
          <div class="col-9">
           <wysiwyg v-model="body" placeholder="Enter your question..."/>
          </div>
        </div>
        <div class="form-group">
          <div class="col-4">
            <label class="form-label">Type</label>
          </div>
          <div class="col-5">
            <select class="form-select" v-model="type">
              <option value="0">Many Correct Answers</option>
              <option value="1">One Correct Answer</option>
              <option value="2">Open Answer</option>
            </select>
          </div>
        </div>

        <div class="form-group" v-if="type === '2'">
          <label class="form-switch">
            <input type="checkbox" v-model="use_checker">
            <i class="form-icon"></i> Use checker
          </label>
        </div>

        <div class="form-group" v-if="use_checker && type === '2'">
          <div class="col-4">
            <label class="form-label">Checker</label>
          </div>
          <div class="col-5">
            <select class="form-select" v-model="checker">
                <option v-for="name in this.checkerNames">{{name}}</option>
            </select>
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
import { mapState } from 'vuex'

export default{
  name: 'create-question',
  props: ['testId'],
  computed: mapState({
    checkerNames (state) {
      var names = []
      for (var i = 0; i < state.myCheckers.length; ++i) {
        names.push(state.myCheckers[i].name)
      }
      for (i = 0; i < state.otherCheckers.length; ++i) {
        names.push(state.otherCheckers[i].name)
      }
      return names
    },
    checkerDict (state) {
      return state.checkerDict
    }
  }),
  data () {
    return {
      'body': '',
      'score': 0,
      'type': 0,
      'use_checker': false,
      'checker': {},
      'use_wysiwyg': false
    }
  },
  methods: {
    create (event) {
      var payload = {
        'quiz': this.testId,
        'text': this.body,
        'score': this.score,
        'type': this.type.toString(),
        'use_checker': this.use_checker,
        'text_in_html': this.use_wysiwyg
      }
      if (this.use_checker === true) {
        payload['checker'] = this.checkerDict[this.checker].id
      }
      this.$store.dispatch('createQuestion', payload)
      this.body = ''
      event.preventDefault()
    }
  },
  created: function () {
    this.$store.dispatch('getCheckers')
  }

}
</script>
