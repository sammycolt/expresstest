<template>

  <nav class="navbar container grid-960">
    <section class="navbar-section" v-if="showModal === false">
      <a v-if="notStartPage" class="btn btn-default" @click="goStart()">Main page</a>
      <a v-if="notStartPage" class="btn btn-default" @click="goBack()">Back</a>
    </section>
    <section class="navbar-center" v-if="showModal === false">
      <div class="chip">
          <img :src="image" class="avatar avatar-lg" v-if="userType === '1'">
          User: {{this.username}}
      </div>
    </section>
    <section class="navbar-section" v-if="showModal === false">

      <a class="btn btn-default" @click="showModal = true" v-if="userType === '1'">Select avatar</a>
      <a class="btn btn-default" @click="logout()">Logout</a>
    </section>

  <div class="modal modal-sm active" v-if="showModal === true">
    <div class="modal-container">
      <div class="modal-header">
        <a class="btn btn-clear float-right" aria-label="Close" @click="showModal = false"></a>
        <div class="modal-title h5">Select avatar for user</div>
      </div>
      <div class="modal-body">
        <div class="content">
          <vue-base64-file-upload
            accept="image/png,image/jpeg"
            placeholder="Select image"
            :max-size="customImageMaxSize"
            @size-exceeded="onSizeExceeded"
            @load="onAvatarLoaded"
            />
        </div>
      </div>
    </div>
  </div>
  </nav>
</template>

<script>

import { mapState } from 'vuex'
import VueBase64FileUpload from 'vue-base64-file-upload'

export default {
  name: 'navbar',
  components: {
    VueBase64FileUpload
  },
  computed: mapState({
    notStartPage (state) {
      return this.$route.path !== '/'
    },
    username (state) {
      return state.userInfo.username
    },
    userId (state) {
      return state.userInfo.id
    },
    avatar (state) {
      return state.userInfo.avatar
    },
    userType (state) {
      return state.userInfo.type
    }
  }),
  data () {
    return {
      customImageMaxSize: 3,
      showModal: false,
      image: ''
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('logoutUser')
      this.$router.push({name: 'Start'})
    },
    goBack () {
      window.history.length > 1
        ? this.$router.go(-1)
        : this.$router.push('/')
    },
    goStart () {
      this.$router.push({name: 'Start'})
    },
    onSizeExceeded (size) {
      alert(`Image ${size}Mb size exceeds limits of ${this.customImageMaxSize}Mb!`)
    },
    onAvatarLoaded (dataUri) {
      console.log(this.userId)
      this.image = dataUri
      var payload = {
        'id': this.userId,
        'data': {
          'avatar': dataUri
        }
      }
      this.$store.dispatch('setAvatar', payload)
    }
  },
  mounted () {
    this.image = this.avatar
  }
}
</script>
