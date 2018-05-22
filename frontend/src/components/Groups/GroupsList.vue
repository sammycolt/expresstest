<template>
  <div>
    <div class="card"  v-for="group in this.groups">
      <div class="card-header is-error">
        <button class="btn btn-clear float-right" @click="deleteGroup(group)"></button>
        <div class="card-title">Group: {{ groupDetails[group].name }}</div>
      </div>
    </div>
  </div>
</template>


<script>
import { mapState } from 'vuex'

export default {
  name: 'groups-list',
  props: ['testId'],
  computed: mapState({
    groups (state) {
      if (state.testDetails[this.testId]) {
        return state.testDetails[this.testId].groups_of_readers
      }
    },
    groupDetails (state) {
      return state.groupsDictionaryById
    },
    groupToTests (state) {
      return state.groupToTests
    }
  }),
  methods: {
    deleteGroup (groupId) {
      var payload = {
        'id': this.groupToTests[this.testId][groupId],
        'test': this.testId
      }
//      console.log('delete')
      this.$store.dispatch('deleteGroupToTest', payload)
    }
  }
}
</script>
