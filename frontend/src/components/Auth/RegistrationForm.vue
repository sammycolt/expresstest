<template>
<form class="form-horizontal" @submit="submitForm">
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Username</label>
  </div>
  <div class="col-9">
    <input class="form-input " :class="usernameError" type="text" v-model="username" placeholder="Type your username..."/>
    <p class="form-input-hint">{{ usernameHint }}</p>
  </div>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Email</label>
  </div>
  <div class="col-9">
    <input class="form-input " :class="emailError" type="email" v-model="email" placeholder="Type your email..."/>
    <p class="form-input-hint">{{ emailHint }}</p>
  </div>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Password</label>
  </div>
  <div class="col-9">
    <input class="form-input " :class="password1Error" type="password" v-model="password1" placeholder="Type your password..."/>
    <p class="form-input-hint">{{ password1Hint }}</p>
  </div>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Repeat Password</label>
  </div>
  <div class="col-9">
    <input class="form-input " :class="password2Error" type="password" v-model="password2" placeholder="Repeat your password..."/>
    <p class="form-input-hint">{{ password2Hint }}</p>
  </div>
</div>
<div class="form-group">
  <div class="col-3">
    <label class="form-label">Type of user</label>
  </div>
  <div class="col-9">
    <select class="form-select" v-model="usertype">
      <option value="1">Student</option>
      <option value="0">Teacher</option>
    </select>
  </div>
</div>
<div class="form-group">
  <div class="col-3"></div>
  <div class="col-9">
    <button class="btn btn-primary" type="submit">Register</button>
  </div>
</div>
</form>
</template>

<script>
export default {
  name: 'register-user',
  data () {
    return {
      'username': 'sjnsdjks',
      'email': 'mfsdsd@mail.ru',
      'password1': 'kekbsjndnsd',
      'password2': 'sdfuhsdjsjd',
      'usertype': '1',
      usernameError: '',
      usernameHint: '',
      emailError: '',
      emailHint: '',
      password1Error: '',
      password1Hint: '',
      password2Error: '',
      password2Hint: ''
    }
  },
  methods: {
    clearErrors () {
      this.usernameError = ''
      this.usernameHint = ''
      this.emailError = ''
      this.emailHint = ''
      this.password1Error = ''
      this.password1Hint = ''
      this.password2Error = ''
      this.password2Hint = ''
    },
    clearFields () {
      this.username = ''
      this.email = ''
      this.password1 = ''
      this.password2 = ''
      this.usertype = '1'
    },
    clear () {
      this.clearFields()
      this.clearErrors()
    },
    submitForm (event) {
      this.clearErrors()
      var resp = this.registerUser()

      resp.then(() => {
        this.clear()
      }).catch(err => {
        if (err.response.status === 400) {
          console.log(err)
          if (err.response.data) {
            var currData = err.response.data
            console.log(currData)
            for (var elem in currData) {
              if (elem === 'username') {
                this.usernameHint = currData[elem][0]
                this.usernameError = 'is-error'
              }
              if (elem === 'email') {
                this.emailHint = currData[elem][0]
                this.emailError = 'is-error'
              }
              if (elem === 'password1') {
                this.password1Hint = currData[elem][0]
                this.password1Error = 'is-error'
              }
              if (elem === 'non_field_errors') {
                this.password1Error = 'is-error'
                this.password2Error = 'is-error'
                this.password1Hint = currData[elem][0]
                this.password2Hint = currData[elem][0]
              }
            }
          }
        } else {
          this.clear()
        }
      })
      event.preventDefault()
    },
    registerUser () {
      return this.$store.dispatch('registerUser', {
        'username': this.username,
        'email': this.email,
        'password1': this.password1,
        'password2': this.password2,
        'type': this.usertype
      }).then(() => {
        return Promise.resolve('Success')
      }).catch(function (error) {
        return Promise.reject(error)
      })
    }
  }
}
</script>
