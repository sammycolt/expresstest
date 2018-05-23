<template>
<div class="panel">
  <div class="panel-header text-center">
    <div class="panel-title h5 mt-10">Create Test</div>
  </div>
  <div class="panel-body">
    <div>
      <form class="form-horizontal">
        <div class="form-group">
          <div class="col-3">
            <label class="form-label">Title</label>
          </div>
          <div class="col-9">
            <input class="form-input "  type="text" v-model="title" placeholder="Type title...">
          </div>
        </div>

        <div class="form-group">
          <div class="col-3">
            <label class="form-label">Max time (minutes)</label>
          </div>
          <div class="col-9">
            <input class="form-input "  type="text" v-model="maxTime" placeholder="Enter max time...">
          </div>
        </div>

        <div class="form-group">
          <div class="col-3">
            <label class="form-label">Max num of attempts</label>
          </div>
          <div class="col-9">
            <input class="form-input "  type="text" v-model="maxAttempts" placeholder="Enter max attempts...">
          </div>
        </div>

        <div class="form-group">
          <div class="col-3">
            <label class="form-label">Scoring system</label>
          </div>
          <div class="col-9">
            <select class="form-select" v-model="scoringSystem">
              <option value="0">For everyone</option>
              <option value="1">For first</option>
            </select>
          </div>
        </div>

        <div class="form-group" v-if="scoringSystem === '1'">
          <div class="col-3">
            <label class="form-label">Num of winners</label>
          </div>
          <div class="col-9">
            <input class="form-input "  type="text" v-model="numOfFirsts" placeholder="Enter num of winners">
          </div>
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
export default{
  name: 'create-test',
  data () {
    return {
      'title': '',
      'maxTime': 2,
      'maxAttempts': 3,
      'scoringSystem': 0,
      'numOfFirsts': 1
    }
  },
  methods: {
    create (event) {
      this.$store.dispatch('createTest', {
        'title': this.title,
        'author': this.$store.getters.userInfo.id,
        'max_time': this.maxTime,
        'max_attempts': this.maxAttempts,
        'scoring_system': this.scoringSystem,
        'num_of_winners': this.numOfFirsts
      })
      event.preventDefault()
    }
  }

}
</script>
