<template lang="pug">
  <div id="app">
    <div class="card" v-for="user in users">
      <div class="card-header">
        <button class="btn btn-clear"></button>
        <div class="card-title">{{ calculateType(user.type) }}</div>
      </div>
      <div class="card-body">{{ user.username }}</div>
      <div class="card-body">{{ user.email }}</div>
    </div>
  </div>
</template>

<script>

import { mapGetters } from 'vuex'
import { UserType } from '../enums/userType'

export default {
  name: 'users-list',
  computed: mapGetters(['users']),
  methods: {
    calculateType (type) {
      console.log(UserType[type])
      try {
        return UserType.properties[type].name
      } catch (err) {
        return UserType.properties[1].name
      }
    }
  },
  beforeMount () {
    this.$store.dispatch('getUsers')
  }

}

</script>

<style>
  header {
    margin-top: 50px;
  }
</style>
