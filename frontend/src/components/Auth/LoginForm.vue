<template>
<div>
  <form class="form-horizontal">
    <div class="form-group">
      <div class="col-3">
        <label class="form-label">Username</label>
      </div>
      <div class="col-9">
        <input class="form-input " :class="isError" type="text" v-model="username" placeholder="Type your username...">
      </div>
    </div>
    <div class="form-group">
      <div class="col-3">
        <label class="form-label">Password</label>
      </div>
      <div class="col-9">
        <input class="form-input " type="password" :class="isError" v-model="password" placeholder="Type your password...">
      </div>
    </div>
    <div class="form-group">
      <div>
        <button class="btn btn-primary btn-block" v-on:click="login">Login</button>
      </div>
    </div>
  </form>
</div>
</template>

<script>
export default {
  name: 'login-form',
  data () {
    return {
      'username': '',
      'password': '',
      'isError': ''
    }
  },
  methods: {
    login (event) {
      this.$store.dispatch('loginUser', {
        'username': this.username,
        'password': this.password
      }).then(resp => {
        this.username = ''
        this.password = ''
      }).catch(err => {
        if (err.response.data) {
          for (var elem in err.response.data) {
            if (elem === 'non_field_errors') {
              this.isError = 'is-error'
            }
          }
        }
      })
      event.preventDefault()
    }
  }
}
</script>
