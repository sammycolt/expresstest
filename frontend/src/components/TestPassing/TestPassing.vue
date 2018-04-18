<template>
<section class="container grid-960">
  <div class="panel">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Pass the test</div>
    </div>
    <div class="panel-body">
      <ul class="step">
        <li class="step-item" v-for="(question, index) in this.questions" :class="[index === questionIndex ? 'active' : '']"><a>{{index + 1}}</a></li>
      </ul>
      <div v-for="(question, index) in this.questions" class="step-item">
        <div v-show="index === questionIndex">
          <h4>{{ question.text }}</h4>
          <ol>
            <li v-for="answer in question.answers">
                <label class="form-checkbox">
                  <input type="checkbox">
                  <i class="form-icon"></i> {{answer.answer_text}}
                </label>
            </li>
          </ol>
        </div>
      </div>
    </div>
    <div class="panel-footer">
      <div class="form-group">
        <div>
          <button class="btn btn-primary btn-block" @click="next">Next</button>
        </div>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import { mapState } from 'vuex'

export default{
  name: 'test-passing',
  computed: mapState({
    questions (state) {
      if (state.testDetails[this.testId]) {
        return state.testDetails[this.testId].questions
      }
    }
  }),
  data () {
    return {
      'testId': this.$route.params.id,
      questionIndex: 0
    }
  },
  methods: {
    next () {
      this.questionIndex++
    }
  },
  created: function () {
    this.$store.dispatch('getTestDetails', this.testId)
  }
}
</script>
