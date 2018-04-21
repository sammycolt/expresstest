<template>
  <div class="panel">
    <div class="panel-header text-center">
      <div class="panel-title h5 mt-10">Express Test</div>
      <div class="panel-subtitle">Login</div>
    </div>
    <div class="panel-body">
      <div class="columns">
        <div class="column">
          <login-form></login-form>
        </div>
        <div class="divider-vert" data-content="OR"></div>
        <div class="column">
          <register-user></register-user>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from './LoginForm.vue'
import RegistrationForm from './RegistrationForm.vue'

export default {
  name: 'auth',
  components: {
    'login-form': LoginForm,
    'register-user': RegistrationForm
  }
}
</script>
