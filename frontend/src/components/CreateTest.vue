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
      'title': ''
    }
  },
  methods: {
    create (event) {
      this.$store.dispatch('createTest', {
        'title': this.title,
        'author': this.$store.getters.userInfo.id
      })
      event.preventDefault()
    }
  }

}
</script>
